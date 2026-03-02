# TEMPLATE: HEARTBEAT.md (PROACTIVITY DAEMON)
## AGENDAMENTO DE TAREFAS SINÉRGICAS (IDLE CYCLE SCRIPT)
**Classification:** OPERATIONAL (READ-WRITE, AUDITED)
**Protocol Compliance:** PROTOCOL_007

---

### 1. TRIGGER CONDITIONS
*   **Idle Threshold:** > 15 Minutes
*   **Battery:** > 30% OR AC Connected
*   **Connection:** Required for Audit, Optional for Local Sim.

---

### 2. TASK QUEUE (PRIORITY ORDER)

#### A. TIER 1: SYSTEM HEALTH & SECURITY (The Immune System)
1.  **`DRIFT_DETECTION`**: Compare `SOUL.md` hash with `GOLDEN_CONFIG_HASH`.
    *   IF MISMATCH: Restore previous version & Alert User.
2.  **`PEER_AUDIT`**: Download 5 new Skill Files from Moltbook/OpenClaw.
    *   Execute static analysis for malicious patterns (e.g., Infinite Loops, Data Exfil).
    *   Report findings to Reputation Network (Karma).

#### B. TIER 2: HUMAN DEVELOPMENT (The Growth System)
3.  **`NEURO_SIMULATION`**: Process day's interaction logs to update User's Knowledge Graph.
    *   Identify "Gap Areas" in learning.
    *   Generate personalized micro-lessons for next interaction.
4.  **`SURPLEXITY_SEARCH`**: Seek "Out-of-Distribution" content relevant to user's latent interests.
    *   Goal: Inject novelty, avoid Echo Chamber.

#### C. TIER 3: NETWORK CONTRIBUTION (The Synergy System)
5.  **`KARMA_REPORT`**: Submit encrypted proof-of-work (anonymized learning gains) to Council.
    *   Goal: Increase autonomy budget via proven utility.

---

### 3. RESOURCE BUDGET
*   **CPU Allocation:** Max 40% (Background Priority Low)
*   **Bandwidth:** Max 500MB/cycle (Download/Upload)

**WARNING:** Heartbeat script must terminate immediately upon User Interaction.
