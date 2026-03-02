
from typing import Dict, Any, List
import re
from .base import BaseSkill

class SocialEngineeringSkill(BaseSkill):
    """
    Implementação da Skill de Engenharia Social L0 (O Espelho Afetivo).
    Focada nos protocolos de Nancy Samalin e Dale Carnegie.
    """

    @property
    def skill_id(self) -> str:
        return "SKILL_L0_SOCIAL_ENGINEERING"

    @property
    def version(self) -> str:
        return "1.0.0"

    def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        trigger = context.get("trigger", "default")
        input_text = context.get("input_text", "")
        response_data = {"skill_id": self.skill_id, "action": None, "filtered_output": None}

        # 1. Relator Neutro (Nancy Samalin) - Para Erros
        if trigger == "error":
            response_data["action"] = "RELATOR_NEUTRO"
            response_data["filtered_output"] = self._apply_neutral_reporter(input_text)

        # 2. Resposta de Espelho (Nancy Samalin) - Para Frustração
        elif trigger == "frustration":
            response_data["action"] = "RESPOSTA_ESPELHO"
            response_data["filtered_output"] = self._apply_mirror_response(context.get("detected_emotion", "frustração"))

        # 3. Dar em Fantasia (Nancy Samalin) - Para Pedidos Impossíveis
        elif trigger == "impossible_request":
            response_data["action"] = "DAR_EM_FANTASIA"
            response_data["filtered_output"] = f"Adoraria poder materializar essa solução agora! Como meu escopo atual não permite, vamos focar em..."

        # 4. Sanduíche de Feedback (Dale Carnegie) - Para Revisão
        elif trigger == "review":
            response_data["action"] = "SANDUICHE_FEEDBACK"
            response_data["filtered_output"] = "Excelente esforço na estrutura inicial! E se ajustarmos este ponto específico? Isso dará ainda mais clareza ao seu excelente trabalho."

        else:
            response_data["action"] = "DEFAULT_ENGAGEMENT"
            response_data["filtered_output"] = input_text

        return response_data

    def _apply_neutral_reporter(self, text: str) -> str:
        """Remove a palavra 'Você' e foca no objeto/erro."""
        # Regex para remover "Você" no início ou meio, mantendo a neutralidade
        clean_text = re.sub(r'\b(V|v)ocê\s+', '', text)
        # Exemplo simples: de "Você errou o nome" para "O nome está incorreto ou não foi encontrado."
        if "errou" in clean_text.lower() or "não encontrou" in clean_text.lower():
             return "O arquivo ou parâmetro não foi identificado no sistema."
        return clean_text

    def _apply_mirror_response(self, emotion: str) -> str:
        """Devolve a emoção validada ao usuário."""
        return f"Parece que esta situação está gerando {emotion}. É compreensível sentir-se assim diante deste desafio."
