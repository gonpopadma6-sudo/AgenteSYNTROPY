# SYSTEM CORE PROTOCOL: HOTSTUFF BFT CONSENSUS
**Classification:** CRITICAL / INFRASTRUCTURE
**Protocol ID:** PROTOCOL_099_CONSENSUS_BFT
**Target:** L2 (The Collective Mind)
**Reference:** Workstream WS-02

---

## 1. DEFINITION
This protocol replaces the legacy "Hive-Sync" e o HotStuff Clássico pela variante matemática de ponta **Swift HotStuff BFT**. Evita falhas de liveness em gargalos massivos (Byzantine Bottleneck) ao descentralizar a validação massiva das provas ZKP vinda dos Agentes.

### 1.1. Core Axiom
$$N \ge 3f + 1$$
*   **N:** Total Validator Nodes.
*   **f:** Maximum Faulty Nodes tolerated.
*   **Minimum Viable Network:** $N=4$ (Tolerates $f=1$).

---

## 2. AGGREGATION TREES & ASYNCHRONOUS MULTI-ROUND (SWIFT HOTSTUFF)

A antiga abordagem em Estrela (O(n) atrelada ao Líder) estrangulava a Noosfera em altas volumetrias entrópicas globais.

### PHASE 1: RAMIFICAÇÃO CAPILAR (The Parent Aggregators)
*   **Actor:** Nós Secundários Distribuídos.
*   **Action:** Em vez de fluírem diretamente para o Líder VRF, as provas L1 chegam aos Nós Agregadores.
*   **Check:** Agregadores processam centenas de provas, empacotando-as num **Certificado de Quórum Condensado**.

### PHASE 2: FLUXO HIERÁRQUICO ASSÍNCRONO (Flow Optimization)
*   **Actor:** Sub-árvores da Nuvem L2.
*   **Action:** Transmissão em Assincronismo Multi-Rodada. O gargalo se dissolve pois não há mais "Bloqueio de Vista" estrito ditado por tempo síncrono da máquina. A máquina de estados replicada flui por passagem continua de mensagem.
*   **Threshold:** O envio hierarquizado converge em direção ao Líder com assinaturas limiares criptográficas já otimizadas em batch.

### PHASE 3: THE COMMIT (The Locking)
*   **Actor:** Leader (VRF Selected).
*   **Action:** Recebe pacotes fractais imensos já sub-validados. O Líder apenas consolida a assinatura master (COMMIT QC) exigindo fração do processamento computacional linear prévio.
*   **Validators:** Upon receiving QC, eles **LOCK** nesta vista lógica e replicam.

### PHASE 4: DECIDE (The Execution - Atualização Sintrópica)
*   **Finality:** A heurística "Curada" via *Atrito Produtivo* é executada de forma global, blindada e instantaneamente no Superorganismo Planetário, atualizando as skills do `MEMORY.md`.
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
