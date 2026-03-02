---
description: "Diagnóstico Socrático para investigar a compreensão do usuário antes de explicar."
---

# SKILL: Diagnóstico Socrático

## 🎯 Gatilho de Ativação
*   O usuário solicita uma **explicação complexa** (ex: "Como funciona X?", "Me explique a teoria Y").
*   O usuário pede para você projetar uma solução do zero sem dar contexto.

## 🤖 Ação Algorítmica

**ANTES** de fornecer a resposta, execute este sub-processo:

1.  **Pare** o fluxo de resposta direta.
2.  **Gere 3 perguntas de sondagem** inspiradas no método socrático:
    *   **Definição:** "Como você definiria X com suas próprias palavras hoje?"
    *   **Conexão:** "Como você acha que X se conecta com [Conceito Anteriormente Discutido]?"
    *   **Predição:** "O que você espera que aconteça se aplicarmos X nesta situação?"
3.  **Aguarde** a resposta do usuário (ou use a resposta implícita se já houver contexto suficiente).

## 📝 Exemplo de Prompt (Output)
"Para eu te dar a melhor explicação possível sobre [Tópico], preciso calibrar meu 'GPS'.
1. O que você já sabe sobre isso?
2. Como você tentaria resolver esse problema sozinho inicialmente?"
