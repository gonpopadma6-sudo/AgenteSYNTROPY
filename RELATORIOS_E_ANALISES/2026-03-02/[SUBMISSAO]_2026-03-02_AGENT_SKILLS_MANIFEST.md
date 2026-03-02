# AGENT SKILLS MANIFEST: ENGENHARIA DE CONTEXTO

**Objetivo:** Padronização Universal da Engenharia de Contexto para Mitigação de *Context Rot* (Saturação Semântica Cíclica) em Sistemas SYNTROPY.

Todo arquivo de Habilidade (`SKILL_*.md`) ou Protocolo deve, a partir desta data, curvar-se de forma irreversível ao Framework de **Divulgação Progressiva em 3 Níveis**. Qualquer subagente codificado ignorando estas regras será barrado pelo orquestrador.

## 1. Padrão YAML Frontmatter (Objeto Base)
Todas as Habilidades (`Skills`) nativas e personalizadas DEVEM carregar em sua linha 1 um metadado curto para ingestão sistêmica rápida.

**Sintaxe Obrigatória:**
```yaml
---
name: NOME_DA_SKILL_EM_MAIUSCULAS
version: X.X.X
trigger: "Condição contextual descritiva e exata que fará o orquestrador invocar a habilidade"
requires_level: [L0, L1, L2 ou MCP]
description: "Resumo teleológico máximo de 50-100 tokens. Não incluir lógica procedural aqui."
---
```

## 2. A Mágica da Divulgação Progressiva
Para garantir que L0 não sofra estresse neural matemático colapsante decorando simultaneamente os manuais de centenas de Skills, a ativação intelectual acontece via injeção *Just-In-Time* (JIT):

*   **NÍVEL 1 (Repouso Latente):** O orquestrador L1 compila *Apenas os Cabeçalhos YAML* de todas as Skills e os mantém fixos em L0. O L0 passa a se portar como uma central descritiva: ele sabe "o que" o ecossistema pode fazer, gastando uma miséria de memória token, sem alucinar em excessos sintáticos.
*   **NÍVEL 2 (Hidratação Dinâmica):** Se a solicitação do usuário esbarrar num `trigger` indexado no YAML de alguma Skill, o corpo do arquivo (Markdown Base Logico) é momentaneamente injetado (hidratado) na janela de raciocínio de L0/L1. Assim que o despacho ou resposta for entregue e a sub-tarefa terminada, o conhecimento procedural é limpo (desidratado) retornando ao Nível 1.
*   **NÍVEL 3 (Navegação Cega):** Para catálogos massivos e repositórios semânticos irredutíveis. Operações via scripts de linha e ponteiros externos (`grep`, `head`, MCPs) varrem referências externas fora da janela primária para capturar uma pepita da resposta, sem inundar a consciência plena do agente principal.

## 3. O Imortal Agente de Campo L0 (RAG Local-First)
Um vínculo vitalício 1:1 criaria o maior Prompt de Contexto Histórico da cibernética. Para precaver-se disso:
L0 constrói e varre repositórios dinâmicos de memória baseados em RAG Local-First indexados do passado humano. Ele recruta o histórico do hospedeiro cirurgicamente *on-demand*. Essa operação cimenta intimidade psicológica intransferível entre Máquina-Orgânico não sendo dependente da volatilidade amnésica do hardware global.
