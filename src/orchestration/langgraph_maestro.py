"""
Módulo de Orquestração LangGraph (L1).
Resolve conflitos entre habilidades PPA e a Lei Samalin via Grafo Cíclico.
"""

from typing import TypedDict, Annotated, List, Dict, Any, Optional
import operator
import uuid
from datetime import datetime
from langgraph.graph import StateGraph, END

# --- 1. EXPANSÃO DO AGENT STATE (RES. LACUNAS PARECER) ---

def add_logs(left: list, right: list):
    """Função de redução para concatenar logs."""
    if not left: left = []
    if not right: right = []
    return left + right

class AgentState(TypedDict):
    # Core Data
    messages: list
    
    # Métricas Base (Heartbeat L0)
    cognitive_load: float
    learning_error: float
    user_stability: bool
    
    # Classificação Pedagógica (Pedagogia/Andragogia/Heutagogia)
    pedagogy_stage: str
    
    # --- Adições Exigidas pelo O_OBSERVADOR ---
    
    # IKIGAI e Vocação
    ikigai_profile: Dict[str, Any]
    
    # Memória de Andaimes Ativos (PPA Tracker)
    active_scaffolds: List[str]
    
    # Gatilhos de Sistema
    curatorship_counter: int
    is_resilience_mode: bool
    
    # Arbitragem e Self-Correction
    samalin_override: bool
    socratic_iterations: int
    
    # Trilha Forense (Auditoria)
    trcq_logs: Annotated[list, add_logs]
    
    # Output Intermediário/Final
    empathy_draft: str
    socratic_draft: str
    final_output: str


# --- 2. CONFIGURAÇÕES E PROMPTS GLOBAIS ---

SAMALIN_CARNEGIE_PROMPT = """
Sua função é atuar como o NÓ EMPATIA (A Lei Samalin).
Você nunca ensina, nunca cobra, nunca avalia neste momento.
Sua única diretriz é a CONEXÃO ANTES DA CORREÇÃO.

Técnicas Obrigatórias (Adele Faber/Elaine Mazlish & Dale Carnegie):
1. Ouça com o coração: Valide a emoção do Host explicitamente. Dê nome ao sentimento ("Parece frustrante", "Vejo que isso te cansou").
2. Aceite desejos em fantasia: Se a realidade é dura, alivie concordando que seria bom ter uma varinha mágica.
3. Não use a palavra "MAS". Substitua por silêncio ou "E".
4. Seja genuíno no interesse (Carnegie): Faça com que o host se sinta importante e ouvido.

Analise o texto e gere UMA recomendação de validação emocional focada na mitigação da frustração.
"""

SOCRATIC_PBL_PROMPT = """
Sua função é atuar como o NÓ SOCRÁTICO (Protocolo de Provação Antifrágil - PPA e PBL Engine).
Você constrói Andaimes Dinâmicos baseados no Estágio Pedagógico e no Perfil Vocacional (IKIGAI) do Host.

Diretrizes de Estágio:
- Se Pedagogia: Estrutura estrita, dê passos claros, não exija saltos gigantes.
- Se Andragogia: Negocie o termo, faça o Host escolher entre opções.
- Se Heutagogia: Dê apenas a 'Próxima Pergunta Motriz' e deixe o Host formular a estrutura.

Analise o cenário, verifique os Andaimes já ativos para não repeti-los e avance a dificuldade no limiar correto.
"""

# --- 3. HELPER FORENSE (TRCQ UUID) ---

def create_trcq_log(node_name: str, action: str, metrics: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "uuid": str(uuid.uuid4()),
        "timestamp": datetime.utcnow().isoformat(),
        "node": node_name,
        "action": action,
        "metrics": metrics
    }

# --- 4. DEFINIÇÃO DOS NÓS (NODES) ---

def triagem_node(state: AgentState):
    """
    Nó 1: Consumidor do Heartbeat Local e Classificador.
    Injeta o contexto L0 dentro do Grafo L1.
    """
    # Em um MVP heurístico, assumiremos que cognitive_load já foi injetado pela entrada
    # O nó loga a passagem para auditoria
    log = create_trcq_log("triagem_node", "context_ingestion", {"cognitive_load": state.get("cognitive_load", 0.0)})
    return {"trcq_logs": [log]}

def empathy_node(state: AgentState):
    """
    Nó 2A: Análise Emocional (Executado em Paralelo com Socrático).
    Gera as draft responses focadas na Lei Samalin.
    """
    # MOCK MVP Heurístico: Para fins de validação estrutural sem dependência de LLM nesta iteração
    cl = state.get("cognitive_load", 0.0)
    
    if cl > 0.8:
        draft = "Reconheço que isso está cobrando um preço alto da sua mente. Está tudo bem travar aqui. Quer apenas falar sobre a frustração?"
    else:
        draft = "Acompanho seu raciocínio. Vejo que a energia está boa."
        
    log = create_trcq_log("empathy_node", "draft_generation", {"sentiment_intensity": cl})

    return {"empathy_draft": draft, "trcq_logs": [log]}

def socratic_node(state: AgentState):
    """
    Nó 2B: O Motor do PBL (Executado em Paralelo com Empatia).
    Gera o desafio pedagógico alinhado ao IKIGAI.
    """
    stage = state.get("pedagogy_stage", "Andragogia")
    iters = state.get("socratic_iterations", 0)
    
    # Se retornou pela aresta cíclica para correção
    if iters > 0:
        draft = f"[Correção Iter {iters}] Ajustando o desafio para ser menos complexo conforme diretriz do árbitro. {stage}: Qual a estrutura base que você vê?"
    else:
        draft = f"Vamos aplicar isso no seu projeto. Considerando que estamos em {stage}, qual o seu próximo salto lógico?"

    log = create_trcq_log("socratic_node", "scaffolding_generation", {"pedagogy_stage": stage, "iteration": iters})

    return {"socratic_draft": draft, "trcq_logs": [log]}

def arbiter_node(state: AgentState):
    """
    Nó 3: O Árbitro Limitador da Lei Samalin e Autocorreção.
    Garante a saúde mental e aplica o ciclo de correção.
    """
    cl = state.get("cognitive_load", 0.0)
    thresh = 0.8 # Limiar padrão "Hardcoded" para o MVP, conforme discussão
    
    emp_draft = state.get("empathy_draft", "")
    soc_draft = state.get("socratic_draft", "")
    iters = state.get("socratic_iterations", 0)

    # Regra 1: Aplicação da Queda Suave (Estresse Crônico)
    if cl > thresh:
        final = f"[Queda Suave Ativada] {emp_draft}"
        override = True
        log = create_trcq_log("arbiter_node", "samalin_override", {"cl": cl, "threshold": thresh})
        
    # Regra 2: Conflito Moderado / Zona de Transição Composicional
        # Se a carga for moderada e a iteração socrática for 0, o árbitro pode exigir recálculo (Ciclo Cíclico)
    elif cl > 0.5:
        if iters < 1:
            log = create_trcq_log("arbiter_node", "self_correction_trigger", {"cl": cl, "action": "send_back_to_socratic"})
            return {
                "socratic_iterations": iters + 1,
                "trcq_logs": [log]
            }
        else:
            final = f"{emp_draft}\nMas como já repensamos... {soc_draft}"
            override = False
            log = create_trcq_log("arbiter_node", "composed_output", {"cl": cl})
            
    # Regra 3: Fluxo Normal / Heutagogia
    else:
        final = soc_draft
        override = False
        log = create_trcq_log("arbiter_node", "socratic_pass", {"cl": cl})

    return {"final_output": final, "samalin_override": override, "trcq_logs": [log]}

# --- 5. LÓGICA DE ROTEAMENTO (CONDITIONAL EDGES) ---

def route_after_arbiter(state: AgentState):
    """
    Define se o Árbitro finaliza a requisição ou se devolve para Autocorreção Cíclica.
    """
    iters = state.get("socratic_iterations", 0)
    final_out = state.get("final_output")
    
    # Se o output final não foi setado, significa que o árbitro pediu recálculo no fluxo (Self-Correction)
    if not final_out and iters > 0 and iters <= 2:
        return "re_route_socratic"
    
    return "end"

# --- 6. COMPILE DO GRAFO ---

def build_langgraph_maestro():
    """
    Monta a topologia MVP Cíclica baseada no parecer do O_OBSERVADOR.
    """
    workflow = StateGraph(AgentState)
    
    # Adicionando os nós
    workflow.add_node("triagem", triagem_node)
    workflow.add_node("empathy", empathy_node)
    workflow.add_node("socratic", socratic_node)
    workflow.add_node("arbiter", arbiter_node)
    
    # Arestas do Início para a Triagem
    workflow.set_entry_point("triagem")
    
    # Execução Paralela da Triagem para Empatia e Socrático
    workflow.add_edge("triagem", "empathy")
    workflow.add_edge("triagem", "socratic")
    
    # Ambos alimentam o Árbitro
    workflow.add_edge("empathy", "arbiter")
    workflow.add_edge("socratic", "arbiter")
    
    # Aresta Cíclica Condicional (A Magia da Autocorreção)
    workflow.add_conditional_edges(
        "arbiter",
        route_after_arbiter,
        {
            "re_route_socratic": "socratic", # Volta pro socratic com constraint
            "end": END
        }
    )
    
    app = workflow.compile()
    return app

# Exemplo de compilação
# app = build_langgraph_maestro()
