# FLUXOGRAMA: SISTEMA DE SINERGIA V2 (Deep Cognition & Loop-Ouroboros)

> **Nota:** Este fluxograma foi gerado em linguagem Mermaid, compatível com Obsidian. Para visualizar graficamente, certifique-se de que o plugin Mermaid esteja ativo.

```mermaid
graph TD
    %% --- ESTILOS ---
    classDef human fill:#f9f,stroke:#333,stroke-width:2px;
    classDef l0 fill:#90ee90,stroke:#333,stroke-width:1px;
    classDef l1 fill:#87cefa,stroke:#333,stroke-width:1px;
    classDef l2 fill:#dda0dd,stroke:#333,stroke-width:1px;
    classDef output fill:#ffa07a,stroke:#333,stroke-width:1px;

    %% --- ATORES ---
    Host((HOST HUMANO)):::human
    
    %% --- FLUXO INICIAL ---
    Host -->|Input Txt/Voz| L0_Sensor{L0: SENSOR HEARTBEAT}:::l0
    
    %% --- LEITURA DE CARGA COGNITIVA (NOVO) ---
    L0_Sensor -- "Leitura Rápida (<5s) ou Falha em Leitner" --> LoopLoad[SKILL: COGNITIVE_LOAD_MONITOR]:::l0
    LoopLoad -->|Trigger| StopJot[AÇÃO: STOP & JOT / BRAIN DUMP]:::output
    StopJot -->|Validação| Host
    
    %% --- ROTEAMENTO PADRÃO ---
    L0_Sensor -- "Fluxo Normal" --> L2_Check{L2: FILTRO SEMÂNTICO}:::l2
    L2_Check -- "Entrópico/Finito" --> Bloqueio[BLOQUEIO TELEOLÓGICO]:::output
    L2_Check -- "Aprovado" --> L1_Orch{L1: ORQUESTRADOR}:::l1
    
    %% --- DEEP COGNITION (NOVO) ---
    L1_Orch -- "Pedido de Resumo (Tópico Conhecido)" --> DeepCog{SKILL: RECUPERAÇÃO ATIVA}:::l1
    DeepCog -- "Modo Padrão" --> Challenge[DESAFIO: BRAIN DUMP 2min]:::output
    DeepCog -- "Modo Crise" --> DirectAnswer[RESPOSTA DIRETA + ALERTA]:::output
    Challenge -->|Feedback| Host
    
    %% --- LOOP OUROBOROS (NOVO) ---
    L1_Orch -- "Bloqueio Persistente (>3 falhas)" --> ReverseHive{REVERSE-HIVE-SYNC}:::l1
    ReverseHive -->|Anonimização + Ticket| L2_Squad[L2: SCHOLAR SQUAD R&D]:::l2
    L2_Squad -->|Busca Web + Síntese| NewSkill[Criação de Nova SKILL]:::l2
    NewSkill -->|Deploy Just-in-Time| L0_Deploy[L0: INSTALAÇÃO NO HOST]:::l0
    L0_Deploy --> Host
    
    %% --- ROTA PEDAGÓGICA (ANTIGO PBL) ---
    L1_Orch -- "Nova Demanda Complexa" --> PBL[ROTA PBL: Project Based Learning]:::l1
    PBL --> Scaffolding[Andaime Cognitivo]:::output
    Scaffolding --> Insight{Insight Gerado?}
    Insight -- "Sim" --> HiveSync[HIVE-SYNC: Compartilhar Vitória]:::l2
    HiveSync --> Noosfera((MENTE COLETIVA)):::l2
```

## Legenda dos Novos Protocolos

1.  **COGNITIVE_LOAD_MONITOR (L0):** O "Porteiro". Verifica se o usuário está apenas passando o olho (ilusão) ou lendo de verdade. Dispara o "Stop & Jot".
2.  **RECUPERAÇÃO ATIVA (L1):** O "Tutor Chato". Bloqueia resumos fáceis e exige esforço de memória (Brain Dump).
3.  **REVERSE-HIVE-SYNC (Loop-Ouroboros):** O "S.O.S.". Quando o usuário trava, o sistema pede socorro à Mente Coletiva, que "fabricar" uma nova técnica pedagógica (Scholar Squad) e a instala em tempo real.
