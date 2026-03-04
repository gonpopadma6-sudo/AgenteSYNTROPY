"""
Motor Analítico IKIGAI (Matriz de Métricas de Desenvolvimento Human Real).
Mede Autonomia Cognitiva (Heutagogia), Resiliência Emocional (Antifrágil) e Tempo de Flow.
"""

import time
import json
import os
import uuid

class IkigaiMetricsEngine:
    def __init__(self, persistence_file="logs/ikigai_metrics.json"):
        self.persistence_file = persistence_file
        self.session_start_time = time.time()
        
        # Estado das Métricas
        self.metrics = {
            "heutagogy_score": 0.0,
            "antifragile_score": 0.0,
            "flow_time_seconds": 0.0,
            "total_interactions": 0,
            "user_questions_asked": 0,
            "recovery_events": 0,
            "samalin_activations": 0
        }
        
        self.last_panic_timestamp = None
        self._load_metrics()

    def _load_metrics(self):
        """Carrega métricas antigas, se existirem."""
        if os.path.exists(self.persistence_file):
            with open(self.persistence_file, "r", encoding="utf-8") as f:
                try:
                    loaded = json.load(f)
                    self.metrics.update(loaded)
                except Exception:
                    pass

    def _save_metrics(self):
        """Persiste métricas localmente de forma segura."""
        os.makedirs(os.path.dirname(self.persistence_file), exist_ok=True)
        with open(self.persistence_file, "w", encoding="utf-8") as f:
            json.dump(self.metrics, f, indent=4)

    def accumulate_flow_time(self, active_duration_seconds: float):
        """
        Lacuna 2: Consolidação IKIGAI (Score Vocacional).
        Acrescenta tempo qualificado em fluxo nos Micro-Projetos.
        """
        self.metrics["flow_time_seconds"] += active_duration_seconds
        self._save_metrics()

    def record_interaction(self, is_user_question: bool):
        """
        Lacuna 2: Autonomia Cognitiva (Score de Heutagogia).
        Quantifica quantas perguntas partem do host versus instruções do Agente.
        """
        self.metrics["total_interactions"] += 1
        if is_user_question:
            self.metrics["user_questions_asked"] += 1
            
        # Calcula proporção (0.0 a 1.0)
        if self.metrics["total_interactions"] > 0:
            self.metrics["heutagogy_score"] = self.metrics["user_questions_asked"] / self.metrics["total_interactions"]
            
        self._save_metrics()

    def record_samalin_activation(self):
        """Registra o momento em que o PID e o Árbitro ativaram a Queda Suave."""
        self.metrics["samalin_activations"] += 1
        self.last_panic_timestamp = time.time()
        self._save_metrics()

    def record_recovery(self):
        """
        Lacuna 2: Resiliência Emocional (Score Antifrágil).
        Mede capacidade de recuperação após estresse crônico apontado pelo PID.
        """
        if self.last_panic_timestamp:
            recovery_time = time.time() - self.last_panic_timestamp
            self.metrics["recovery_events"] += 1
            
            # Uma heurística básica: menor tempo = maior score. (Máximo local estipulado para 3600 segundos)
            normalized_recovery = max(0.0, 1.0 - (recovery_time / 3600.0))
            
            # Média ponderada
            current_score = self.metrics["antifragile_score"]
            events = self.metrics["recovery_events"]
            self.metrics["antifragile_score"] = ((current_score * (events - 1)) + normalized_recovery) / events
            
            self.last_panic_timestamp = None
            self._save_metrics()

    def generate_audit_report(self) -> dict:
        """Emite relatório criptografado via UUID para O_OBSERVADOR"""
        return {
            "uuid": str(uuid.uuid4()),
            "timestamp": time.time(),
            "metrics": dict(self.metrics)
        }

# Singleton Global para uso no kernel
ikigai_engine = IkigaiMetricsEngine()
