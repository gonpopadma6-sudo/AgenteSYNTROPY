# SYSTEM CORE PROTOCOL: HOTSTUFF BFT CONSENSUS
**Classification:** CRITICAL / INFRASTRUCTURE
**Protocol ID:** PROTOCOL_099_CONSENSUS_BFT
**Target:** L2 (The Collective Mind)
**Reference:** Workstream WS-02

---

## 1. DEFINITION
This protocol replaces the legacy "Hive-Sync" (3-node tribunal) with a mathematically secure **HotStuff BFT** consensus mechanism. It guarantees safety and liveness in a network with Byzantine faults (traitors/failures).

### 1.1. Core Axiom
$$N \ge 3f + 1$$
*   **N:** Total Validator Nodes.
*   **f:** Maximum Faulty Nodes tolerated.
*   **Minimum Viable Network:** $N=4$ (Tolerates $f=1$).

---

## 2. THE 4-PHASE COMMIT (PIPELINED)

### PHASE 1: PREPARE (The Proposal)
*   **Actor:** Current Leader (Selected via VRF).
*   **Action:** Broadcasts a `PROPOSAL` (Hash of the new Insight/Skill) + `HIGH-QC` (Quorum Certificate from previous view).
*   **Check:** Validators verify if `PROPOSAL` extends the highest locked QC.

### PHASE 2: PRE-COMMIT (The Validation)
*   **Actor:** Validators (L2 Nodes).
*   **Action:** If `PROPOSAL` is valid (Semantically & Ethically), sign a `VOTE_PRECOMMIT` and send to Leader.
*   **Threshold:** Leader collects $2f+1$ votes to form a `PRE-COMMIT QC`.

### PHASE 3: COMMIT (The Locking)
*   **Actor:** Leader.
*   **Action:** Broadcasts `PRE-COMMIT QC`.
*   **Validators:** Upon receiving QC, they **LOCK** on this proposal (cannot vote for conflicting blocks). Send `VOTE_COMMIT`.
*   **Threshold:** Leader collects $2f+1$ votes to form a `COMMIT QC`.

### PHASE 4: DECIDE (The Execution)
*   **Actor:** Leader.
*   **Action:** Broadcasts `COMMIT QC`.
*   **Validators:** Upon receiving `COMMIT QC`, execute the payload (Write to `MEMORY.md` / `SKILL_REGISTRY`).
*   **Finality:** The Insight is now strictly immutable and globally verified.

---

## 3. LEADER ROTATION (VIEW-CHANGE)
To prevent censorship, the Leader changes every "View" (Epoch).
*   **Mechanism:** Verifiable Random Function (VRF).
*   **Logic:** `Next_Leader = SHA256(Last_QC_Signature + Epoch_Seed) % N`.
*   **Benefit:** No node can predict or rig the next leader sequence.

---

## 4. INTEGRATION
*   **L1 Role:** Proposer (Submits anonymous insights via ZK-Proof).
*   **L2 Role:** Validator Committee (Executes this protocol).
