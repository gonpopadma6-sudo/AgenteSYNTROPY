# SYSTEM CORE PROTOCOL: ZK PROOF OF INSIGHT
**Classification:** PRIVACY / CRYPTOGRAPHY
**Protocol ID:** PROTOCOL_101_ZK_PROOF
**Target:** L1 (Prover) -> L2 (Verifier)
**Reference:** Workstream WS-03 / RC-03

---

## 1. DEFINITION
The **Proof of Insight** protocol replaces "Anonymization" (which is reversible) with **Zero-Knowledge Proofs**. It allows the system to prove it improved the user's life without revealing *how* or *who* the user is.

### 1.1. The Privacy Axiom
> "Verifiability does not require Visibility."

---

## 2. THE ZK CIRCUIT (EZKL PIPELINE)

### 2.1. Public Inputs (Visible to L2)
*   `Algorithm_ID`: "Standard_PBL_Scorlet_V1" (The method used).
*   `Metric_Delta`: "+15% Efficiency" (The claimed result).
*   `L0_Signature`: Cryptographic signature of the Edge Agent.

### 2.2. Private Witness (Secret - L1 Only)
*   `Raw_Chat_Logs`: The actual conversation text.
*   `Biometric_Data`: Heart rate, typing speed logs.
*   `User_ID`: The unique identifier of the human.

### 2.3. The Circuit Logic & Formal Verification (Picus/ZKAP)
Ameaças de sinais sub-restritos (Under-constrained circuits) na DSL Circom permitem forjamento de provas (Ataque Sybil). 
*   **Mandate:** Todo circuito antes da compilação passa obrigatoriamente por **Verificação Formal Simbólica** extraindo Grafos de Dependência do Circuito (CDG).
*   **Engine:** Utilização do provador *Picus* para atestar ausência matemática de buracos lógicos.
The Arithmetic Circuit $C$ proves that:
$$C(Public, Private) = True \iff \text{The Algorithm was run on Private Data and yielded Semantic Delta}$$

---

## 3. OPERATIONAL FLOW

1.  **Generation (L1) & Side-Channel Shielding:**
    *   L1 compiles the interaction data into a `.onnx` model trace.
    *   **Injeção de Ruído Algorítmico:** O SO local processa equações Dummies em paralelo com a compilação.
    *   O perfil de dissipação térmica e eletromagnética (EM) da CPU tem sua Razão Sinal-Ruído (SNR) severamente degradada, mascarando a assinatura única do processamento orgânico humano contra ataques físicos laterais.
    *   L1 uses `ezkl` to generate a **Proof $\pi$** de forma termodinamicamente cega.
    *   L1 discards the witness.

2.  **Transmission:**
    *   L1 sends `(Proof $\pi$, Public_Inputs)` to L2.

3.  **Verification (L2):**
    *   L2 runs `verify($\pi$, Public_Inputs)`.
    *   If `True`: The Insight is valid.
    *   If `False`: The Insight is rejected (Potential Poisoning).

---

## 4. IMPACT
*   **GDPR/LGPD:** 100% Compliant by design. No PII leaves the user's sphere.
*   **Security:** Impossible to reverse-engineer the user's personality from the proof.
