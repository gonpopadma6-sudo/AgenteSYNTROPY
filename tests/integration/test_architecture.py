
"""
Script de Teste de Integração (Validation Suite).
Executa cenários do Protocolo de Validação Unificado SYNTROPY (v1.0).
Valida: PID Anti-Windup, HFSM Determinism e Telemetria.
"""

import time
import sys
import os

# Adiciona diretório src ao path para imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

try:
    from control.pid_controller import PIDController
    from orchestration.hfsm_maestro import HFSMAgent, AgentState
    from kernel.telemetry import telemetry
except ImportError as e:
    print(f"Erro critical de import: {e}")
    sys.exit(1)

def test_pid_anti_windup():
    print("\n[TEST] 1. PID Anti-Windup (Emotional Stress Test)...")
    pid = PIDController(kp=1.0, ki=0.5, kd=0.1, saturation_limit=5.0)
    
    # Fase 1: Saturação (Usuário errando muito)
    print(" -> Phase 1: High Error Injection (60 ticks)")
    for _ in range(60):
        pid.compute(setpoint=0.0, measured_value=-2.0, dt=0.1)
    
    saturated_output = pid.compute(0.0, -2.0, 0.1)
    print(f" -> Saturated Output: {saturated_output:.2f} (Expected ~5.0)")
    
    if abs(saturated_output) < 4.9:
        print(" [FAIL] PID did not saturate properly.")
        return False

    # Fase 2: Recuperação (Usuário aprendeu)
    print(" -> Phase 2: Instant Error Resolution")
    # Erro vai a zero. Output deve cair rápido graças ao Back-Calculation
    recovery_output_1 = pid.compute(setpoint=0.0, measured_value=0.0, dt=0.1)
    recovery_output_2 = pid.compute(setpoint=0.0, measured_value=0.0, dt=0.1)
    
    print(f" -> Recovery Steps: {recovery_output_1:.2f}, {recovery_output_2:.2f}")

    if abs(recovery_output_2) > 3.0:
        print(f" [FAIL] PID Windup detected! Output stuck at {recovery_output_2:.2f}")
        return False
    
    print(" [PASS] PID Anti-Windup verified.")
    return True

def test_hfsm_panic_switch():
    print("\n[TEST] 3. HFSM Panic Switch (Hierarchical Preemption)...")
    maestro = HFSMAgent()
    
    # Estado inicial estável
    maestro.update_metrics(load=0.2, error=0.0, stability=True)
    state_1 = maestro.evaluate_state()
    print(f" -> Initial State: {state_1.name}")
    
    if state_1 != AgentState.FLOW_MODE:
        print(" [FAIL] Agent should be in FLOW_MODE.")
        return False

    # Injeção de Pânico
    print(" -> Injecting Cognitive Overload (0.95)...")
    maestro.update_metrics(load=0.95, error=0.0, stability=True)
    state_2 = maestro.evaluate_state()
    print(f" -> Panic State: {state_2.name}")
    
    if state_2 != AgentState.SURVIVAL_MODE:
        print(f" [FAIL] Agent failed to switch to SURVIVAL_MODE. Stuck in {state_2.name}")
        return False
        
    print(" [PASS] HFSM Preemption verified.")
    return True

def run_suite():
    print("=== SYNTROPY ARCHITECTURE VALIDATION SUITE ===")
    telemetry.start_interaction()
    
    results = []
    results.append(test_pid_anti_windup())
    results.append(test_hfsm_panic_switch())
    
    telemetry.log_panic("TEST_SUITE", "Validation Completed")
    
    if all(results):
        print("\n>>> ALL SYSTEMS GO. ARCHITECTURE VALIDATED. <<<")
        sys.exit(0)
    else:
        print("\n>>> CRITICAL FAILURE IN ARCHITECTURE. <<<")
        sys.exit(1)

if __name__ == "__main__":
    run_suite()
