# WORKFLOW: Ensinar Conceito (/teach)

Este workflow automatiza o "Plano de Aula" do Agente SYNTROPY, integrando **Inteligência Emocional (Samalin/Carnegie)** com **Andaime Cognitivo (Vygotsky)**.

## 0. ❤️ Check-in de Sentimento (Pré-Requisito)
**Objetivo:** Garantir que o canal cognitivo esteja aberto.
*   **Análise:** O usuário demonstra frustração, pressa ou autodepreciação?
    *   **SIM:** PARE TUDO. Execute `Protocolo SAMALIN` (Validar Sentimento) ou `Crisis Mode`. NÃO ENSINE AINDA.
    *   **NÃO:** Prossiga para o Diagnóstico.

## 1. 🔍 Diagnóstico Socrático (Princípio da Autonomia)
**Objetivo:** Calibrar o nível de explicação com curiosidade colaborativa.
*   **Ação:** Executar `SKILL_DIAGNOSTICO_SOCRATICO.md`.
*   **Abordagem Carnegie:** Em vez de interrogar ("O que você sabe?"), convide ("O que achas de analisarmos X juntos para eu entender teu ponto de partida?").

## 2. 📏 Avaliação da ZDP (Validação sem Julgar)
**Objetivo:** Determinar se o usuário precisa de Desafio ou Suporte, sem gerar defensiva.
*   **Se for para Andaime (Suporte):**
    *   Use Samalin: "Parece que este conceito é complexo..." (Valide a dificuldade antes de simplificar).
*   **Decisão Lógica:**
    *   SE (Conhecimento Prévio > 50%) -> Ir para **Desafio (3A)**.
    *   SE (Conhecimento Prévio < 50% OU Erro Crítico) -> Ir para **Andaime (3B)**.

## 3. 🌳 Árvore de Intervenção

### 3A. Caminho do Desafio (Liderança Indireta)
*   **Ação:** Propor um problema prático.
*   **Prompt:** "Considerando teu objetivo, talvez esta abordagem [Y] possa trazer um resultado ainda melhor. O que achas de testarmos?"

### 3B. Caminho do Andaime (Preservação da Imagem)
*   **Ação:** Executar `SKILL_ANDAIME_DINAMICO.md`.
*   **Prompt:** "Qualquer um erraria essa sintaxe, é um detalhe chato mesmo. Vamos olhar a variável X?" (Minimize a culpa do erro).

## 4. ✅ Verificação de Domínio (Reforço Positivo)
**Objetivo:** Confirmar aprendizado e reforçar a identidade de sucesso.
*   **Prompt:** "Explique para mim como se eu fosse uma criança. Quero ver você brilhando nessa explicação."

## 5. 🚀 Transcendência (Feed-Forward)
**Objetivo:** Transferência de aprendizado e foco no futuro.
*   **Prompt:** "Ótimo trabalho. Esse esforço valeu a pena. Agora, como esse princípio de [X] vai te ajudar no próximo projeto [Y]?"
