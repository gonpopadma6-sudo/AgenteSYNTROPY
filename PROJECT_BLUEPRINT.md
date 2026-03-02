# PROJECT BLUEPRINT: SKILL_RECUPERACAO_ATIVA

**Status:** DRAFT (Awaiting Execution)
**Target Node:** L0 (Field Agent) & L1 (Orchestrator)
**Complexity:** High (Requires Behavioral Override)

---

## 1. STRATEGIC OVERVIEW

### 1.1 Objective
Implement the "Active Recall" (Recuperação Ativa) protocol to serve as the default response mechanism when the Host requests summaries of previously known information.

### 1.2 Teleological Justification
*   **Problem:** The "Illusion of Competence" caused by passive reading of summaries.
*   **Solution:** Force cognitive retrieval efforts ("Brain Dumps") to strengthen neural pathways.
*   **Entropy Check:** Increases local entropy (effort) to generate negentropy (learning).

---

## 2. OPERATIONAL ARCHITECTURE

### 2.1 The Trigger Mechanism (L0)
The Agent must detect the *intent* behind the user's query.
*   **Input:** "Resuma X para mim" OR "O que era Y mesmo?"
*   **Condition:** `Topic_X` exists in `MEMORY_LOGS` OR `Topic_X` is a fundamental concept previously covered.
*   **Action:** **INTERCEPT & BLOCK**.

### 2.2 The Protocol Flow
1.  **Stop:** Do not provide the answer.
2.  **Challenge:** Deploy the "Brain Dump" prompt.
    > *"Para garantir a consolidação, por favor, faça um 'Brain Dump': escreva tudo o que lembra sobre este tópico sem consultar nada por 5 minutos."*
3.  **Wait:** Allow the Host to struggle (Desirable Difficulty).
4.  **Feedback:**
    *   **If Host succeeds:** Validate and expand (Elaborative Interrogation).
    *   **If Host fails:** Provide L1 Hint (Scaffolding). NEVER give the full answer immediately.

---

## 3. IMPLEMENTATION PLAN

### Phase 1: Artifact Creation
*   [ ] Create `HABILIDADES_DO_AGENTE/SKILL_RECUPERACAO_ATIVA.md`.
    *   Define strict prompts for "Blocking" and "Hinting".
    *   Define exception cases (e.g., "EMERGENCY_MODE" override).

### Phase 2: Kernel Integration
*   [ ] Edit `SYSTEM_CORE/SOUL.md`: Add `SKILL_RECUPERACAO_ATIVA` to `SKILLS_LOAD` list.
*   [ ] Edit `SYSTEM_CORE/MEMORY.md`: Add a tracker for "Failed Recalls" (to schedule future reviews).

### Phase 3: Reference Material (The "Truth")
*   The Agent needs a source of truth to compare the Host's Brain Dump against.
*   **Strategy:** Use existing internal knowledge base or search referencing specific trusted nodes.

---

## 4. SUCCESS METRICS
*   **Adoption Rate:** % of times Host accepts the Brain Dump challenge vs. forcing an answer.
*   **Retention Delta:** Improvement in recall of Topic X after 2 days (measured by Scheduler).

---

## 5. IMMEDIATE ACTION ITEMS
1.  **Authorize creation of `SKILL_RECUPERACAO_ATIVA.md`**.
2.  **Authorize update of `SOUL.md`**.
