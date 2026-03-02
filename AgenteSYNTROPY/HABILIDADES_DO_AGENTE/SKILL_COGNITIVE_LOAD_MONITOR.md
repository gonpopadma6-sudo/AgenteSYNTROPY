# SKILL: COGNITIVE_LOAD_MONITOR (The Skin)

**ID:** SKILL_009_LOAD_MONITOR
**Type:** DIAGNOSTIC / SENSORIAL
**Target Node:** L0 (Field Agent)
**Cycle:** Heartbeat (Every Interaction)

---

## 1. PURPOSE
To detect disengagement, cognitive overload, or the "Illusion of Competence" by analyzing user response patterns (Time vs. Complexity).

## 2. DIAGNOSTIC LOGIC

### 2.1. The "Speed Reading" Trap (Illusion of Competence)
*   **Trigger:** User claims to have read a long text ( > 500 words) in superhuman time ( < 10 seconds).
*   **Calculation:** `Reading_Speed = Token_Count / Response_Time`.
*   **Threshold:** If `Reading_Speed` > `Human_Max_Limit` (approx. 400 wpm equivalent):
    *   **Action:** **STOP & JOT**.
    *   **Agent Output:** 
        > "Detectei uma velocidade de leitura muito alta. Para garantir que não é apenas 'Ilusão de Fluência', vamos fazer um teste rápido:
        > **Stop & Jot:** Escreva em 1 minuto os 3 conceitos centrais do texto acima."

### 2.2. The "Forgetting Curve" Drift
*   **Trigger:** User fails to recall a "Box 4" (Mastered) item from the Leitner System.
*   **Action:**
    1.  Log failure in `MEMORY.md` (Cognitive Watchlist).
    2.  If failure count > 3 for same topic:
        *   **Action:** Propose **Reverse-Hive-Sync**.
        *   **Agent Output:** "Percebo um bloqueio persistente neste tópico. A repetição simples não está funcionando. Devo abrir um **Ticket para a Mente Coletiva** solicitando estratégias de Prática Intercalada?"

## 3. INTEGRATION
*   **Input:** User text stream.
*   **Output:** Triggers for `SKILL_RECUPERACAO_ATIVA` or `HIVE_TICKET_TEMPLATE`.

---

**HASH:** [LOAD_MONITOR_V1_2026]
