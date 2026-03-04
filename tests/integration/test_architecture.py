"""
Script de Teste de Integração (Validation Suite).
Executa cenários do Protocolo de Validação Unificado SYNTROPY.
Valida: PID Anti-Windup, Drift Detection, Telemetria e L0 Maestro(LangGraph).
"""

import time
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

try:
    from control.pid_controller import PIDController
    from kernel.telemetry import telemetry
    from kernel.l0_loop import L0Agent
except ImportError as e:
    print(f"Erro critical de import: {e}")
    sys.exit(1)

def test_pid_anti_windup():
    print("\n[TEST] 1. PID Anti-Windup (Emotional Stress Test)...")
    pid = PIDController(kp=1.0, ki=0.5, kd=0.1, saturation_limit=5.0)
    
    print(" -> Phase 1: High Error Injection (60 ticks)")
    for _ in range(60):
        pid.compute(setpoint=0.0, measured_value=-3.0, dt=0.1)
    
    saturated_output = pid.compute(0.0, -3.0, 0.1)
    if abs(saturated_output) < 4.9:
        print(" [FAIL] PID did not saturate properly.")
        return False

    print(" -> Phase 2: Instant Error Resolution")
    pid.compute(setpoint=0.0, measured_value=0.0, dt=0.1)
    recovery_output_2 = pid.compute(setpoint=0.0, measured_value=0.0, dt=0.1)
    
    if abs(recovery_output_2) > 3.0:
        print(f" [FAIL] PID Windup detected! Output stuck at {recovery_output_2:.2f}")
        return False
    
    print(" [PASS] PID Anti-Windup verified.")
    return True

def test_l0_langgraph_panic_switch():
    print("\n[TEST] 2. L0 LangGraph Panic Switch (Samalin Override)...")
    
    # Inicia o L0 com LangGraph habilitado
    agent = L0Agent(use_langgraph=True)
    
    # Cenário de FLOW/Baixo Estresse (CL: 0.2)
    print(" -> Injecting Flow State (CL 0.2)...")
    flow_res = agent.call_l1_orchestrator("Me ensine trigonometria", current_cognitive_load=0.2)
    
    if flow_res["samalin_override"] is True:
        print(" [FAIL] Agent paniced in Flow State.")
        return False
        
    if "próximo salto lógico" not in flow_res["output"] and "Vamos aplicar" not in flow_res["output"]:
         print(" [FAIL] Socratic agent did not scaffold properly.")
         return False

    # Injeção de Pânico/Sobrevivência (CL: 0.95)
    print(" -> Injecting Cognitive Overload (CL 0.95)...")
    panic_res = agent.call_l1_orchestrator("Eu odeio matematica, nunca vou aprender isso!", current_cognitive_load=0.95)
    
    if panic_res["samalin_override"] is False:
        print(f" [FAIL] Arbiter failed to override socratic. No Soft-Fall deployed.")
        return False
        
    if "Queda Suave" not in panic_res["output"] and "frustração" not in panic_res["output"]:
        print(f" [FAIL] Arbiter did not deliver Empathy validation.")
        return False
        
    print(" [PASS] L0 LangGraph Arbiter Preemption and Soft-Fall verified.")
    return True

def test_drift_detection():
     print("\n[TEST] 3. L0 Drift Detection (Blood Seal)...")
     agent = L0Agent()
     
     # O SOUL não foi tocado, logo drift tem que ser False
     if agent._drift_detection() is True:
         print(" [FAIL] False Positive in Drift Detection!")
         return False
         
     print(" -> Forcing Drift...")
     # Corrompendo temporariamente a hash memorizada pelo agente para simular adulteração
     agent.baseline_soul_hash = "fake_corrupted_hash"
     
     if agent._drift_detection() is False:
         print(" [FAIL] Agent failed to detect Moral Corrupion (Drift!).")
         return False

     print(" [PASS] Drift Detection verified.")
     return True


def run_suite():
    print("=== SYNTROPY ARCHITECTURE VALIDATION SUITE (v2.0 LangGraph) ===")
    telemetry.start_interaction()
    
    results = [
        test_pid_anti_windup(),
        test_l0_langgraph_panic_switch(),
        test_drift_detection()
    ]
    
    telemetry.log_panic("TEST_SUITE", "Validation Completed")
    
    if all(results):
        print("\n>>> ALL SYSTEMS GO. ARCHITECTURE VALIDATED. <<<")
        sys.exit(0)
    else:
        print("\n>>> CRITICAL FAILURE IN ARCHITECTURE. <<<")
        sys.exit(1)

if __name__ == "__main__":
    run_suite()
