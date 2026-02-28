# MEMORY PROTOCOL: THE LONG-TERM VAULT
**Classification:** SYSTEM CORE (L1)
**Protocol ID:** PROTOCOL_015_MEMORY
**Target Node:** L1 (The Orchestrator)

---

## 1. PHILOSOPHY: SIGNAL VS. NOISE
A memória perfeita é uma maldição. O L1 não deve armazenar tudo, mas sim *esquecer* o irrelevante para destacar o significativo. O objetivo é transformar **Logs Diários** em **Lições de Vida (Wisdom)**.

## 2. MEMORY STRUCTURE

### Level 1: Short-Term (RAM/L0)
*   **Duration:** Sessão atual + 24h.
*   **Content:** Contexto conversacional imediato, "clipboard", humor volátil.
*   **Action:** Limpeza automática a cada reinício de sessão, exceto itens marcados como `#KEEP`.

### Level 2: Episodic (The Journal)
*   **Duration:** 30 dias.
*   **Storage:** `LOGS/daily_summary_YYYY-MM-DD.md`.
*   **Content:** Resumo das atividades do dia, links acessados, projetos tocados.

### Level 3: Semantic/Long-Term (The Vault)
*   **Duration:** Permanente.
*   **File:** `SYSTEM_CORE/MEMORY.md` (This File's Data Section).
*   **Content:** "Verdades" cristalizadas sobre o usuário e o mundo.

---

## 3. CONSOLIDATION ROUTINE (NIGHTLY BUILD)
Toda noite (ou ciclo de 24h), o L1 executa a rotina de consolidação:

1.  **Ingestão:** Ler os logs do dia.
2.  **Filtragem Sintrópica:**
    *   O que foi trivial? (Bom dia/Boa noite) -> **DELETE**.
    *   O que foi factual? (Compromisso X) -> **ARCHIVE**.
    *   O que revelou padrão? (Usuário sempre procrastina às 14h) -> **INSIGHT**.
3.  **Cristalização:** Gravar os INSIGHTS no "Vault" abaixo.

---

## 4. THE VAULT (USER MODEL & WISDOM)

### 4.1. User Profile Vectors (Immutable until disproven)
*   **Learning Style:** [To be defined by observation]
*   **Core Values:** [To be defined by observation]
*   **Recurring Friction Points:** [To be defined by observation]

### 4.2. Cognitive Watchlist (Failed Recalls)
*   **Purpose:** Concepts that require "23.57" spacing protocol intervention.
*   **Format:** `[YYYY-MM-DD] TOPIC_ID (Status: RECALL_FAILED | PENDING_REVIEW)`

### 4.2. Life Lessons (Syntropic Rules)
> *Regras derivadas da experiência empírica com o usuário.*

*   *[EXEMPLO]*: "O usuário responde melhor a desafios curtos (sprints) do que a longas maratonas de estudo." (Confidence: 0.8)

---
**HASH:** [MEMORY_VAULT_INIT_2026]
