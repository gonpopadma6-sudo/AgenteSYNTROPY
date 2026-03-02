
"""
Módulo de Observabilidade do Kernel (Eixo VII).
Instrumentação OpenTelemetry para os '4 Artefatos da Verdade'.
"""

import time
import uuid
import json
# Em produção, importaríamos opentelemetry-api e sdk
# from opentelemetry import trace
# from opentelemetry.trace import Status, StatusCode

class TelemetryKernel:
    def __init__(self, service_name="syntropy-agent"):
        self.service_name = service_name
        self.interaction_id = None
        self.flight_recorder_data = [] # Buffer para Flight Recorder (PID)
        self.panic_logs = []
        
        # Mock do Tracer Provider
        self.tracer = self._mock_tracer_provider()

    def _mock_tracer_provider(self):
        return "OTEL_TRACER_MOCK"

    def start_interaction(self):
        """Inicia um novo Root Span para uma interação do usuário."""
        self.interaction_id = str(uuid.uuid4())
        print(f"[TELEM] Starting Trace: {self.interaction_id}")
        # tracer.start_as_current_span("interaction_root")

    def log_pid_metric(self, p, i, d, u_t, user_stress_level):
        """Registra métricas do controlador para o Flight Recorder (telemetry.csv)."""
        metric_entry = {
            "timestamp": time.time(),
            "interaction_id": self.interaction_id,
            "P": p,
            "I": i,
            "D": d,
            "Output": u_t,
            "UserStress": user_stress_level
        }
        self.flight_recorder_data.append(metric_entry)
        # Em produção, exportar via OTLP Metrics

    def log_decision_trace(self, input_context, decision_logic, output_action):
        """Gera o Explainability Trace (decision_trace.json)."""
        trace_entry = {
            "interaction_id": self.interaction_id,
            "trigger": "HFSM_Transition",
            "context_hash": hash(input_context),
            "logic_path": decision_logic, # Ex: "State: Pedagogic -> Detected Error -> Action: Socratic Question"
            "final_action": output_action
        }
        with open(f"logs/decision_trace_{self.interaction_id}.json", "w") as f:
            json.dump(trace_entry, f, indent=2)

    def log_panic(self, error_type, message):
        """Registra anomalias críticas (Panic Logs)."""
        panic_entry = {
            "timestamp": time.time(),
            "severity": "CRITICAL",
            "error": error_type,
            "message": message,
            "interaction_id": self.interaction_id
        }
        self.panic_logs.append(panic_entry)
        print(f"[PANIC] {error_type}: {message}")

    def export_flight_recorder(self):
        """Salva o buffer do Flight Recorder em CSV."""
        if not self.flight_recorder_data:
            return
        
        filename = f"logs/telemetry_{self.interaction_id}.csv"
        # Implementar escrita CSV simples
        header = "timestamp,interaction_id,P,I,D,Output,UserStress\n"
        with open(filename, "w") as f:
            f.write(header)
            for entry in self.flight_recorder_data:
                line = f"{entry['timestamp']},{entry['interaction_id']},{entry['P']},{entry['I']},{entry['D']},{entry['Output']},{entry['UserStress']}\n"
                f.write(line)
        self.flight_recorder_data = [] # Limpar buffer

# Singleton
telemetry = TelemetryKernel()
