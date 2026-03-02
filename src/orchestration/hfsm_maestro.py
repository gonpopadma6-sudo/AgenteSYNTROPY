
"""
Módulo de Orquestração HFSM (Hierarchical Finite State Machine).
Eixo IV do Plano de Resolução Arquitetural.
Resolve conflitos entre habilidades concorrentes de forma determinística.
"""

from enum import Enum, auto

class AgentState(Enum):
    SURVIVAL_MODE = auto()    # Prioridade Suprema (One-Word Mode)
    PEDAGOGIC_MODE = auto()   # Prioridade Intermediária (PBL/Socrático)
    FLOW_MODE = auto()        # Prioridade Inferior (Ghost Racing/Desafio)

class HFSMAgent:
    def __init__(self):
        self.current_state = AgentState.PEDAGOGIC_MODE
        self.cognitive_load = 0.0
        self.learning_error = 0.0
        self.user_stability = True

    def update_metrics(self, load: float, error: float, stability: bool):
        """Atualiza as métricas de entrada para a máquina de estados."""
        self.cognitive_load = load
        self.learning_error = error
        self.user_stability = stability

    def evaluate_state(self) -> AgentState:
        """
        Avalia as transições de estado baseadas na hierarquia rígida.
        
        Hierarquia:
        1. Sobrevivência (Carga Cognitiva > Limiar) -> One-Word Mode
        2. Pedagógico (Erro > 0 ou Instável) -> Socrático
        3. Fluxo (Erro ~ 0 e Estável) -> Desafio
        """
        
        # 1. Checagem de Sobrevivência (Preempção Absoluta)
        if self.cognitive_load > 0.8: # 80% de carga
            self.current_state = AgentState.SURVIVAL_MODE
            return self.current_state

        # 2. Checagem Pedagógica
        if self.learning_error > 0.1 or not self.user_stability:
            self.current_state = AgentState.PEDAGOGIC_MODE
            return self.current_state

        # 3. Modo de Fluxo (Se nada acima for verdade)
        self.current_state = AgentState.FLOW_MODE
        return self.current_state

    def get_allowed_skills(self):
        """Retorna a lista de habilidades permitidas no estado atual."""
        if self.current_state == AgentState.SURVIVAL_MODE:
            return ["SKILL_COGNITIVE_LOAD_MONITOR", "SKILL_ONE_WORD_MODE", "SKILL_L0_SOCIAL_ENGINEERING"]
        
        elif self.current_state == AgentState.PEDAGOGIC_MODE:
            return ["SKILL_PBL_ENGINE", "SKILL_RECUPERACAO_ATIVA", "SKILL_ESPELHO_AFETIVO", "SKILL_DIAGNOSTICO_PEDAGOGICO"]
        
        elif self.current_state == AgentState.FLOW_MODE:
            return ["SKILL_TRAINING_COACH", "SKILL_GAMIFICATION_IKIGAI"]
        
        return []

# Exemplo de uso:
# maestro = HFSMAgent()
# maestro.update_metrics(load=0.9, error=0.0, stability=True)
# new_state = maestro.evaluate_state() # Retorna SURVIVAL_MODE
