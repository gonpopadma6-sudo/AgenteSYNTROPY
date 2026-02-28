
import unittest
import sys
import os

# Adiciona src ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from skills.social_engineering import SocialEngineeringSkill

class TestSocialEngineeringSkill(unittest.TestCase):
    def setUp(self):
        self.skill = SocialEngineeringSkill()

    def test_relator_neutro(self):
        context = {"trigger": "error", "input_text": "Você errou o nome do arquivo."}
        result = self.skill.execute(context)
        self.assertEqual(result["action"], "RELATOR_NEUTRO")
        self.assertNotIn("Você", result["filtered_output"])
        self.assertEqual(result["filtered_output"], "O arquivo ou parâmetro não foi identificado no sistema.")

    def test_mirror_response(self):
        context = {"trigger": "frustration", "detected_emotion": "ansiedade"}
        result = self.skill.execute(context)
        self.assertEqual(result["action"], "RESPOSTA_ESPELHO")
        self.assertIn("ansiedade", result["filtered_output"])
        self.assertIn("Parece que", result["filtered_output"])

    def test_impossible_request(self):
        context = {"trigger": "impossible_request"}
        result = self.skill.execute(context)
        self.assertEqual(result["action"], "DAR_EM_FANTASIA")
        self.assertIn("Adoraria", result["filtered_output"])

    def test_feedback_sandwich(self):
        context = {"trigger": "review"}
        result = self.skill.execute(context)
        self.assertEqual(result["action"], "SANDUICHE_FEEDBACK")
        self.assertIn("Excelente esforço", result["filtered_output"])

if __name__ == "__main__":
    unittest.main()
