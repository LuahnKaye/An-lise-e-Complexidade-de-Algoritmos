# Trabalho: Análise de Complexidade de Algoritmos
### Sequência de Fibonacci, Números de Pell e Números de Catalan

---

## 📁 Estrutura de Pastas do Projeto

O repositório foi organizado em três diretórios correspondentes a cada sequência:

```text
trab-complexidade-de-algoritmos/
│
├── 1_fibonacci/
│   ├── 1_fibonacci_definicao.py          # Abordagem 1: Recursiva direta O(2^n)
│   ├── 2_fibonacci_intermediarios.py     # Abordagem 2: Programação Dinâmica / Iterativa O(n)
│   ├── 3_fibonacci_matrizes.py           # Abordagem 3: Exponenciação Rápida de Matrizes O(log n)
│   ├── 4_comparativo_geral.py           # Comparativo consolidado
│   ├── 5_gerar_graficos.py              # Script gerador dos gráficos
│   ├── graficos_fibonacci.png           # Gráfico comparativo linear e de grandes valores
│   └── grafico_escala_log.png           # Gráfico em escala logarítmica
│
├── 2_pell/
│   ├── pell_iterativo.py                # Abordagem 1: Iterativo com DP O(n)
│   ├── pell_matrizes.py                 # Abordagem 2: Exponenciação de Matrizes O(log n)
│   ├── pell_recursivo.py                # Abordagem comparativa: Recursão pura O((1+√2)^n)
│   ├── pell_graficos.py                 # Script gerador dos gráficos de Pell
│   └── graficos_pell.png                # Gráficos comparativos de desempenho
│
├── 3_catalan/
│   ├── catalan_recursivo.py             # Recursão pura por convolução O(4^n / n^1.5)
│   ├── catalan_dp.py                    # Abordagem 1: Programação Dinâmica O(n^2)
│   ├── catalan_analitico.py             # Abordagem 2: Fórmula Multiplicativa O(n)
│   ├── catalan_graficos.py              # Script gerador dos gráficos de Catalan
│   └── graficos_catalan.png             # Gráficos comparativos de desempenho
│
├── .gitignore
└── README.md                            # Documentação completa e referências
```

---

# PARTE 1: SEQUÊNCIA DE FIBONACCI

## 1. Descrição das Abordagens
- **Pela Definição ($\mathcal{O}(2^n)$):** $F(0)=0, F(1)=1, F(n) = F(n-1) + F(n-2)$. Árvore de recursão redundante com complexidade de tempo $\Theta(\phi^n)$ ($\phi \approx 1,618$) e espaço $\mathcal{O}(n)$ na pilha.
- **Resultados Intermediários ($\mathcal{O}(n)$):** Abordagem *bottom-up* que calcula linearmente reaproveitando os dois termos anteriores ($a, b = b, a + b$). Espaço $\mathcal{O}(1)$.
- **Utilizando Matrizes ($\mathcal{O}(\log n)$):** Relação matricial $\begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}^n = \begin{pmatrix} F_{n+1} & F_n \\ F_n & F_{n-1} \end{pmatrix}$ resolvida via potenciação binária (divisão e conquista). Espaço $\mathcal{O}(1)$.

## 2. Resultados Experimentais: $F(5)$, $F(15)$ e $F(30)$

| $n$ | $F(n)$ | 1. Pela Definição $\mathcal{O}(2^n)$ | 2. Intermediários $\mathcal{O}(n)$ | 3. Matrizes $\mathcal{O}(\log n)$ |
| :---: | :---: | :---: | :---: | :---: |
| **5** | **5** | **0.0029 ms** (15 chamadas) | **0.0017 ms** | **0.0065 ms** |
| **15** | **610** | **0.0652 ms** (1.973 chamadas) | **0.0011 ms** | **0.0040 ms** |
| **30** | **832.040** | **86.2645 ms** (2.692.537 chamadas) | **0.0032 ms** | **0.0087 ms** |

## 3. Maior Número Calculável (Fibonacci)
- **Pela Definição:** $n \approx 38$ a $42$ (limite: tempo de CPU exponencial; $F(50)$ levaria horas).
- **Resultados Intermediários:** $n \approx 500.000$ a $1.000.000$ (limite: custo de adição de *bignum* em $\mathcal{O}(n)$ e memória RAM).
- **Matrizes:** $n \approx 10.000.000$ a $50.000.000$ (apenas 24 multiplicações para $n=10^7$; limite: multiplicação de inteiros de milhões de dígitos).

---

# PARTE 2: NÚMEROS DE PELL

## 1. Definição Matemática
A sequência de Pell é dada pela relação de recorrência linear:
$$P_0 = 0, \quad P_1 = 1, \quad P_n = 2 \cdot P_{n-1} + P_{n-2} \quad (n \ge 2)$$
Termos iniciais: `0, 1, 2, 5, 12, 29, 70, 169, 408, 985, 2378, ...`

A equação característica é $r^2 - 2r - 1 = 0$, com raízes $r = 1 \pm \sqrt{2}$. A raiz dominante $1 + \sqrt{2} \approx 2,41421356$ é a **Proporção Prateada** (*Silver Ratio* $\delta_S$).

## 2. Aplicações Práticas
1. **Aproximação Rápida de $\sqrt{2}$:** A razão entre termos de Pell $\frac{P_n + P_{n-1}}{P_n}$ produz as convergentes em frações contínuas de $\sqrt{2}$ ($\frac{3}{2}, \frac{7}{5}, \frac{17}{12}, \frac{41}{29}, \frac{577}{408} \approx 1,4142156$).
2. **Equação de Pell ($x^2 - 2y^2 = \pm 1$):** Soluções inteiras fundamentais para criptografia de curvas e corpos quadráticos.
3. **Roteamento de Redes:** Particionamento topológico e balanceamento de carga em redes distribuídas.

## 3. Implementação e Resultados

| $n$ | $P(n)$ | Abordagem 1: Iterativo $\mathcal{O}(n)$ | Abordagem 2: Matrizes $\mathcal{O}(\log n)$ |
| :---: | :---: | :---: | :---: |
| **5** | **29** | **0.0020 ms** | **0.0067 ms** |
| **15** | **195.025** | **0.0017 ms** | **0.0047 ms** |
| **30** | **107.578.520.350** | **0.0020 ms** | **0.0049 ms** |

## 4. Maior Número Calculável (Pell)
- **Iterativo:** $n \approx 300.000$ a $500.000$ ($P(300.000)$ possui $114.833$ dígitos calculados em ~2,3s).
- **Matrizes:** $n \approx 5.000.000$ a $10.000.000$ ($P(1.000.000)$ possui $382.776$ dígitos calculados em ~0,69s).

---

# PARTE 3: NÚMEROS DE CATALAN

## 1. Definição Matemática
Os números de Catalan formam uma sequência de inteiros que satisfaz a relação de recorrência por convolução (recorrência de Segner):
$$C_0 = 1, \quad C_{n+1} = \sum_{i=0}^{n} C_i \cdot C_{n-i} \quad (n \ge 0)$$
Ou explicitamente via coeficientes binomiais e relação multiplicativa direta:
$$C_n = \frac{1}{n+1} \binom{2n}{n} = \frac{(2n)!}{(n+1)!\,n!}, \qquad C_n = \frac{2(2n-1)}{n+1} C_{n-1}$$
Termos iniciais: `1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, 58786, ...`

## 2. Aplicações Práticas na Ciência da Computação
1. **Contagem de Árvores Binárias:** $C_n$ é exatamente o número de árvores binárias estruturalmente distintas que podem ser formadas com $n$ nós.
2. **Design de Compiladores e Agrupamento de Parênteses:** Número de maneiras válidas de parentizar uma expressão matemática com $n+1$ fatores (ex.: multiplicação de matrizes em cadeia).
3. **Árvores de Sintaxe Abstrata (AST):** Quantificação e otimização de árvores sintáticas geradas por analisadores sintáticos (*parsers*).
4. **Caminhos de Dyck e Polígonos:** Número de triangulações convexas de um polígono com $n+2$ lados e caminhos em grade que não cruzam a diagonal principal.

## 3. Implementação das Duas Abordagens

### Abordagem 1: Programação Dinâmica ($\mathcal{O}(n^2)$)
- **Arquivo:** `3_catalan/catalan_dp.py`
- **Funcionamento:** Armazena uma tabela de $C_0$ até $C_n$ e computa cada termo por convolução: $dp[i] = \sum_{j=0}^{i-1} dp[j] \cdot dp[i-1-j]$.
- **Complexidade:** Tempo $\mathcal{O}(n^2)$, Espaço $\mathcal{O}(n)$.

### Abordagem 2: Fórmula Recorrente Multiplicativa Linear ($\mathcal{O}(n)$)
- **Arquivo:** `3_catalan/catalan_analitico.py`
- **Funcionamento:** Inicia em $c=1$ e atualiza $c = \frac{c \cdot 2(2i-1)}{i+1}$ para $i$ de $1$ a $n$.
- **Complexidade:** Tempo $\mathcal{O}(n)$, Espaço $\mathcal{O}(1)$.

*(O arquivo `3_catalan/catalan_recursivo.py` foi incluído como referência da definição ingênua $\mathcal{O}(4^n / n^{1.5})$).*

## 4. Resultados Experimentais (Catalan)

| $n$ | $C(n)$ | Abordagem 1: Prog. Dinâmica $\mathcal{O}(n^2)$ | Abordagem 2: Multiplicativo $\mathcal{O}(n)$ |
| :---: | :---: | :---: | :---: |
| **5** | **42** | **0.0046 ms** | **0.0023 ms** |
| **15** | **9.694.845** | **0.0094 ms** | **0.0021 ms** |
| **30** | **3.814.986.502.092.304** | **0.0319 ms** | **0.0031 ms** |

## 5. O que os Gráficos nos dizem sobre a Performance? (Catalan)
Os gráficos gerados em `3_catalan/graficos_catalan.png` revelam:
1. **Hiper-explosão da Recursão Pura ($n=1$ a $15$):** O custo $\mathcal{O}(4^n / n^{1.5})$ explode muito mais rápido que Fibonacci e Pell, tornando inviável passar de $n \approx 16$.
2. **Impacto de $\mathcal{O}(n^2)$ vs $\mathcal{O}(n)$ em Grandes Valores:** Para $n = 2.500$, a programação dinâmica $\mathcal{O}(n^2)$ gasta mais de **$5,5$ segundos** devido aos milhões de pares da convolução, enquanto a fórmula multiplicativa $\mathcal{O}(n)$ executa em **$0,001$ segundo** (milésimos de segundo).

## 6. Maior Número Calculável (Catalan)
- **Recursão Pura:** $n \approx 15 \sim 18$.
- **Programação Dinâmica $\mathcal{O}(n^2)$:** $n \approx 3.000 \sim 5.000$ (acima disso o tempo quadrático ultrapassa dezenas de segundos).
- **Fórmula Multiplicativa $\mathcal{O}(n)$:** **$n \approx 100.000$ a $300.000$** ($C(100.000)$ possui mais de $60.000$ dígitos decimais e é calculado em ~1,9s).

---

## 📚 Referências Bibliográficas

1. **CORMEN, Thomas H. et al.** *Introduction to Algorithms* (Algoritmos: Teoria e Prática). 3. ed. MIT Press / Campus, 2009. (Cap. 15: Programação Dinâmica; Cap. 31: Exponenciação de Matrizes).
2. **STANLEY, Richard P.** *Catalan Numbers*. Cambridge University Press, 2015. (Tratado abrangente sobre aplicações combinatórias, árvores binárias e linguagens formais).
3. **SEDGEWICK, Robert; FLAJOLET, Philippe.** *An Introduction to the Analysis of Algorithms*. 2. ed. Addison-Wesley, 2013. (Análise assintótica de recorrências de convolução e números de Catalan).
4. **DASGUPTA, Sanjoy; PAPADIMITRIOU, Christos; VAZIRANI, Umesh.** *Algorithms*. McGraw-Hill, 2006. (Cap. 0: Prologue - Fibonacci numbers).
5. **HORADAM, A. F.** "Pell Identities." *The Fibonacci Quarterly*, v. 9, n. 3, p. 245-252, 1971.

---

## 🚀 Como Executar os Scripts

```bash
# --- 1. FIBONACCI ---
py 1_fibonacci/1_fibonacci_definicao.py
py 1_fibonacci/2_fibonacci_intermediarios.py
py 1_fibonacci/3_fibonacci_matrizes.py
py 1_fibonacci/4_comparativo_geral.py
py 1_fibonacci/5_gerar_graficos.py

# --- 2. PELL ---
py 2_pell/pell_iterativo.py
py 2_pell/pell_matrizes.py
py 2_pell/pell_recursivo.py
py 2_pell/pell_graficos.py

# --- 3. CATALAN ---
py 3_catalan/catalan_dp.py
py 3_catalan/catalan_analitico.py
py 3_catalan/catalan_recursivo.py
py 3_catalan/catalan_graficos.py
```
