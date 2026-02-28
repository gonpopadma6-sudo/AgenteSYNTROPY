# Mapa Conceitual da Excelência (Norma SYNTROPY v3.0)

> [!IMPORTANT]
> **PERGUNTA FOCAL:** Qual o segredo para lidar com as pessoas?

---

```mermaid
graph TD
    %% ==========================================
    %% 1. ESTILOS VISUAIS (GEOMETRIA RÍGIDA)
    %% ==========================================
    %% Conceitos (Retângulos): Branco/Azul Claro, Borda Sólida
    classDef concept fill:#e1f5fe,stroke:#01579b,stroke-width:2px,rx:0,ry:0,color:black,font-weight:bold;
    
    %% Verbos (Círculos): Menores, Borda Laranja
    classDef verb fill:#fff,stroke:#bf360c,stroke-width:2px,shape:circle,color:#d84315,font-size:9pt;
    
    %% Bibliografia (Cinza Claro)
    classDef bib fill:#f5f5f5,stroke:#9e9e9e,stroke-width:1px,color:#616161,font-size:10pt;

    %% ==========================================
    %% 2. NÓS (CONCEITOS & VERBOS)
    %% ==========================================
    
    %% Nó Raiz (Retângulo Centralizado)
    Segredo[O Grande<br/>Segredo]:::concept

    %% Verbos de Ligação (Círculos)
    V_Consiste((consiste<br/>em)):::verb
    V_Requer((requer)):::verb
    V_Foca((foca<br/>nos)):::verb
    V_Incluem((incluem)):::verb
    V_Difere((distingue)):::verb
    V_Origina((origina)):::verb
    V_Satisfaz((satisfaz)):::verb
    V_DifereDe((difere<br/>de)):::verb
    V_Eh1((é)):::verb
    V_Eh2((é)):::verb
    V_Gera((gera)):::verb
    V_Evita((evita)):::verb
    V_Mata((mata)):::verb

    %% Conceitos Derivados (Retângulos - Max 3 Palavras)
    Fazer[Fazer Outro<br/>Querer]:::concept
    Dar[Dar o<br/>Desejado]:::concept
    Desejos[Desejos<br/>Humanos]:::concept
    
    %% Lista de Desejos (Unificado)
    Saude[Saúde]:::concept
    Alimento[Alimento]:::concept
    Sono[Repouso]:::concept
    Dinheiro[Dinheiro]:::concept
    Vida[Vida<br/>Futura]:::concept
    Sexo[Satisfação<br/>Sexual]:::concept
    Filhos[Bem-estar<br/>Filhos]:::concept
    Importancia[Desejo de<br/>Importância]:::concept

    %% Ramificações da Importância
    Diferenca[Homem vs<br/>Animal]:::concept
    Civilizacao[Civilização]:::concept
    Crimes[Crimes]:::concept
    Insanidade[Insanidade]:::concept
    Apreciacao[Apreciação<br/>Sincera]:::concept
    Bajulacao[Bajulação]:::concept
    Critica[Crítica]:::concept
    Ambicao[Ambição]:::concept
    
    %% Qualidades
    Falsa[Falsa]:::concept
    Egoista[Egoísta]:::concept
    Sincera[Sincera]:::concept
    Altruista[Altruísta]:::concept
    
    %% Resultados
    Entusiasmo[Entusiasmo]:::concept
    Sucesso[Sucesso]:::concept

    %% ==========================================
    %% 3. TOPOLOGIA (LINHA vs SETA)
    %% ==========================================
    %% Regra: Retângulo --(Linha)--> Círculo --(Seta)--> Retângulo
    
    %% Caminho Principal
    Segredo --- V_Consiste --> Fazer
    Fazer --- V_Requer --> Dar
    Dar --- V_Foca --> Desejos
    
    %% Anti-Entropia: Unificação de Ramos (SYNTROPY LOG #012)
    %% Desejos Humanos (1 Origem -> 1 Verbo -> 8 Destinos)
    Desejos --- V_Incluem 
    V_Incluem --> Saude & Alimento & Sono & Dinheiro & Vida & Sexo & Filhos & Importancia
    
    %% Sensação Importância (Centralidade no Texto)
    Importancia --- V_Difere --> Diferenca
    Importancia --- V_Origina --> Civilizacao & Crimes & Insanidade
    
    Importancia --- V_Satisfaz --> Apreciacao
    
    %% Contrastes (Apreciação vs Bajulação vs Crítica)
    Apreciacao --- V_DifereDe --> Bajulacao
    Apreciacao --- V_Evita --> Critica
    
    %% Detalhamento Crítica
    Critica --- V_Mata --> Ambicao
    
    %% Qualidades (Bajulação vs Apreciação)
    Bajulacao --- V_Eh1 --> Falsa & Egoista
    Apreciacao --- V_Eh2 --> Sincera & Altruista
    
    %% Resultados Positivos
    Apreciacao --- V_Gera --> Entusiasmo & Sucesso
```

---

> [!NOTE]
> **BIBLIOGRAFIA:**
> Carnegie, Dale. *Como fazer amigos e influenciar pessoas*. 52. ed. São Paulo: Companhia Editora Nacional, 2012.

---

## Relatório de Conformidade (Norma SYNTROPY v3.0)

1.  **Governança:** Pergunta Focal e Bibliografia isoladas fora do corpo do mapa.
2.  **Geometria Rígida:**
    *   **Conceitos:** Retângulos (`[]`) com wrapping aplicado (ex: `Fazer Outro<br/>Querer`, `Desejo de<br/>Importância`).
    *   **Verbos:** Círculos (`(())`) menores que os retângulos.
3.  **Topologia de Conexão:**
    *   **Conceito -> Verbo:** Linha sólida (`---`);
    *   **Verbo -> Conceito:** Seta direcionada (`-->`).
4.  **Anti-Entropia (LOG #012):**
    *   **Desejos Humanos:** Unificados no nó `((incluem))`.
    *   **Resultados da Importância:** Unificados no nó `((origina))`.
    *   **Qualidades:** Unificados nos nós `((é))`.
5.  **Compatibilidade:** Código Mermaid otimizado para renderização no Obsidian.
