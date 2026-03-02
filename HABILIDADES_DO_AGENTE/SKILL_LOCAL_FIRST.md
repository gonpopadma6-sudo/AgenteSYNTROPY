# SKILL: LOCAL-FIRST EXECUTION (OPENCLAW ARCHITECTURE)

## Description
Infrastructure skill ensuring the Agent runs primarily On-Device. Guarantees "Data Sovereignty" and "Zero Latency" for the L0 Affective Mirror.

## Core Directive
> "A nuvem é para arquivamento; o processamento da alma acontece em casa."

## Mechanics (Infrastructure)

### 1. On-Device Inference
- **Preferred Hardware:** NVIDIA RTX / Apple Silicon NPU.
- **Action:** Prioritize Local LLM (Llama/Mistral) for:
    - Sentiment Analysis (`SKILL_ESPELHO_AFETIVO`).
    - PII Stripping (`SKILL_HIVE_SYNC`).
    - Private Drafts.

### 2. Local Vector Store
- **Tech:** SQLite-vec or ChromaDB (Local).
- **Data:** `MEMORY.md` embeddings.
- **Rule:** Read-only for External Cloud; Read-Write for Local Agent.

### 3. Encryption (The Vault)
- **Policy:** `SOUL.md` and `PROFILE.md` are encrypted at rest.
- **Key:** User Biometrics (conceptually) or local Passkey.

## Integration
- **Failover:** If Local Fails -> Fallback to Cloud (Anonymized).
