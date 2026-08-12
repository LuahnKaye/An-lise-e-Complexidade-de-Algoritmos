# Relatório: Análise de Complexidade de Algoritmos
## Sequência de Fibonacci e Números de Pell

---

# PARTE 1: SEQUÊNCIA DE FIBONACCI

## 1. Descrição das Abordagens

### 1. Pela Definição Matemática (Recursão Pura)
- **Arquivo:** `1_fibonacci_definicao.py`
- **Funcionamento:** $F(0)=0$, $F(1)=1$ e $F(n) = F(n-1) + F(n-2)$.
- **Complexidade de Tempo:** $\mathcal{O}(2^n)$ ou $\Theta(\phi^n)$, onde $\phi \approx 1,618$ (Proporção Áurea).
- **Complexidade de Espaço:** $\mathcal{O}(n)$ na pilha de chamadas.

### 2. Armazenando Resultados Intermediários (Programação Dinâmica / Iterativo)
- **Arquivo:** `2_fibonacci_intermediarios.py`
- **Funcionamento:** Calcula de baixo para cima (*bottom-up*), armazenando os dois termos anteriores.
- **Complexidade de Tempo:** $\mathcal{O}(n)$.
- **Complexidade de Espaço:** $\mathcal{O}(1)$ (duas variáveis) ou $\mathcal{O}(n)$ (vetor).

### 3. Utilizando Matrizes (Exponenciação Rápida)
- **Arquivo:** `3_fibonacci_matrizes.py`
- **Funcionamento:** Exponenciação binária da matriz:
$$\begin{pmatrix} F_{n+1} & F_n \\ F_n & F_{n-1} \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}^n$$
- **Complexidade de Tempo:** $\mathcal{O}(\log n)$ multiplicações de matrizes.
- **Complexidade de Espaço:** $\mathcal{O}(1)$.

---

## 2. Resultados Experimentais: $F(5)$, $F(15)$ e $F(30)$

| $n$ | $F(n)$ | 1. Pela Definição $\mathcal{O}(2^n)$ | 2. Intermediários $\mathcal{O}(n)$ | 3. Matrizes $\mathcal{O}(\log n)$ |
| :---: | :---: | :---: | :---: | :---: |
| **5** | **5** | **0.0029 ms** | **0.0017 ms** | **0.0065 ms** |
| **15** | **610** | **0.0652 ms** | **0.0011 ms** | **0.0040 ms** |
| **30** | **832.040** | **86.2645 ms** (~2,69M chamadas) | **0.0032 ms** | **0.0087 ms** |

---

## 3. Maior Número Calculável (Fibonacci)
- **Pela Definição:** $n \approx 38$ a $42$ (limite: tempo de CPU exponencial).
- **Resultados Intermediários:** $n \approx 500.000$ a $1.000.000$ (limite: memória RAM e custo da soma *bignum*).
- **Matrizes:** $n \approx 10.000.000$ a $50.000.000$ (limite: multiplicação de inteiros de milhões de dígitos).

---

# PARTE 2: NÚMEROS DE PELL

## 1. Definição Matemática dos Números de Pell
A sequência de Pell é uma relação de recorrência linear de segunda ordem definida por:
$$P_0 = 0$$
$$P_1 = 1$$
$$P_n = 2 \cdot P_{n-1} + P_{n-2}, \quad \text{para } n \ge 2$$

Os primeiros termos da sequência são:
`0, 1, 2, 5, 12, 29, 70, 169, 408, 985, 2378, 5741, 13860, 33461, ...`

A equação característica associada é $r^2 - 2r - 1 = 0$, cujas raízes são $r = 1 \pm \sqrt{2}$. A raiz dominante $1 + \sqrt{2} \approx 2,41421356$ é conhecida como a **Proporção Prateada** (*Silver Ratio* $\delta_S$). A fórmula fechada de Binet para Pell é:
$$P_n = \frac{(1 + \sqrt{2})^n - (1 - \sqrt{2})^n}{2\sqrt{2}}$$

---

## 2. Aplicações Práticas dos Números de Pell

1. **Aproximação Rápida da Raiz Quadrada de 2 ($\sqrt{2}$):**
   A razão entre termos consecutivos de Pell associados aos números de Pell-Lucas gera as melhores aproximações racionais (frações contínuas) de $\sqrt{2}$:
   $$\frac{P_n + P_{n-1}}{P_n} \approx \sqrt{2}$$
   - Para $n=2$: $\frac{2 + 1}{2} = \frac{3}{2} = 1,5$
   - Para $n=3$: $\frac{5 + 2}{5} = \frac{7}{5} = 1,4$
   - Para $n=4$: $\frac{12 + 5}{12} = \frac{17}{12} \approx 1,4166$
   - Para $n=5$: $\frac{29 + 12}{29} = \frac{41}{29} \approx 1,41379$
   - Para $n=8$: $\frac{408 + 169}{408} = \frac{577}{408} \approx 1,4142156$ (precisão de 5 casas decimais).

2. **Equações Diofantinas (Equação de Pell):**
   Equações da forma $x^2 - 2y^2 = \pm 1$ possuem soluções inteiras dadas exatamente pelos números de Pell: $x = P_n + P_{n-1}$ e $y = P_n$.

3. **Criptografia de Chave Pública e Roteamento de Redes:**
   As propriedades aritméticas da Equação de Pell e dos corpos quadráticos $\mathbb{Z}[\sqrt{d}]$ são empregadas em esquemas criptográficos baseados em curvas algébricas e no particionamento e balanceamento ótimo de nós em topologias de redes interconectadas.

---

## 3. Implementação das Duas Abordagens

### Abordagem 1: Iterativa com Programação Dinâmica ($\mathcal{O}(n)$)
- **Arquivo:** `pell_iterativo.py`
- **Funcionamento:** Inicia com $a=0, b=1$ e atualiza iterativamente $a, b = b, 2b + a$.
- **Complexidade de Tempo:** $\mathcal{O}(n)$.
- **Complexidade de Espaço:** $\mathcal{O}(1)$.

### Abordagem 2: Exponenciação de Matrizes ($\mathcal{O}(\log n)$)
- **Arquivo:** `pell_matrizes.py`
- **Funcionamento:** Utiliza a representação matricial da recorrência de Pell:
$$\begin{pmatrix} P_{n+1} & P_n \\ P_n & P_{n-1} \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 1 & 0 \end{pmatrix}^n$$
  Calculada em tempo logarítmico via potenciação binária.
- **Complexidade de Tempo:** $\mathcal{O}(\log n)$ multiplicações.
- **Complexidade de Espaço:** $\mathcal{O}(1)$.

---

## 4. Resultados Experimentais (Pell)

| $n$ | $P(n)$ | Abordagem 1: Iterativo $\mathcal{O}(n)$ | Abordagem 2: Matrizes $\mathcal{O}(\log n)$ |
| :---: | :---: | :---: | :---: |
| **5** | **29** | **0.0020 ms** | **0.0067 ms** |
| **15** | **195.025** | **0.0017 ms** | **0.0047 ms** |
| **30** | **107.578.520.350** | **0.0020 ms** | **0.0049 ms** |

---

## 5. Análise dos Gráficos de Performance (Pell)

Os gráficos gerados pelo script `pell_graficos.py` (arquivo `graficos_pell.png`) mostram:

1. **Crescimento Exponencial da Definição Recursiva ($n=1$ a $26$):**
   - Como a base da exponenciação dos números de Pell é a razão prateada $\delta_S \approx 2,414$ (maior que a razão áurea de Fibonacci $\phi \approx 1,618$), a explosão do tempo de execução ocorre ainda mais rápido (em $n \approx 24$, o tempo já atinge múltiplos segundos).

2. **Iterativo $\mathcal{O}(n)$ vs. Matrizes $\mathcal{O}(\log n)$ para Grandes Valores ($n=1.000$ a $300.000$):**
   - O método iterativo cresce linearmente em operações, alcançando mais de $2$ segundos para $n = 300.000$.
   - O método matricial realiza apenas ~18 multiplicações de matrizes, finalizando o cálculo em menos de $0,15$ segundos.

---

## 6. Maior Número Calculável (Pell)

- **Abordagem Iterativa:** **$n \approx 300.000$ a $500.000$** (gerando números com mais de $110.000$ dígitos decimais em ~2 segundos).
- **Abordagem com Matrizes:** **$n \approx 5.000.000$ a $10.000.000$** (calcula $P(1.000.000)$ com mais de $382.000$ dígitos em ~0,69 segundos).

---

## 7. Referências Bibliográficas

1. **HORADAM, A. F.** "Pell Identities." *The Fibonacci Quarterly*, v. 9, n. 3, p. 245-252, 1971.
2. **CORMEN, Thomas H. et al.** *Introduction to Algorithms*. 3. ed. MIT Press, 2009. (Exponenciação de Matrizes em Recorrências Lineares).
3. **LENSTRA, H. W.** "Solving the Pell Equation." *Notices of the AMS*, v. 49, n. 2, p. 182-192, 2002.
4. **DASGUPTA, Sanjoy; PAPADIMITRIOU, Christos; VAZIRANI, Umesh.** *Algorithms*. McGraw-Hill, 2006.

---

## 8. Como Executar os Scripts

```bash
# Fibonacci
py 1_fibonacci_definicao.py
py 2_fibonacci_intermediarios.py
py 3_fibonacci_matrizes.py
py 4_comparativo_geral.py
py 5_gerar_graficos.py

# Pell
py pell_iterativo.py
py pell_matrizes.py
py pell_recursivo.py
py pell_graficos.py
```
