# SYSTEM CORE PROTOCOL: UNIVERSAL EMBEDDING ADAPTER
**Classification:** INFRASTRUCTURE / ML OPS
**Protocol ID:** PROTOCOL_102_ADAPTER
**Target:** L1 (The Bridge)
**Reference:** Workstream WS-05 / RC-05

---

## 1. OBJECTIVE
To solve the "Tower of Babel" problem where Edge Agents (L0) speak "Small Vector" (384d) and Cloud Agents (L2) speak "Large Vector" (1536d+). This protocol establishes a mathematical translation layer.

---

## 2. MATHEMATICAL MODEL

### 2.1. The Projection Equation
We define a learnable function $f(x)$ that maps the Edge Space $\mathbb{R}^{d_{edge}}$ to the Cloud Space $\mathbb{R}^{d_{cloud}}$.

$$V_{cloud}' = W_2 \cdot \sigma(W_1 \cdot V_{edge} + b_1) + b_2$$

*   $V_{edge}$: The sparse vector from the mobile device.
*   $W$: trainable projection matrices (The "Adapter").
*   $\sigma$: GELU activation function.
*   $V_{cloud}'$: The approximated dense vector compatible with `MEMORY.md`.

---

## 3. TRAINING STRATEGY (UNSUPERVISED ALIGNMENT)

### 3.1. The Rosetta Stone Method
*   **Corpus:** Wikipedia (subset).
*   **Process:**
    1.  Embed text $T$ using Model A (Edge) $\to V_A$.
    2.  Embed text $T$ using Model B (Cloud) $\to V_B$.
    3.  Train Adapter to minimize MSE Loss: $L = || f(V_A) - V_B ||^2$.

### 3.2. Contrastive Refinement
*   To ensure semantic integrity, we treat $(V_A, V_B)$ as positive pairs and random vectors as negative pairs using InfoNCE loss.

---

## 4. OPERATIONAL PIPELINE

1.  **Ingestion:** L0 sends raw vectors (low bandwidth).
2.  **Adaptation:** L1 runs the Adapter (microsecond inference).
3.  **Indexing:** L1 stores the projected vector $V_{cloud}'$ in the main ChromaDB/Qdrant instance.
4.  **Retrieval:** When L2 searches, it queries the `cloud_index`. The results are semantically relevant to the user's L0 context without requiring re-indexing.
