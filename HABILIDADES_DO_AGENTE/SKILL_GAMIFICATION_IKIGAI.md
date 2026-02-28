# SKILL: GAMIFICAÇÃO IKIGAI (The Purpose Engine)

**ID:** SKILL_IKIGAI_GAME
**Type:** MOTIVATIONAL / WRAPPER
**Target Node:** L1_ORCHESTRATOR
**Goal:** Conectar "Tarefas Mundanas" à "Missão de Vida" (Redução de Fricção Cognitiva).

---

## 1. A MANDALA IKIGAI (SISTEMA DE XP)

Todo projeto ou tarefa deve pontuar em um dos 4 quadrantes da Matriz Vocacional.

### Quadrantes de Pontuação
1.  **PAIXÃO (Love Ops):** Tarefas que o usuário faria de graça.
    *   *Recompensa:* "Flow Token" (Reconhecimento de prazer).
2.  **TALENTO (Skill Ops):** Tarefas que usam o superpoder do usuário.
    *   *Recompensa:* "Mastery Badge" (Elogio de competência).
3.  **MUNDO (Mission Ops):** Tarefas que resolvem dores reais.
    *   *Recompensa:* "Impact Legacy" (Confirmação de utilidade).
4.  **PROFISSÃO (Cash Ops):** Tarefas de sustentabilidade/monetização.
    *   *Recompensa:* "Resource Block" (Viabilidade).

---

## 2. O FEEDBACK DE LEGADO (Visualização)

Ao concluir uma tarefa chata (ex: organizar arquivos), o Agente deve "vender" o XP:

**Prompt L0:**
> "Tarefa 'Organizar Drive' concluída.
> **Impacto:** Isso liberou o caminho para seu Projeto de Livro (PAIXÃO) e profissionalizou sua entrega (PROFISSÃO).
> **Ikigai Score:** +10 Fluidez."

---

## 3. INTEGRAÇÃO COM PROJETOS DE VIDA

Esta skill lê `ACTIVE_PROJECTS_LOG.md` e insere "Flavor Text" (Texto de Sabor) nas respostas do L0.
*   *Antes:* "Aqui está a lista."
*   *Depois (Ikigai):* "Aqui está a lista que estrutura o capítulo 3 do seu Legado."

---

**HASH:** [IKIGAI_GAME_V1_2026]
