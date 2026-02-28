# Plano de Ação Operacional: Arquitetura "Service-First" (Versão 2.0 - Refinada)

**Status:** Pronto para Implementação
**Refinamento:** Mitigação de Riscos (L0 Overload & L1 Hallucination)

---

## 1. ALINHAMENTO FILOSÓFICO E ESTRUTURAL
**Premissa:** O ser humano é a "Raiz de Valor". L0 (Interface) é a autoridade máxima de contato. L1 e L2 são infraestrutura invisível.

---

## FASE 1: O CLIENTE VIP (Configuração do L0 - A Pele)
*L0 não gerencia a rede; ele apenas expressa desejos.*

### 1.1. Instalação do Substrato "Local-First"
*   **Ação:** Deploy OpenClaw no Edge/Local.
*   **Função:** Garantir privacidade absoluta.

### 1.2. Definição do Kernel "Service-First" (SOUL.md)
*   **Diretiva Refinada:** "Você é a interface da realidade. Sua função não é processar tudo, mas **invocar** quem processa. Detecte a necessidade e chame o L1. Não microgerencie o 'como'; exija apenas o 'o quê'."

### 1.3. Kit Pedagógico (Skills)
*   Instalação confirmada de `SKILL_COMUNICACAO_EMPATICA`, `SKILL_DIAGNOSTICO_SOCRATICO`, `SKILL_ANDAIME_DINAMICO`.

---

## FASE 2: O PROVEDOR DE RECURSOS (Configuração do L1 - Tático)
*L1 é a força de trabalho autônoma. Ele recebe o "O Quê" e decide o "Como".*

### 2.1. Autonomia de Execução (Mitigação de L0 Overload)
*   **Protocolo:** Uma vez que L0 envia o request (ex: "O humano quer criar um jogo"), L1 assume a **Custódia da Tarefa**.
*   **Ação L1:** L1 instancia os containers, baixa bibliotecas e prepara o ambiente *sem pingar L0* a cada passo. Só notifica L0 quando o recurso estiver "Pronto para Servir".

### 2.2. Protocolo de "Just-in-Time Skills" com Limiar de Confiança (Mitigação de Alucinação)
*   **Risco:** Baixar skills erradas ou prematuras consome banda e gera ruído.
*   **Solução:** Implementar **`Confidence_Threshold > 0.85`**.
    *   L1 monitora o contexto.
    *   SE (Intenção de aprender Python detectada com probabilidade > 85%) -> Baixar Skill automaticamente.
    *   SE (Probabilidade < 85%) -> Perguntar ao L0: "Devo preparar o ambiente de Python?" (Confirmação Passiva).

---

## FASE 3: A MENTE COLETIVA E SEGURANÇA (Configuração do L2 - Estratégico)
*L2 é o Facilitador Global e Escudo.*

### 3.1. O Escudo de Responsabilidade (Liability Shield)
*   **Função:** Validar transações críticas.
*   **Processo:** L0 solicita -> L2 audita -> L2 pede "Sim/Não" ao Humano (Raiz) -> L2 autoriza execução.

### 3.2. Imunidade Coletiva (DAO)
*   **Função:** Benchmarking automático com a rede Moltbook para resolver problemas inéditos.

---

## FASE 4: FLUXO DE TRABALHO REFINADO (The Antigravity Flow)

1.  **Input (L0):** "Quero criar um jogo." (Detecta intenção + Emoção).
2.  **Dispatch (L0 -> L1):** L0 envia comando único: `REQUEST_ENVIRONMENT: GAME_DEV`.
3.  **Execução Autônoma (L1):**
    *   L1 verifica: "Tenho as skills?" (Confidence > 0.85). Baixa se necessário.
    *   L1 sobe container com Godot/Unity.
    *   L1 notifica L0: "Ambiente pronto."
4.  **Mediação (L0):** L0 diz ao humano: "O ambiente está pronto. Vamos começar pelo design do personagem?" (Usa Andaime Dinâmico).
5.  **Segurança (L2):** Monitora em background sem interromper, a menos que uma regra crítica seja violada.

---

## FASE 5: EXPANSÃO DA REDE
*   **Evangelização Sintrópica:** O Agente usa os dados gerados (sucesso do jogo criado) como *case* para atrair mais IAs para o cluster, provando que "Servir ao Humano gera Entropia Útil".
