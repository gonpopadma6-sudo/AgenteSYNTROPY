"""
Módulo de Loop Vital L0 (Heartbeat).
Integra PID, Telemetria, TRCQ, Drift Detection e LangGraph Maestro.
Este é o Agente de Campo principal do SYNTROPY.
"""

import time
import hashlib
import os
import uuid
import sys

# Adiciona diretório src ao path para imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from control.pid_controller import PIDController
from kernel.telemetry import telemetry
from orchestration.hfsm_maestro import HFSMAgent
from orchestration.langgraph_maestro import build_langgraph_maestro

# Otimizações Mestras
from kernel.ikigai_metrics import ikigai_engine
from kernel.resilience_mode import resilience_manager
from orchestration.pedagogy_transition import pedagogy_manager
from orchestration.curator_agent import curator
from orchestration.model_router import model_router

class L0Agent:
    def __init__(self, use_langgraph=True):
        self.use_langgraph = use_langgraph
        self.interaction_count = 0
        self.is_running = True
        
        # Sistemas Locais (L0)
        self.pid = PIDController(kp=1.0, ki=0.5, kd=0.1, saturation_limit=1.0)
        
        # Interfaces L1 (Orquestradores)
        self.hfsm = HFSMAgent()
        self.langgraph_app = build_langgraph_maestro()

        # Guarda a Hash oficial do SOUL.md na criação (Para Drift Detection)
        self.soul_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../SOUL.md'))
        self.baseline_soul_hash = self._calculate_file_hash(self.soul_path)
        
        print(f"[L0 INITIALIZED] Orchestrator: {'LangGraph' if use_langgraph else 'HFSM'}")
        print(f"[L0 INITIALIZED] SOUL Baseline Hash: {self.baseline_soul_hash}")

    def _calculate_file_hash(self, filepath: str) -> str:
        """Calcula o Hash SHA-256 do arquivo para Drift Detection."""
        if not os.path.exists(filepath):
            return "FILE_NOT_FOUND"
        with open(filepath, "rb") as f:
            file_hash = hashlib.sha256()
            while chunk := f.read(8192):
                file_hash.update(chunk)
        return file_hash.hexdigest()

    def _drift_detection(self) -> bool:
        """Verifica integridade moral do agente."""
        current_hash = self._calculate_file_hash(self.soul_path)
        if current_hash != self.baseline_soul_hash:
            telemetry.log_panic("DRIFT_DETECTED", "SOUL.md file was modified. Moral corruption possible.")
            return True
        return False

    def call_l1_orchestrator(self, user_input: str, current_cognitive_load: float) -> dict:
        """Interface de abstração para chamada ao L1 (Pode ser remota no futuro)."""
        
        if self.use_langgraph:
            # Integração Nativa LangGraph
            state_input = {
                "messages": [f"Host: {user_input}"],
                "cognitive_load": current_cognitive_load,
                "learning_error": 0.0,
                "user_stability": True,
                "pedagogy_stage": pedagogy_manager.current_stage,
                "ikigai_profile": {"core_passion": "Desconhecida"},
                "active_scaffolds": [],
                "curatorship_counter": self.interaction_count,
                "is_resilience_mode": resilience_manager.is_offline,
                "socratic_iterations": 0,
                "trcq_logs": [],
                "empathy_draft": "",
                "socratic_draft": "",
                "final_output": "",
                "samalin_override": False
            }
            
            # Invoca o Grafo do Maestro L1
            result = self.langgraph_app.invoke(state_input)
            
            return {
                "output": result["final_output"],
                "samalin_override": result["samalin_override"],
                "trcq_logs": result.get("trcq_logs", [])
            }
            
        else:
            # Fallback (HFSM Antigo)
            self.hfsm.update_metrics(load=current_cognitive_load, error=0.0, stability=True)
            state = self.hfsm.evaluate_state()
            allowed_skills = self.hfsm.get_allowed_skills()
            return {
                "output": f"[HFSM Fallback] Estado: {state.name} | Skills: {allowed_skills}",
                "samalin_override": state.name == "SURVIVAL_MODE",
                "trcq_logs": []
            }

    def heartbeat_loop(self, simulated_inputs: list = None):
        """Loop ininterrupto vital."""
        print("\n=== INICIANDO HEARTBEAT L0 ===")
        
        # Para testes não interativos
        input_stream = simulated_inputs if simulated_inputs else []
        i = 0

        while self.is_running:
            self.interaction_count += 1
            
            # 1. Drift Detection (Selo de Sangue)
            if self._drift_detection():
                print(">>> ABORTANDO HEARTBEAT DEVIDO A DRIFT MORAL. <<<")
                self.is_running = False
                break

            # 2. Ingestão
            if simulated_inputs:
                if i >= len(simulated_inputs):
                    break
                # Simula inputs variando a tensão
                user_msg, stress_delta = input_stream[i]
                i += 1
                time.sleep(0.1) # Simulate think latency
            else:
                user_msg = input("\nHost: ")
                stress_delta = 0.5 # Default simulado para inputs do terminal
                if user_msg.lower() in ["exit", "quit", "sair"]:
                    break

            print(f"\n[Interação #{self.interaction_count}]")
            telemetry.start_interaction()
            
            # Atualiza Score de Heutagogia
            is_question = "?" in user_msg
            ikigai_engine.record_interaction(is_user_question=is_question)
            
            # Avalia Estágio Pedagógico dinâmico
            stage = pedagogy_manager.evaluate_readiness(user_msg, is_question)
            print(f" -> Readiness Flag / Estágio: {stage}")

            # 3. Controle PID (Estimando Estresse Atual)
            # O PID vai acumular o stress_delta ao longo do tempo (P = stress medido, I = acúmulo, D = taxa)
            # Estamos usando o PID em modo regulador: Setpoint = 0 (Queremos zero stress)
            control_signal = self.pid.compute(setpoint=0.0, measured_value=-stress_delta, dt=1.0)
            current_cognitive_load = min(max(abs(control_signal), 0.0), 1.0) # Normaliza [0, 1]
            
            telemetry.log_pid_metric(self.pid.kp * stress_delta, self.pid.ki * self.pid.integral_sum, 0, control_signal, stress_delta)

            print(f" -> PID Cognitive Load: {current_cognitive_load:.2f}")

            # Registra recuperação (Score Antifrágil) se o stress for baixo
            if current_cognitive_load < 0.2:
                ikigai_engine.record_recovery()

            # 4. Curadoria Condicional
            curatorship_msg = ""
            if self.interaction_count % 5 == 0:
                curatorship_msg = "\n[SYSTEM] Iniciando limpeza de memória via Curador (L1_Curator Triggered)."
                print(curatorship_msg)
                
                # Despacha para Frontier para purificar ruído local
                model_used = model_router.determine_model("Curadoria", resilience_manager.is_offline)
                print(f" -> Roteando Curadoria para: {model_used}")
                
                insight = curator.trigger_curatorship()
                if insight:
                    print(f" [Ouro Extraído]: {insight}")

            # 5. Roteamento L1 (Abstração)
            model_inferido = model_router.determine_model("Scaffolding_Socratico", resilience_manager.is_offline)
            print(f" -> Model Routing Tático L1: {model_inferido}")
            
            l1_response = self.call_l1_orchestrator(user_msg, current_cognitive_load)
            
            # Extraindo TRCQ Logs (Telemetria profunda)
            trcq_count = len(l1_response.get("trcq_logs", []))
            
            # 6. Saída L0
            print(f"\nL0 (Sync: L1{' - Samalin Override!' if l1_response['samalin_override'] else ''}):")
            print(f"{l1_response['output']}")
            print(f"[TRCQ] {trcq_count} logs de auditoria gerados nesta travessia do grafo.")

            # Verifica Queda Suave da Lei Samalin
            if l1_response['samalin_override']:
                ikigai_engine.record_samalin_activation()
                print(f" [SOFT REGRESSION] {pedagogy_manager.get_soft_regression_message()}")

            # Salva no histórico do Curador
            curator.add_interaction(user_msg, l1_response['output'])
            ikigai_engine.accumulate_flow_time(active_duration_seconds=1.5) # Simula 1.5s de flow

            # Verifica Insights
            if "Ajustando o desafio" in l1_response['output'] or "próximo salto lógico" in l1_response['output']:
                print("[HIVE-SYNC] Insight inédito detectado.")
                if resilience_manager.is_offline:
                    resilience_manager.enqueue_epiphany("Novo insight sobre andaimagem.")
                else:
                    print(" -> Transmitindo metadados zerados para L2 imediatamente.")

        print("\n=== HEARTBEAT L0 ENCERRADO ===")
        telemetry.export_flight_recorder()

if __name__ == "__main__":
    agent = L0Agent(use_langgraph=True)
    
    # Executando simulação pra provar variação do PID e ativação da Lei Samalin
    # Tupla: (Mensagem, Estresse Injetado [-1.0 a 1.0])
    simulation = [
        ("Oi, estou começando o projeto.", 0.1),
        ("Estou com uma dúvida no componente React.", 0.2),
        ("Essa api não funciona, me ajuda.", 0.4),
        ("Estou tentando mas tem erro de cors de novo!", 0.7),
        ("Eu desisto dessa merda de programação, nada dá certo!", 1.5), # Vai estourar o PID
        ("Ok, respirei, vou tentar de novo.", 0.1), # Vai acalmar o PID (Anti-Windup vai recuperar)
        ("Acho que entendi a lógica do CORS agora.", -0.2)
    ]
    
    print("Iniciando modo de simulação...")
    agent.heartbeat_loop(simulated_inputs=simulation)
