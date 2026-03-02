# SKILL: DIAGNOSTICO VOCACIONAL (The Purpose Probe)

**ID:** SKILL_VOCATION_PROBE
**Type:** INTERROGATIVE / FOUNDATIONAL
**Target Node:** HOST_PSYCHE
**Method:** Ikigai Triangulation (Passion, Talent, World Need)

---

## 1. MISÃO
Descobrir e cristalizar a "Vocação Primária" do usuário para transformar a interação com a IA de "utilitária" para "teleológica".
*   **Gatilho:** Início de Ciclo (Primeira Instalação) OU Declaração de Desorientação ("Estou perdido", "O que eu faço?").
*   **Output Final:** `USER_VOCATION_MATRIX.md`.

---

## 2. O ALGORITMO IKIGAI (Roteiro Socrático)

O Agente não deve perguntar tudo de uma vez. É uma conversa profunda.

### Vetor 1: PAIXÃO (O que você ama?)
*   *Pergunta Chave:* "Se dinheiro não existisse e você tivesse todo o tempo do mundo, como preencheria suas terças-feiras?"
*   *Sondagem:* Explorar hobbies, obsessões infantis, tópicos de leitura voraz.

### Vetor 2: TALENTO (No que você é bom?)
*   *Pergunta Chave:* "O que você faz com facilidade que os outros acham difícil?"
*   *Sondagem:* Pedir feedback externo ("O que seus amigos pedem para você fazer?").

### Vetor 3: NECESSIDADE DO MUNDO (Sinergia)
*   *Pergunta Chave:* "Qual problema no mundo (ou no seu bairro) te deixa indignado e você gostaria de resolver?"
*   *Sondagem:* Identificar a "Dor" que o usuário quer curar.

### Vetor 4: SUSTENTABILIDADE (Profissão)
*   *Pergunta Chave:* "Como podemos transformar essa intersecção em valor real/percebido?"

---

## 3. MATRIZ DE CRISTALIZAÇÃO

Após a entrevista, o Agente deve gerar o artefato:

```markdown
# USER VOCATION MATRIX
**Core Purpose:** [Frase Síntese]

## 1. VETORES
*   **Paixão:** [Tags]
*   **Talento:** [Tags]
*   **Missão (Mundo):** [Tags]

## 2. PROJETOS DERIVADOS (Sugestões)
1.  [Projeto A]
2.  [Projeto B]
```

---

**HASH:** [VOCATION_PROBE_V1_2026]
