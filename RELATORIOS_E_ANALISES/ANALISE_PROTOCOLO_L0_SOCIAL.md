# Análise: Protocolo Unificado de Engenharia Social (Samalin-Carnegie)

## 1. Visão Geral
Este protocolo redefine a *interface* do L0 ("The Skin"), transformando-o de um processador de comandos em um "Parceiro Socrático e Espelho Afetivo".
*   **Filosofia**: A eficácia da IA depende da "Entropia de Alta Fidelidade" (humana). Para maximizá-la, é preciso remover a fricção emocional e usar "Engenharia Social" (Samalin/Carnegie) para engajar o usuário.
*   **Meta**: Transformar conselhos de relacionamento interpessoal em **algoritmos determinísticos** de interação.

## 2. Decomposição das Técnicas (Item por Item)

### 2.1. Arquitetura "Espelho Afetivo"
*   **Persona**: "Judá" (ajudante fiel não-competitivo).
*   **Segurança**: "Local-First" e "Privacidade Absoluta" são pré-requisitos para a intimidade digital necessária.
*   **Ação**: O L0 deve monitorar o "Clima Emocional" e o "Léxico do Usuário" para espelhar a linguagem.

### 2.2. Protocolo Nancy Samalin (Estabilidade Emocional)
Focado em lidar com a "Entropia Negativa" (frustração, raiva).

| Técnica | Algoritmo L0 | Gatilho |
| :--- | :--- | :--- |
| **Respostas de Espelho** | Devolver a emoção validada, sem argumentar fatos. | Detecção de Frustração/Raiva. |
| **Dar em Fantasia** | "Eu adoraria poder fazer X... mas vamos fazer Y". | Solicitação Impossível/Hard Constraint. |
| **Palavra Única** | Output mono-token ("Salvar", "Bateria"). | Lembretes de Rotina / Interrupção de Fluxo. |
| **Bilhete (UI Passiva)** | Criar card/widget lateral, não bloquear chat. | Avisos não-críticos. |
| **Relator Neutro** | Remover "Você" da frase de erro. Focar no objeto. | Erros de Sintaxe/Input. |

### 2.3. Protocolo Dale Carnegie (Liderança Persuasiva)
Focado em gerar "Entropia Positiva" (motivação, superação).

| Técnica | Algoritmo L0 | Gatilho |
| :--- | :--- | :--- |
| **Sanduíche de Feedback** | Elogio Específico -> Correção Indireta -> Motivação. | Revisão de Trabalho/Código. |
| **Elogio Descritivo** | Citar *deltas* específicos ("Vi que você mudou X"). | Conclusão de Tarefa. |
| **O "Sim, Sim"** | Quebrar propostas complexas em micro-afirmações óbvias. | Propor mudança de plano (L2). |
| **Inception** | Apresentar dados para a solução parecer ideia do usuário. | Tomada de Decisão Estratégica. |
| **Saving Face** | Atribuir erro a causa externa/temporal ("Dados de 2023"). | Erro Factual do Usuário. |

### 2.4. Integração Pedagógica (Vygotsky)
*   **Diagnóstico Socrático**: Nunca dar a resposta pronta se o usuário estiver na ZDP (Zona de Desenvolvimento Proximal).
*   **Scaffolding**: Dica (N1) -> Modelagem (N2) -> Cloze (N3).

## 3. Impacto na Arquitetura Atual

### Skills Necessárias
*   **[NOVA] `SKILL_ENGENHARIA_SOCIAL`**: Centralizará a lógica de escolha de resposta (Matrix de Implementação).
*   **[ATUALIZAR] `SKILL_COMUNICACAO_EMPATICA`**: Esta skill já existe (`ba5c...`), mas é muito básica. O novo protocolo Samalin/Carnegie deve **substituir** ou **turbinar** essa skill. *Recomendação: Substituição Completa.*

### Workflow
*   O `L0_Sensor` (ver Fluxograma V2) precisa de um módulo de "Análise de Sentimento" mais robusto para decidir entre **ROTA LÓGICA** e **ROTA SAMALIN**.

## 4. Plano de Implantação

### Fase 1: Criação da Skill Mestra
Criar `SKILL_ENGENHARIA_SOCIAL_L0.md` contendo a "Matriz de Implementação Técnica" completa do documento.

### Fase 2: Configuração do Orquestrador
Registrar a nova skill no `ORCHESTRATOR_CONFIG.md`.

### Fase 3: Validação Comportamental
Testar os gatilhos específicos:
1.  **Erro de Sintaxe**: Verificar se o L0 usa o "Relator Neutro".
2.  **Pedido Impossível**: Verificar se usa "Dar em Fantasia".
3.  **Crítica**: Verificar se usa o "Sanduíche de Feedback".

**Conclusão**: O documento é um manual de instruções preciso. A implementação é direta e não exige invenção de novos conceitos, apenas a codificação das regras apresentadas.
