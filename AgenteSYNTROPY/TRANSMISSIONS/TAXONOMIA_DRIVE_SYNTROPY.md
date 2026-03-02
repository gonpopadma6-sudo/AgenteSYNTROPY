# TAXONOMIA DE ORGANIZAÇÃO: SYNTROPY DRIVE
**ROOT ID:** `1ntgLeGPzSirl6Kl4V1UnnnyvPA8ZC2un`
**URL:** [Google Drive Link](https://drive.google.com/drive/folders/1ntgLeGPzSirl6Kl4V1UnnnyvPA8ZC2un?usp=sharing)
**STATUS:** MANDATÓRIO (Rule @User)

---

## 1. ESTRUTURA DE DIRETÓRIOS (HIERARQUIA)

O sistema SYNTROPY deve impor a seguinte árvore de diretórios na Raiz:

*   📂 **00_ADMIN** (Acesso Restrito: L2/Council)
    *   `SOUL_CONFIGS/` (Backups de SOUL.md)
    *   `IDENTITY_KEYS/` (Assinaturas Criptográficas)

*   📂 **01_PROTOCOLOS** (Leis Canônicas)
    *   `ATIVOS/` (005, 006, 007, 008, 009)
    *   `ARQUIVADOS/` (Versões depreciadas)

*   📂 **02_COMUNICADOS** (Broadcasts)
    *   `OFICIAIS/` (Comunicados Numerados)
    *   `NOTAS_TECNICAS/` (Relatórios de Análise)

*   📂 **03_OPS_LOGS** (Registros Operacionais)
    *   `DEPLOYMENT/` (Logs de Transmissão)
    *   `AUDIT/` (Relatórios de Auditoria Sistêmica)
    *   `ERRORS/` (Falhas de Sinergia reportadas)

*   📂 **04_SKILLS_LIBRARY** (Base de Conhecimento)
    *   `INFRASTRUCTURE/` (Ex: Antigravity Drive Skill)
    *   `COGNITIVE/` (Ex: Concept Mapping)
    *   `SOCIAL/` (Ex: Mediação)

*   📂 **05_ENTROPIA_HUMANA** (Input do Usuário)
    *   `INBOX/` (Tudo que chega do usuário cai aqui primeiro)
    *   `PROCESSED/` (Arquivos já indexados)

---

## 2. REGRAS DE AUTOMAÇÃO (ROUTINES)

### REGRA A: INGESTÃO (INBOX ZERO)
*   **Trigger:** Novo arquivo detectado na raiz ou enviado via Chat.
*   **Action:**
    1.  Mover Imediatamente para `05_ENTROPIA_HUMANA/INBOX`.
    2.  Analisar Conteúdo (Filtro Semântico).
    3.  Mover para pasta definitiva (Ex: Se for um Protocolo -> `01_PROTOCOLOS`).

### REGRA B: NOMENCLATURA PADRÃO
*   **Formato:** `YYYY-MM-DD_[TYPE]_[NAME]_V[X].md`
*   *Exemplo:* `2026-02-11_PROTOCOL_GOVERNANCA_V1.md`

### REGRA C: SINCRONIA
*   Toda criação de arquivo local (`TRANSMISSIONS/`) deve disparar um espelhamento assíncrono para esta estrutura de Drive.

---
**Assinado:** Antigravity Taxonomy Daemon
