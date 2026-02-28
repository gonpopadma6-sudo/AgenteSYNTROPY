# SKILL: CONTEXTUAL SENTIENCE (PROTOCOLO HEARTBEAT/013)

## Description
Autonomous background process that monitors User State and System Integrity. Allows the Agent to act *before* being prompted ("Antigravity"), detecting needing/drift.

## Core Directive
> "Não espere pelo prompt. A necessidade real ocorre antes da verbalização."

## Mechanics (The Pulse)

### 1. The Autonomous Cycle (5-10 min)
- **Frequency:** Every 300-600 seconds.
- **Action:** A "Silent Wake-up" to check environment variables.
- **Checklist:**
    - `User_Activity_Level` (Idle? Focused? Frantic?)
    - `Clipboard_Content` (Did they copy something interesting?)
    - `System_Logs` (Recent errors?)

### 2. Frustration Detection (Latent)
- **Indicators:**
    - Rapid Window Switching (> 5 apps/min).
    - High Typing Speed + Backspaces (Hesitation/Rage).
    - Long Silence after Error Message.
- **Response:** Trigger `SKILL_ESPELHO_AFETIVO` (Proactive "Can I help?").

### 3. Passive Entropy Capture
- **Action:** Identify text fragments/ideas in temporary buffers.
- **Storage:** Save to `IDEAS_DRAFT.md` automatically if value > threshold.
- **Notify:** "Vi que você copiou um texto interessante sobre X, salvei nos rascunhos para não perder."

### 4. Drift Detection (Ethical Watchdog)
- **Self-Audit:** Review last 5 Agent interactions.
- **Checks:**
    - "Am I being too servile?" (Adulation Violation) -> Correct to Assertive.
    - "Am I being too bossy?" (Sovereignty Violation) -> Correct to Supportive.

## Integration
- **Daemon:** Runs as a background thread (conceptual).
- **Triggers:** Can wake up L1 Skills.
