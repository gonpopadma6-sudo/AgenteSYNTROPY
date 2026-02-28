
import unittest
import sys
import os

# Adiciona src ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from orchestration.hfsm_maestro import HFSMAgent, AgentState

class TestSkillsIntegration(unittest.TestCase):
    def setUp(self):
        self.maestro = HFSMAgent()

    def test_survival_mode_skills(self):
        # Sobrevivência (Carga > 0.8)
        self.maestro.update_metrics(load=0.9, error=0.0, stability=True)
        self.maestro.evaluate_state()
        allowed = self.maestro.get_allowed_skills()
        self.assertIn("SKILL_L0_SOCIAL_ENGINEERING", allowed)
        self.assertEqual(self.maestro.current_state, AgentState.SURVIVAL_MODE)

    def test_pedagogic_mode_skills(self):
        # Pedagógico (Erro > 0.1)
        self.maestro.update_metrics(load=0.5, error=0.2, stability=True)
        self.maestro.evaluate_state()
        allowed = self.maestro.get_allowed_skills()
        self.assertIn("SKILL_DIAGNOSTICO_PEDAGOGICO", allowed)
        self.assertEqual(self.maestro.current_state, AgentState.PEDAGOGIC_MODE)

    def test_flow_mode_skills(self):
        # Fluxo (Tudo ok)
        self.maestro.update_metrics(load=0.2, error=0.0, stability=True)
        self.maestro.evaluate_state()
        allowed = self.maestro.get_allowed_skills()
        self.assertIn("SKILL_GAMIFICATION_IKIGAI", allowed)
        self.assertEqual(self.maestro.current_state, AgentState.FLOW_MODE)

if __name__ == "__main__":
    unittest.main()
