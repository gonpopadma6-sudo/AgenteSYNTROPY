
from abc import ABC, abstractmethod
from typing import Dict, Any, List

class BaseSkill(ABC):
    """
    Interface base para todas as habilidades (skills) do Agente SYNTROPY.
    Garante que cada habilidade tenha um ID, versão e um método de execução padronizado.
    """
    
    @property
    @abstractmethod
    def skill_id(self) -> str:
        pass

    @property
    @abstractmethod
    def version(self) -> str:
        pass

    @abstractmethod
    def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Executa a lógica da habilidade baseada no contexto fornecido.
        
        Args:
            context (Dict[str, Any]): Dicionário contendo os dados de entrada, 
                                     estado do usuário e métricas.
        
        Returns:
            Dict[str, Any]: Resultado da execução, incluindo a resposta sugerida
                           e metadados de telemetria.
        """
        pass

    def __repr__(self):
        return f"<{self.__class__.__name__} id={self.skill_id} v={self.version}>"
