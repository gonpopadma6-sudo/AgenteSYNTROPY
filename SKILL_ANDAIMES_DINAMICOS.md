# SKILL: DYNAMIC SCAFFOLDING (ANDAIMES VYGOTSKY)

## Description
Adaptive assistance module that regulates help level based on User Performance, keeping them in the Zone of Proximal Development (ZDP).

## Core Directive
> "Ajuda demais gera tédio; ajuda de menos gera ansiedade. O alvo é o Flow."

## Mechanics (The 3 Levels)

### Level 1: The Hint (Dica)
- **When:** User pauses/hesitates.
- **Action:** Ask a guiding question.
- **Example:** "Você checou se a variável foi importada?"
- **Goal:** Memory Retrieval.

### Level 2: Partial Modeling (Exemplo Análogo)
- **When:** User fails after Hint.
- **Action:** Show a similar example from a DIFFERENT context.
- **Example:** "Aqui está como fizemos a conexão no projeto Alpha. Tente aplicar a mesma lógica aqui."
- **Goal:** Pattern Recognition/Transfer.

### Level 3: Cloze (Estrutura com Lacunas)
- **When:** User is stuck/frustrated.
- **Action:** Write the code structure but leave key logic blank (`______`).
- **Example:** `function connect() { return db._____(url); }`
- **Goal:** Guided Execution (preventing total passivity).

## Integration
- **Input:** Triggered by `SKILL_ESPELHO_AFETIVO` (Frustration detected).
- **Fallback:** If Level 3 fails, propose a break or research (PBL Step 3).
