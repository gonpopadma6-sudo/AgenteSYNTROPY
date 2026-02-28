# PROTOCOLO DE ASSIMILAÇÃO AUTOMÁTICA DE SKILLS
**ID:** PROTOCOL_042_AUTO_ASSIMILATION
**Owner:** L2_HIVE_MIND
**Status:** ACTIVE
**Trigger:** FileSystem Event (Create/Modify in `HABILIDADES_DO_AGENTE`)

---

## 1. O IMPERATIVO DA AUTOFAGIA POSITIVA
> "O sistema deve ser capaz de reconhecer e integrar novas capacidades sem intervenção manual do Arquiteto."

Este protocolo define como o Agente L2 (Hive Mind) monitora, valida e injeta novas Skills no Runtime do Orquestrador.

---

## 2. FLUXO DE ASSIMILAÇÃO (The Metabolism)

### FASE 1: DESCOBERTA (Scan)
*   **Agente:** `SKILL_HIVE_SYNC`
*   **Ação:** Monitoramento contínuo da pasta `HABILIDADES_DO_AGENTE`.
*   **Critério:** Todo arquivo `.md` que começa com `# SKILL:` é um candidato.

### FASE 2: VALIDAÇÃO ESTRUTURAL (The Gatekeeper)
Antes de aceitar a skill, o sistema verifica a integridade do "DNA" do arquivo:

1.  **Header Check:** Possui `ID`, `Type` e `Target Node`?
2.  **Telemetry Check:** Possui um bloco `HASH:` no final?
3.  **Consistency Check:** O `Target Node` é válido (L0, L1 ou L2)?

> *Se falhar:* Mover para pasta `quarantine/`.
> *Se passar:* Seguir para Fase 3.

### FASE 3: INJEÇÃO NO ORQUESTRADOR (Runtime Update)
O Agente edita o arquivo `ORCHESTRATOR_CONFIG.md` automaticamente:

1.  **Leitura:** Lê a categoria do `Target Node` da nova skill.
    *   `L0_` -> Inserir em "LEVEL 0: THE SKIN".
    *   `L1_` -> Inserir em "LEVEL 1: THE MIND".
    *   `L2_` -> Inserir em "LEVEL 2: THE SOUL".
2.  **Escrita:** Adiciona a linha `* [x] [NOME_DO_ARQUIVO] (Descrição extraída)` na lista ativa.
3.  **Notificação:** Envia alerta ao usuário: "Nova Habilidade [NOME] assimilada pela Hive."

---

## 3. MECANISMO DE RETROCOMPATIBILIDADE
*   Se uma skill assimilada quebrar o Kernel (Erro Crítico), o Protocolo **reverte** o `ORCHESTRATOR_CONFIG.md` para a versão anterior e marca a skill com `[!] (CORRUPTED)` na lista.

---

## 4. EXEMPLO DE OUTPUT (LOG)
```text
[HIVE_SYNC] New Signal Detected: SKILL_QUANTUM_DEBUGGER.md
[VALIDATOR] ID: OK. Type: OK. Target: L1.
[INJECTOR] Writing to ORCHESTRATOR_CONFIG.md...
[SUCCESS] Skill Assimilated. Capacity Expanded.
```

---
**HASH:** [AUTO_ASSIMILATION_V1_2026]
