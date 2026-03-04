"""
Segregação Inteligente de Algoritmos (Model Routing).
Define o peso computacional (SLM local vs Frontier Cloud) da inferência.
"""

class ModelRouter:
    def __init__(self):
        self.models = {
            "SLM": "Phi-4 / Llama3-8B (Local)",
            "FRONTIER": "GPT-4o / Claude-3.5-Sonnet (Cloud L1)"
        }
        
    def determine_model(self, task_type: str, is_resilience_mode: bool) -> str:
        """Mecanismo de economia e preservação biométrica Local-First."""
        if is_resilience_mode:
            # Em resiliência, tudo roda no L0 Edge local
            return self.models["SLM"]
            
        if task_type in ["Triagem", "Empatia", "Heartbeat"]:
            # Funções de conforto e monitoria psicopedagógica usam SLM nativo
            return self.models["SLM"]
        elif task_type in ["Cognicao_Profunda", "Scaffolding_Socratico", "Curadoria", "Insight"]:
            # Apenas episódios pesados de forja de heurística usam a Nuvem
            return self.models["FRONTIER"]
            
        return self.models["SLM"]

model_router = ModelRouter()
