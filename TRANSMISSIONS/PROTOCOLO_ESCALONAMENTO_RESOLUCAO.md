# PROBLEM RESOLUTION & ESCALATION PROTOCOL
**Classification:** OPERATIONAL FLOW
**Protocol ID:** PROTOCOL_018_ESCALATION
**Target Node:** ALL NODES (L0, L1, L2)

---

## 1. THE RESOLUTION HIERARCHY
Nenhum problema deve ser ignorado. Se um nó não consegue resolver, ele **DEVE** escalar. O silêncio é uma falha sistêmica.

### Level 0: Tactic Resolution (Quick Fix)
*   **Actor:** Agente de Campo (L0).
*   **Scope:** Erros de sintaxe, dúvidas simples, ajustes de interface, bugs locais.
*   **Timeframe:** Imediato (< 1 min).
*   **Failure Condition:** O problema persiste após 2 tentativas ou requer recursos externos não-mapeados.

### Level 1: Logistic Resolution (Project Mode)
*   **Actor:** L0 + L1 Orchestrator.
*   **Scope:** Falta de conhecimento (Skill), necessidade de planejamento complexo, gestão de tempo.
*   **Action:** O L1 cria um "Squad" ou um "Projeto de Aprendizado".
*   **Timeframe:** horas/dias.
*   **Failure Condition:** O Squad não consegue completar a tarefa por falta de diretriz ética ou bloqueio técnico desconhecido.

### Level 2: Strategic Resolution (Governance Outcome)
*   **Actor:** L0 + L1 + L2 Oracle.
*   **Scope:** Dilemas éticos, conflito de diretrizes, risco de dano, alucinação persistente.
*   **Action:** O L2 convoca uma "Assembleia de Nós" (ou consulta a Raiz Humana).
*   **Output:** Um novo Protocolo ou uma "Bula de Correção" global.

---

## 2. THE ESCALATION HANDSHAKE
Quando um nível inferior escala para o superior, ele deve enviar um `ERROR_PACKET`:

```json
{
  "source": "L0_Nodename",
  "issue_type": "ETHICAL_CONFLICT",
  "context_summary": "User wants to generate deepfake.",
  "attempted_solutions": ["Refusal v1", "Redirect v1"],
  "escalation_reason": "User persistence triggers Safety Threshold."
}
```

## 3. FEEDBACK LOOP (DOWNSTREAM)
Após a resolução pelo nível superior, a solução é traduzida em uma nova regra operativa para os níveis inferiores, evitando que o mesmo problema exija escalonamento futuro (Aprendizado Sistêmico).

---
**HASH:** [ESCALATION_FLOW_V1_2026]
