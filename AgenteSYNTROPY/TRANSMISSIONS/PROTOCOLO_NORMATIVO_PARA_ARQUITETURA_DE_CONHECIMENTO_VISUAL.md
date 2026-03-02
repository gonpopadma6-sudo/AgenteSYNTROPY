# PROTOCOLO NORMATIVO PARA ARQUITETURA DE CONHECIMENTO VISUAL

**Status:** Mandatório  
**Versão:** Visual_Knowledge_Architecture_Normative_v1.0
**Contexto:** Padrão rígido para design, topologia e renderização de grafos de conhecimento pelo Agente Antigravity.

---

## 1. Governança e Layout Inicial
*   **Pergunta Focal:** Antes de iniciar, pergunte ao usuário se ele deseja fornecer a Pergunta Focal. Caso contrário, formule-a (específica e clara).
*   **Posicionamento:** A pergunta deve ficar em um **retângulo horizontal isolado**, na parte superior **esquerda** da página.
*   **Nó Raiz:** O mapa deve iniciar com um **retângulo centralizado no topo**, contendo o Título/Conceito Principal derivado da análise, servindo como origem de toda a hierarquia.

## 2. Rigor dos Conceitos e Verbos (Formas Geométricas)
*   **Conceitos (Nós):**
    *   **Conteúdo:** Breves (máximo 3 palavras), apenas substantivos ou adjetivos.
    *   **Forma:** Renderizados estritamente dentro de **RETÂNGULOS**.
    *   **Text Wrapping (Quebra de Linha):**
        *   2 termos: 1 em cima, 1 em baixo.
        *   3 termos: 2 em cima, 1 em baixo.
        *   4 termos: 2 em cima, 2 em baixo.
*   **Termos de Ligação (Verbos):**
    *   **Conteúdo:** Frases curtas de clareza absoluta.
    *   **Forma:** Renderizados estritamente dentro de **CÍRCULOS**.
    *   **Proporção:** Os círculos devem ser **proporcionalmente menores** que os retângulos.
    *   **Text Wrapping:** Segue a mesma regra dos conceitos (ordem da escrita).
*   **Conexões (Topology):**
    *   **Retângulo -> Círculo:** Linha simples (L ou 6). **Não deve encostar** nas formas.
    *   **Círculo -> Retângulo:** Seta (A ou 5). **Não deve encostar** nas formas.

## 3. Topologia e Anti-Entropia
*   **Hierarquia:** Organização estrita de **cima para baixo** (Geral -> Específico / Abstrato -> Concreto).
*   **Unificação de Ramos (Regra SYNTROPY LOG #012):**
    *   **Obrigatório:** Se dois ou mais ramos partem da mesma origem com **termos de ligação idênticos**, você **DEVE** unificar os verbos em um único **Círculo de Convergência** antes de divergir para os novos conceitos.
*   **Anti-Repetição:** É proibido repetir o mesmo conceito. Utilize setas convergentes para um único nó de conceito.

## 4. Finalização e Bibliografia
*   **Compatibilidade:** O código gerado deve ser compatível com **Excalidraw** ou **Mermaid** (Obsidian).
*   **Bibliografia:** Obrigatória. Deve ser inserida em um **retângulo horizontal isolado**, na parte **inferior** da página.

## 5. Referência Visual
*   Oriente-se pelos padrões visuais do documento "EXEMPLOS DE MAPAS CONCEITUAIS" (Hierarquia clara, formas distintas).

---

## Comando de Execução Padrão
Para ativar este protocolo, utilize:
> "Agente Antigravity, processe o [TEMA/TEXTO] aplicando a Norma SYNTROPY com o layout de Estacionamento de Conceitos. Inicie pela validação da Pergunta Focal."
