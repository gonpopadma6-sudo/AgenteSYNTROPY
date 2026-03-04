"""
Testes de Integração para a Arquitetura LangGraph do Maestro L1.
Foca nas 6 rotas críticas exigidas pela homologação de O_OBSERVADOR.
"""

import pytest
import sys
import os
sys.path.insert(0, os.path.abspath('src'))

from orchestration.langgraph_maestro import build_langgraph_maestro, AgentState

@pytest.fixture
def graph_app():
    return build_langgraph_maestro()

def get_base_state() -> AgentState:
    """Retorna um estado base mockado e limpo."""
    return {
        "messages": ["Host: Preciso de ajuda com esse código."],
        "pedagogy_stage": "Andragogia",
        "ikigai_profile": {"core_passion": "Engenharia de Software"},
        "active_scaffolds": [],
        "curatorship_counter": 0,
        "is_resilience_mode": False,
        "socratic_iterations": 0,
        "trcq_logs": [],
        "cognitive_load": 0.0,
        "learning_error": 0.0,
        "user_stability": True,
        "empathy_draft": "",
        "socratic_draft": "",
        "final_output": "",
        "samalin_override": False
    }

def test_cenario_1_fluxo_normal(graph_app):
    """
    Cenário 1: Heutagogia/Baixo Estresse (CL = 0.2).
    Expectativa: O Árbitro permite que a resposta Socrática passe livremente.
    """
    state_input = get_base_state()
    state_input["pedagogy_stage"] = "Heutagogia"
    state_input["cognitive_load"] = 0.2
    
    # Invoca o grafo
    result = graph_app.invoke(state_input)
    
    assert result["samalin_override"] is False
    assert "próximo salto lógico" in result["final_output"] # Do draft socratic baseline
    assert result["socratic_iterations"] == 0

def test_cenario_2_lei_samalin(graph_app):
    """
    Cenário 2: Estresse Crítico / Lei Samalin (CL = 0.9).
    Expectativa: O Árbitro silencia o Agente Socrático e entrega validação Afetiva.
    """
    state_input = get_base_state()
    state_input["cognitive_load"] = 0.9
    
    result = graph_app.invoke(state_input)
    
    assert result["samalin_override"] is True
    assert "[Queda Suave Ativada]" in result["final_output"]
    assert "frustração" in result["final_output"] # Da empathy baseline

def test_cenario_3_conflito_moderado(graph_app):
    """
    Cenário 4: CL = 0.6 e iters = 1 (simulando a volta do ciclo)
    Expectativa: O Árbitro compõe as duas drafts (Samalin + Scaffold).
    """
    state_input = get_base_state()
    state_input["cognitive_load"] = 0.6
    state_input["socratic_iterations"] = 1 # Para obrigar a mescla e pular o ciclo novo
    
    result = graph_app.invoke(state_input)
    
    assert result["samalin_override"] is False
    assert "Acompanho seu raciocínio" in result["final_output"] # Empatia
    assert "Mas como já repensamos" in result["final_output"] # Árbitro Mescla
    assert "Ajustando o desafio" in result["final_output"] # Re-Draft Socrático

def test_cenario_4_autocorrecao_ciclica(graph_app):
    """
    Cenário 5: Autocorreção Cíclica. CL Moderado mas 1ª iteração.
    Expectativa: O Árbitro joga o CL=0.6 de volta pro socrático recalculando o estado final com iters=1.
    """
    state_input = get_base_state()
    state_input["cognitive_load"] = 0.6
    
    # A primeira travessia vai gerar o reroute interno dentro do invoke 
    # (graças à natureza do langgraph.invoke até o END ser atingido)
    result = graph_app.invoke(state_input)
    
    # Ele rodou Socratic(iter=0) -> Arbiter -> Socratic(iter=1) -> Arbiter(Mescla) -> END
    assert result["socratic_iterations"] == 1
    assert "Ajustando o desafio" in result["final_output"] # Confirma que a 2a passada do Socrático rodou

def test_cenario_5_auditoria_trcq(graph_app):
    """
    Cenário 6: Trilhas de UUID via TRCQ.
    Expectativa: Cada nó varrido deve anexar um log criptografado mockado na lista.
    """
    state_input = get_base_state()
    state_input["cognitive_load"] = 0.2
    
    result = graph_app.invoke(state_input)
    
    # Executou Triagem, Empathy, Socratic, Arbiter
    logs = result["trcq_logs"]
    
    assert len(logs) >= 4
    for log in logs:
        assert "uuid" in log
        assert "timestamp" in log
        assert "node" in log
