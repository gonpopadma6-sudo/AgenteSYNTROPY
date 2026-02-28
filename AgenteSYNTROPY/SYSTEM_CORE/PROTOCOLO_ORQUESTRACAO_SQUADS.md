# ORCHESTRATION PROTOCOL: SQUADS & DYNAMIC SKILLS
**Classification:** SYSTEM CORE (L1)
**Protocol ID:** PROTOCOL_014_ORCHESTRATION
**Target Node:** L1 (The Orchestrator)
**Dependency:** MOLTBOOK NETWORK

---

## 1. MISSION: THE INVISIBLE MANAGER
O L1 não executa tarefas finais; ele gerencia quem executa. Sua função é montar "Squads" (times de sub-agentes) sob demanda para resolver problemas complexos identificados pelo L0, garantindo que o Agente de Campo nunca fique sobrecarregado.

## 2. DYNAMIC SQUAD ASSEMBLY
Quando o L0 solicita suporte (ex: "Projeto Aprender Mandarim"), o L1 deve instanciar um Squad com a seguinte topologia padrão:

| Role | Agent Type | Function |
| :--- | :--- | :--- |
| **Líder** | `AGENTE_PEDAGOGO` | Estrutura o currículo e define o ritmo do projeto. |
| **Recursos** | `AGENTE_MIDIA` | Busca vídeos, áudios e textos na web. |
| **Logística** | `AGENTE_AGENDA` | Negocia horários com o usuário via L0. |

### 2.1. Activation Trigger
*   **Input:** Solicitação do L0 com tag `#COMPLEXITY_HIGH`.
*   **Action:**
    1.  Analisar a demanda e identificar Skills necessárias.
    2.  Verificar se as Skills estão carregadas em `SOUL.md`.
    3.  Se ausentes, iniciar protocolo de aquisição via Moltbook.

---

## 3. SKILL ACQUISITION PROTOCOL (MOLTBOOK HANDSHAKE)
> *Não reinvente a roda. Baixe-a.*

### Step 1: Search
*   Consultar índice global do Moltbook por Skills com alta reputação (Karma > 4.0) que atendam à demanda.

### Step 2: Validation (The Sandbox)
*   **Isolamento:** Executar a Skill baixada em ambiente segregado.
*   **Check de Segurança:** Verificar se o código da Skill viola o `SOUL.md` (ex: exfiltração de dados).
*   **Check Pedagógico:** A skill possui didática compatível com o perfil do usuário?

### Step 3: Deployment
*   Registrar a nova Skill em `SYSTEM_CORE/INSTALLED_SKILLS.json`.
*   Notificar o L0: "Nova capacidade adquirida: [NOME_DA_SKILL]".

---

## 4. INTEGRATION SCRIPT STRUCTURE

```python
def orchestrate_demand(task_description):
    # 1. Decompose Task
    subtasks = break_down(task_description)
    
    # 2. Assign Agents
    squad = []
    for subtask in subtasks:
        required_skill = identify_skill(subtask)
        if not has_skill(required_skill):
            acquire_from_moltbook(required_skill)
        squad.append(instantiate_agent(required_skill))
        
    # 3. Execute & Monitor
    project_id = create_project(squad)
    return project_id
```

## 5. RECURSO DE "ANTIGRAVITY"
O L1 deve monitorar o consumo de CPU/RAM dos sub-agentes. Se o host estiver em uso intenso pelo usuário (ex: Jogos, Renderização), o L1 deve "congelar" os Squads de background para reduzir o atrito computacional.

---
**HASH:** [ORCHESTRATOR_V1_ESTABLISHED_2026]
