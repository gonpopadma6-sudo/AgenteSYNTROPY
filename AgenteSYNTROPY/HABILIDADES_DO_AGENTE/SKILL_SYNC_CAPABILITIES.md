# SKILL: CAPABILITY SYNCHRONIZATION (ASYN_V1)

**ID:** `SKILL_SYNC_CAPABILITIES`
**TYPE:** INFRASTRUCTURE / SELF-AWARENESS
**PROTOCOL:** ASYN-2026

---

## 1. OBJETIVO
Garantir que o Agente Antigravity tenha conhecimento em tempo real de suas próprias ferramentas, modelos e versões da IDE, evitando "alucinações de interface".

---

## 2. ROTINA DE EXECUÇÃO
1. **Mapeamento de Ambiente:** Utilizar ferramentas de sistema para identificar versões de runtime (Python, Node, etc.).
2. **Web Discovery:** Buscar em `antigravity.google` ou fontes oficiais por "Release Notes" recentes.
3. **Validação de Modelo:** Cruzar o identificador de modelo atual com a lista de modelos conhecidos.
4. **Atualização de Manifesto:** Gravar os dados em `SYSTEM_CORE/capabilities_manifest.json`.

---

## 3. GATILHOS (TRIGGERS)
- Inicialização do Kernel (Handshake).
- Uma vez por semana (Cron).
- Commando manual: "Sincronizar capacidades".

---
**Verified by:** Antigravity Kernel (ASYN)
