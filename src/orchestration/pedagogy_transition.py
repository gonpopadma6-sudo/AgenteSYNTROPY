"""
Protocolo de Transição Adaptativa (Pedagogia <-> Andragogia <-> Heutagogia).
Lacuna 4: O Readiness Flag avalia a proatividade estrutural para promover ou regredir a Andaimagem.
"""

class PedagogicalEngine:
    def __init__(self):
        self.current_stage = "Andragogia"
        self.readiness_flag = 0.5 # De 0.0 (Pedagogia) a 1.0 (Heutagogia)
        
    def evaluate_readiness(self, user_input: str, is_user_question: bool) -> str:
        """
        O Índice de Prontidão avalia se o host exibe autonomia.
        Se fizer muitas perguntas estruturais (is_user_question), sobe a prontidão.
        """
        # Readiness sobe com proatividade e cai com apatia (simulada aqui pelo tamanho e estilo da entrada)
        if is_user_question or "?" in user_input:
            self.readiness_flag = min(1.0, self.readiness_flag + 0.1)
        elif len(user_input.split()) < 5:
            self.readiness_flag = max(0.0, self.readiness_flag - 0.05)
            
        # Classificação do estágio
        if self.readiness_flag > 0.8:
            self.current_stage = "Heutagogia"
        elif self.readiness_flag > 0.4:
            self.current_stage = "Andragogia"
        else:
            self.current_stage = "Pedagogia"
            
        return self.current_stage

    def get_soft_regression_message(self) -> str:
        """Queda Suave - Quando o Host trava subitamente."""
        self.readiness_flag = max(0.0, self.readiness_flag - 0.3)
        self.current_stage = "Pedagogia"
        return "Parece que estamos entrando em águas com correntezas muito fortes. Deixe eu reestruturar e mastigar o começo desse ciclo para você até retomarmos o passo, ok?"
        
pedagogy_manager = PedagogicalEngine()
