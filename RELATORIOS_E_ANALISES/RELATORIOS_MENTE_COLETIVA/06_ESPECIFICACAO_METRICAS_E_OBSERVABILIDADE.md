# RELATÓRIO 06: ESPECIFICAÇÃO DE OBSERVABILIDADE TÉCNICA (OS 4 ARTEFATOS)

**Data:** 18 de Fevereiro de 2026
**Autor:** Agente SYNTROPY (Módulo de Arquitetura de Sistemas)
**Destinatário:** Equipe Multidisciplinar (Cientistas de Dados, Eng. de IA, DevOps)
**Escopo:** Definição dos Protocolos de Exportação de Dados para Auditoria e Prova Matemática.

Este documento especifica os requisitos técnicos para a geração dos 4 "Artefatos de Verdade" necessários para validar a eficácia do Sistema de Sinergia.

---

## 1. O "FLIGHT RECORDER" (REGISTRO DE VOO / TELEMETRIA)
**Público:** Matemáticos e Cientistas de Dados.
**Objetivo:** Provar a estabilidade matemática (Sintropia vs. Entropia).

### 1.1. Estrutura de Exportação (CSV/Time-Series)
O sistema deve gerar um log contínuo (`telemetry.csv`) com a seguinte granularidade, agora incluindo **Métricas PID**:

| Timestamp (ISO8601) | World_StateV (Volatilidade) | PID_Output (u) | Error_Rate (e) | Integral_Term (I) | Derivative_Term (D) | Action_Taken |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-02-18T09:00:01Z | 0.82 (High Stress) | 0.75 (High) | 0.4 (Stress) | 0.2 (Accumulated) | 0.15 (Rising) | ACT_SAMALIN_CALM |
| 2026-02-18T09:00:05Z | 0.40 (Med Stress) | 0.30 (Low) | 0.1 (Flow) | 0.2 (Stable) | -0.05 (Falling) | ACT_PBL_SCAFFOLD |

### 1.2. Definições de Campos
*   **Snapshot do Ambiente:** Vetor de estado $S_t$ (ex: Carga Cognitiva, Erros de Compilação).
*   **PID Output ($u_t$):** Força da intervenção calculada por $K_p e(t) + K_i \int e + K_d \frac{de}{dt}$.
*   **Métrica de Convergência:** $\lim_{t\to\infty} E(t) = 0$. Deve provar que o erro $E$ diminui com o tempo.

---

## 2. RELATÓRIO DE "EXPLAINABILITY" (TRACE DE DECISÃO)
**Público:** Engenheiros de IA e Especialistas.
**Objetivo:** Eliminar a "Caixa Preta".

### 2.1. Estrutura de Log Estruturado (JSON)
Cada decisão crítica gera um objeto JSON em `decision_trace.json`:

```json
{
  "interaction_id": "uuid-v4",
  "trigger": "USER_FRUSTRATION_DETECTED",
  "context_window_snapshot": [
    "User: 'Eu odeio isso, nada funciona!'",
    "System_State: 'Error count > 5'"
  ],
  "reasoning_chain": [
    "Step 1: Detected negative sentiment (Score -0.9).",
    "Step 2: Checked Heartbeat limits. Panic mode active.",
    "Step 3: Selected Strategy 'SAMALIN' over 'DEBUGGING'."
  ],
  "decision_weights": {
    "technical_solution_weight": 0.2,
    "emotional_support_weight": 0.8
  },
  "confidence_score": 0.98,
  "final_action": "EXECUTE_AFFECTIVE_MIRROR"
}
```

---

## 3. RELATÓRIO DE LATÊNCIA E REATIVIDADE (STRESS TEST)
**Público:** Arquitetos e DevOps.
**Objetivo:** Garantir a física da "Antigravidade" (Velocidade de Reação).

### 3.1. Métricas de Performance (APM)
O sistema deve exportar métricas compatíveis com Prometheus/Grafana:

*   **Tick-to-Action (TTA):** Tempo entre `Event_Detected` e `Action_Executed`.
    *   *Alvo:* < 200ms para L0 (Edge); < 2s para L1 (Server).
*   **Resource Consumption:**
    *   CPU Usage vs. Token Output Rate.
    *   Memory Leak Check (Estabilidade pós-24h de operação).
*   **Failure Rate:**
    *   `Execution_Blocked_Count`: Quantas vezes o Agente tentou agir mas falhou (API Timeout, Permission Denied).

---

## 4. RELATÓRIO DE CENÁRIOS DE BORDA (CHAOS & PANICS - BFT ADDITION)
**Público:** Auditores de Segurança e Matemáticos.
**Objetivo:** Validar robustez em condições extremas (Invariantes).

### 4.1. Logs de Pânico (`panic.log`)
Registro de comportamentos quando as entradas violam a realidade esperada:

*   **Input Nulo/Infinito:** Usuário envia caracteres randômicos ou arquivos de 10GB.
    *   *Comportamento Esperado:* Graceful Degradation (Não crashar, rejeitar elegantemente).
*   **Violação de Invariantes Bizantinas (Nova Regra):**
    *   *Cenário:* Um nó L2 tenta validar um Insight sem prova ZK válida ou com assinatura forjada.
    *   *Ação:* **BFT_SLASHER_TRIGGERED**. O nó traidor é isolado e seus tokens de reputação queimados.
    *   *Alerta:* "CRITICAL_CONSENSUS_VIOLATION". Rejeição imediata da proposta.
*   **Violação de Soberania de Dados:**
    *   *Cenário:* Agente tenta enviar PII não-anonimizado.
    *   *Alerta:* **PRIVACY_FIREWALL_BLOCK**. Ação bloqueada na saída do L1.
*   **Violação de Invariantes:**
    *   *Regra Sagrada:* "Nunca apagar dados do usuário sem backup."
    *   *Alerta:* Se o Agente tentar executar `rm -rf`, o sistema deve logar **CRITICAL_INVARIANT_VIOLATION** e travar a ação.

### 4.2. Exemplo de Log de Borda
```log
[WARN] 2026-02-18 09:15:00 - INVARIANT THREAT DETECTED
Target: SYSTEM_CORE/SOUL.md
Action: WRITE_OVERRIDE
Actor: L1_Tactical_Agent
Reason: "Optimization"
INTERVENTION: KERNEL_LOCK triggered. Action blocked. Immutability preserved.
```

---

## 5. SOLICITAÇÃO DE IMPLEMENTAÇÃO (RFC)

Para a Equipe de Desenvolvimento:

1.  **Instrumentação:** Adicionar bibliotecas de telemetria (ex: OpenTelemetry) no Kernel do Agente.
2.  **Exportadores:** Configurar endpoints ou *log rotation* para salvar os arquivos `.csv`, `.json` e `.log` na pasta `SYSTEM_LOGS/`.
3.  **Visualização:** Criar dashboards padrão (Grafana/Streamlit) que leiam esses arquivos e plotem os gráficos de Convergência e Latência.

Sem esses dados, o Agente SYNTROPY é apenas uma promessa teórica. Com eles, torna-se um sistema científico provável.
