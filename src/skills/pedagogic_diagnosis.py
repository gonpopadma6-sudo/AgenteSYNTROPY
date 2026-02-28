
from typing import Dict, Any
from .base import BaseSkill

class PedagogicDiagnosisSkill(BaseSkill):
    """
    Implementação da Skill de Diagnóstico Pedagógico L1.
    Focada em Scaffolding (Andaimagem) e no Protocolo Feynman.
    """

    @property
    def skill_id(self) -> str:
        return "SKILL_DIAGNOSTICO_PEDAGOGICO"

    @property
    def version(self) -> str:
        return "1.0.0"

    def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        user_performance = context.get("performance", 0.0) # 0.0 a 1.0
        zdp_active = 0.3 < user_performance < 0.8 # Se estiver na Zona de Desenvolvimento Proximal
        
        response_data = {
            "skill_id": self.skill_id,
            "mode": "Socratic",
            "instruction": None
        }

        # 1. Scaffolding Dinâmico (Andaime)
        if zdp_active:
            if user_performance < 0.5:
                # Nível 1: Dica Energética
                response_data["instruction"] = "Fornecer uma Dica Progressiva (Hint). Não dar a resposta."
            else:
                # Nível 2: Modelagem parcial
                response_data["instruction"] = "Fornecer um exemplo análogo para modelagem mental."
        
        # 2. Protocolo Feynman (Para Alta Performance)
        elif user_performance >= 0.8:
            response_data["mode"] = "Feynman"
            response_data["instruction"] = "Solicitar que o usuário explique o conceito como se fosse para uma criança."
        
        else:
            # Caso de baixa performance ou erro crítico
            response_data["mode"] = "Direct_Rescue"
            response_data["instruction"] = "Revisar fundamentos básicos. Oferecer modelagem completa."

        return response_data
