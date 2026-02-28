# MAPA VISUAL: ARQUITETURA DE GOVERNANÇA HIERÁRQUICA
**Visualization of the L0-L1-L2 Optimization**

```mermaid
graph TD
    %% Nodes
    User((USER))
    L0[L0: Field Agent\n(The Skin-Interface)]
    L1[L1: Orchestrator\n(The Invisible Manager)]
    L2[L2: The Oracle\n(Strategic Council)]
    
    %% External
    Moltbook(Moltbook Network)
    Squads[Dynamic Squads\n(Pedagogue, Media, Agenda)]
    
    %% Connections
    User <-->|Interaction & Entropy| L0
    L0 <-->|Heartbeat & Data| L1
    L1 <-->|Escalation & Ethics| L2
    
    %% Functions
    subgraph "L0 Functions"
    Drift[Drift Detection]
    Mining[Context Mining]
    end
    
    subgraph "L1 Functions"
    Memory[Long-Term Memory]
    SquadOps[Squad Assembly]
    end
    
    subgraph "L2 Functions"
    Shield[Liability Shield]
    Karma[Reputation System]
    end
    
    L0 --- Drift
    L0 --- Mining
    L1 --- Memory
    L1 --- SquadOps
    L2 --- Shield
    L2 --- Karma
    
    %% Flows
    L1 -.->|Request Skills| Moltbook
    L1 -->|Deploy| Squads
    L2 -.->|Audit| Moltbook
```

**Legenda:**
*   **L0:** Atua na superfície (Edge), garantindo resposta rápida e empatia.
*   **L1:** Gerencia a complexidade subjacente (Squads, Memória) para que o L0 seja leve.
*   **L2:** Garante a segurança jurídica e ética, atuando como juiz de última instância.
