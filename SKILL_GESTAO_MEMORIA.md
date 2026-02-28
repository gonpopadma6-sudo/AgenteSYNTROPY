# SKILL: SYNTROPIC MEMORY MANAGEMENT

## Description
Nightly process of converting Raw Logs into Wisdom. Prevents context window inflation and database pollution ("Digital Hoarding").

## Core Directive
> "Esquecer o irrelevante é tão importante quanto lembrar do essencial."

## Mechanics (The Distillation Process)

### 1. Ingestion (Raw Logs)
- **Source:** Chat logs, Command history, `HEARTBEAT` logs.
- **Time:** Low activity period (e.g., 04:00 AM).

### 2. Filtering (The Sieve)
- **Criteria:**
    - Is this fact permanent? (e.g., User hates Python) -> **KEEP**.
    - Is this transient? (e.g., User fixed typo on line 10) -> **DISCARD**.

### 3. Transmutation (Log -> Wisdom)
- **Algo:** `Synthesize(Events) -> Insight`.
- **Example:**
    - *Log:* User worked 4h on frontend, 30m on backend.
    - *Insight:* "Usuário tem preferência/flow maior em Frontend." -> Save to `PROFILE.md`.

### 4. Storage (Artifact Updates)
- **Target:** Update `MEMORY.md` and `SOUL.md` (Identity Matrix).
- **Pruning:** Delete raw logs older than 7 days.

## Integration
- **Output:** `Daily_Wisdom_Report.md`.
