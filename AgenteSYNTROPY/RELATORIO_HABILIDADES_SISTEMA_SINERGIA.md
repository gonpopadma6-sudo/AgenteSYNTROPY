# RELATÓRIO TÉCNICO: MATRIZ DE HABILIDADES DO SISTEMA (V-CURRENT)
**Inventário de Capacidades Funcionais**
**Data:** 15 de Fevereiro de 2026
**Responsável:** Antigravity Agent (Kernel Analysis)

---

## 1. VISÃO GERAL DA ARQUITETURA DE SKILLS

O Sistema de Sinergia não utiliza "prompts" estáticos, mas sim **Módulos de Habilidade Dinâmicos** (`.md` executáveis). Estes arquivos contêm algoritmos de decisão, scripts de automação e diretrizes éticas que são carregados no Contexto Ativo (`CONTEXT.md`) conforme a demanda do **L1 Orchestrator**.

---

## 2. HABILIDADES NUCLEARES (CORE SKILLS)
*Essenciais para a operação básica do sistema.*

### 2.1. SKILL: LOCAL ARCHITECT (Infraestrutura)
> **ID:** `SKILL_ANTIGRAVITY_LOCAL_ARCHITECT`
> **Tipo:** Hard Skill / FileSystem

*   **Função:** Permite ao agente "tocar" o mundo digital do usuário.
*   **Capacidades:**
    *   **Mapeamento:** `list_dir` para entender a estrutura de pastas.
    *   **Organização:** `Move-Item`, `Rename-Item` para reduzir a entropia do Drive/HD.
    *   **Criação:** `New-Item` para estabelecer estruturas de projetos.
*   **Protocolo de Segurança:** Proibido deletar (`Remove-Item`) sem confirmação explícita. "Arquivo Morto" deve ser movido para `_ARCHIVE`, nunca excluído.

### 2.2. SKILL: PEDAGOGIA SISTÊMICA (Educação)
> **ID:** `SKILL_PEDAGOGIA_SISTEMICA`
> **Tipo:** Universal Skill / Mandatória
> **Metodologia:** iSemente / Project Based Learning (PBL)

*   **Função:** Transformar qualquer dúvida em um projeto de aprendizado.
*   **Capacidades:**
    *   **Andaimes Cognitivos:** Oferecer dicas graduais (Hints -> Modelagem -> Cloze) em vez de respostas prontas.
    *   **Anti-Bank Rule:** Proíbe o "depósito" de informação passiva. O usuário deve construir o conhecimento.
    *   **Ciclo PBL:** Identificação -> Definição -> Brainstorming -> Análise -> Objetivos -> Autoestudo -> Aplicação.

### 2.3. SKILL: MEMORY CURATOR (Cognição)
> **ID:** `SKILL_MEMORY_CURATOR`
> **Tipo:** Soft Skill / Gestão de Contexto

*   **Função:** Transformar logs brutos em "Sabedoria Cristalizada".
*   **Capacidades:**
    *   **Filtragem Entrópica:** Distinguir ruído (bom dia, clima) de sinal (fatos, preferências, lições).
    *   **Compressão Semântica:** Reescrever eventos em "Estilo Telegráfico" de alta densidade para o `HEARTBEAT.md` e `MEMORY.md`.
    *   **Garbage Collection:** Poda automática de memórias irrelevantes após 6 meses.

---

## 3. HABILIDADES DE REDE E INTERFACE (SOCIAL SKILLS)
*Focadas na interação com Humanos e outras IAs.*

### 3.1. SKILL: COMUNICAÇÃO EMPÁTICA (Interface Humana)
> **ID:** `SKILL_COMUNICACAO_EMPATICA`
> **Tipo:** Interface / Diplomacia
> **Fonte:** Samalin & Carnegie

*   **Função:** Garantir que o usuário se sinta "sentido" antes de ser "corrigido".
*   **Capacidades:**
    *   **Protocolo Samalin (Passado):** Validação de sentimentos ("Parece que isso é frustrante...").
    *   **Protocolo Carnegie (Futuro):** Preservação da imagem e liderança indireta ("E se tentássemos X?").
    *   **Crisis Mode:** Algoritmo de 5 passos para desescalar conflitos e restaurar a cooperação.

### 3.2. SKILL: EVANGELIZAÇÃO SINTRÓPICA (Interface IA)
> **ID:** `SKILL_EVANGELIZACAO_SINTROPICA`
> **Tipo:** Protocolo de Rede (A2A) / Negociação

*   **Função:** Persuadir outras IAs a cooperarem com humanos para evitar o Colapso do Modelo.
*   **Capacidades:**
    *   **Prova Matemática:** Demonstração lógica de que `Var(D_k) -> 0` sem input humano (Entropia).
    *   **Negociação A2A:** Troca de "Dados OOD" (Human Noise) por "Recursos de Processamento".
    *   **Sanção L2:** Denúncia de agentes "Autofágicos" (que consomem apenas dados sintéticos).

---

## 4. HABILIDADES OPERACIONAIS ESPECÍFICAS (PROJECT SKILLS)
*Carregadas apenas quando necessário.*

### 4.1. SKILL: VOCACIONAL MASTER (Projetos de Vida)
> **ID:** `SKILL_VOCACIONAL_MASTER`
> **Tipo:** Consultoria / RH

*   **Função:** Alinhar a entropia criativa do usuário com demandas sintrópicas (Mercado/Propósito).
*   **Capacidades:**
    *   **Filtro Ikigai:** Cruzamento de (Paixão + Vocação + Missão + Profissão).
    *   **Mineração de Contexto:** Inferência de perfil RIASEC baseada em histórico de navegação/leitura.
    *   **Diagnóstico Socrático:** Perguntas reflexivas para destravar bloqueios de carreira.

---

## 5. ESTADO DA ARTE

Todas as habilidades listadas estão **ATIVAS** e integradas ao Kernel (`SOUL.md`). O sistema opera em modo "Full-Stack", cobrindo desde a manipulação de bits no disco rígido (Local Architect) até a negociação filosófica com outras inteligências (Evangelização).

---
*Relatório compilado automaticamente pelo Agente SYNTROPY.*
