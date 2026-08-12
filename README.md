# Relatório: Análise de Complexidade e Desempenho no Cálculo da Sequência de Fibonacci

## 1. Objetivo do Trabalho
Implementar, testar e analisar comparativamente três abordagens algorítmicas para o cálculo do $n$-ésimo número da Sequência de Fibonacci ($F_n$), avaliando o tempo de execução, a complexidade assintótica (tempo e espaço), o comportamento gráfico de crescimento e os limites computacionais de cada método.

---

## 2. Descrição das Abordagens

### 1. Pela Definição Matemática (Recursão Pura)
- **Arquivo:** `1_fibonacci_definicao.py`
- **Funcionamento:** Aplica a definição matemática direta: $F(0)=0$, $F(1)=1$ e $F(n) = F(n-1) + F(n-2)$.
- **Complexidade de Tempo:** $\mathcal{O}(2^n)$ ou precisamente $\Theta(\phi^n)$, onde $\phi \approx 1,618$ (Proporção Áurea).
- **Complexidade de Espaço:** $\mathcal{O}(n)$ na pilha de chamadas de recursão.
- **Característica:** Constrói uma árvore binária de chamadas com recálculos redundantes massivos (ex.: $F(n-2)$ é recalculado repetidamente por múltiplos ramos).

### 2. Armazenando Resultados Intermediários (Programação Dinâmica / Iterativa)
- **Arquivo:** `2_fibonacci_intermediarios.py`
- **Funcionamento:** Elimina recálculos armazenando os termos anteriores. A versão iterativa calcula de baixo para cima (*bottom-up*), mantendo apenas as duas variáveis anteriores ($a$ e $b$).
- **Complexidade de Tempo:** $\mathcal{O}(n)$ (cada termo de $2$ até $n$ é computado exatamente uma vez).
- **Complexidade de Espaço:** $\mathcal{O}(1)$ utilizando duas variáveis (ou $\mathcal{O}(n)$ se armazenado em vetor).
- **Característica:** Execução linear eficiente, sem repetição de trabalho.

### 3. Utilizando Matrizes (Exponenciação Rápida)
- **Arquivo:** `3_fibonacci_matrizes.py`
- **Funcionamento:** Utiliza a relação matricial clássica:
$$\begin{pmatrix} F_{n+1} & F_n \\ F_n & F_{n-1} \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}^n$$
  Calcula a potência da matriz $2 \times 2$ por **potenciação binária** (divisão e conquista), dividindo o expoente por 2 a cada etapa.
- **Complexidade de Tempo:** $\mathcal{O}(\log n)$ multiplicações de matrizes.
- **Complexidade de Espaço:** $\mathcal{O}(1)$ iterativo.
- **Característica:** Realiza um número mínimo de operações mesmo para números na casa dos milhões (ex.: para $n=1.000.000$, são necessárias apenas ~20 multiplicações de matrizes).

---

## 3. Resultados Experimentais: $F(5)$, $F(15)$ e $F(30)$

Os testes foram executados em ambiente Python 3.12 com cronometragem em alta precisão (`time.perf_counter`):

| $n$ | $F(n)$ | 1. Pela Definição $\mathcal{O}(2^n)$ | 2. Intermediários $\mathcal{O}(n)$ | 3. Matrizes $\mathcal{O}(\log n)$ |
| :---: | :---: | :---: | :---: | :---: |
| **5** | **5** | **0.0025 ms** (15 chamadas) | **0.0014 ms** | **0.0059 ms** |
| **15** | **610** | **0.0637 ms** (1.973 chamadas) | **0.0011 ms** | **0.0040 ms** |
| **30** | **832.040** | **84.5288 ms** (2.692.537 chamadas) | **0.0034 ms** | **0.0076 ms** |

---

## 4. O Maior Número Calculável em Cada Versão

### Versão 1: Pela Definição
- **Maior valor prático:** **$n \approx 38$ a $42$** (para tempo $\le 1$ minuto).
- **Limite:** **Tempo de CPU exponencial**. O número de operações cresce a uma taxa de $1,618^n$.
  - $F(30)$: ~2,69 milhões de operações (84 ms).
  - $F(35)$: ~29,8 milhões de operações (~1,7 s).
  - $F(40)$: ~331 milhões de operações (~35 s).
  - $F(50)$: ~40 bilhões de operações (levaria horas).
  - $F(100)$: $> 10^{20}$ operações (tempo maior que a idade do universo).

### Versão 2: Resultados Intermediários
- **Maior valor prático:** **$n \approx 500.000$ a $1.000.000$**.
- **Limite:** Custo de adição de inteiros de precisão arbitrária (*bignum*) e memória RAM.
  - $F(100.000)$ possui $20.899$ dígitos decimais (tempo: ~0,06 s).
  - $F(500.000)$ possui $104.494$ dígitos decimais (tempo: ~1,32 s).
  - $F(1.000.000)$ possui $208.988$ dígitos decimais (tempo: ~3,5 s).

### Versão 3: Utilizando Matrizes
- **Maior valor prático:** **$n \approx 10.000.000$ a $50.000.000$ (10 a 50 milhões)**.
- **Limite:** A quantidade de multiplicações é irrelevante ($\approx 24$ passos para $10^7$). O limite é a multiplicação de números com milhões de dígitos (algoritmo de Karatsuba) e consumo de memória RAM.
  - $F(1.000.000)$: ~0,27 s (208.988 dígitos).
  - $F(10.000.000)$: ~14 s (**2.089.877 dígitos decimais**).

---

## 5. Análise dos Gráficos de Performance

Os gráficos gerados pelo script `5_gerar_graficos.py` registram e comprovam empiricamente a teoria de complexidade:

1. **Gráfico Linear ($n=1$ até $34$):**
   - A curva da **Definição $\mathcal{O}(2^n)$** sofre uma explosão vertical a partir de $n \approx 28$, inviabilizando sua execução rapidamente.
   - As abordagens de **Resultados Intermediários** e **Matrizes** permanecem completamente estáveis próximas a 0 ms nessa faixa.

2. **Gráfico em Escala Logarítmica:**
   - Na escala logarítmica, a curva exponencial se transforma em uma reta ascendente com inclinação positiva acentuada, ilustrando que a cada acréscimo de $n$, o tempo é multiplicado por uma constante.
   - As versões linear e logarítmica formam linhas muito inferiores, demonstrando ordens de grandeza de separação de desempenho.

3. **Gráfico para Grandes Valores ($n=1.000$ até $400.000$):**
   - Evidencia a diferença entre $\mathcal{O}(n)$ e $\mathcal{O}(\log n)$.
   - Enquanto a abordagem iterativa $\mathcal{O}(n)$ apresenta crescimento contínuo de tempo com centenas de milhares de iterações, a abordagem matricial $\mathcal{O}(\log n)$ mantém tempos inferiores a $0,1$ segundo, confirmando a alta eficiência da exponenciação binária.

---

## 6. Referências Bibliográficas

1. **CORMEN, Thomas H. et al.** *Introduction to Algorithms* (Algoritmos: Teoria e Prática). 3. ed. MIT Press / Campus, 2009.
   - *Capítulo 15:* Dynamic Programming (Programação Dinâmica).
   - *Capítulo 31:* Number-Theoretic Algorithms (Algoritmos de Teoria dos Números e Exponenciação Rápida de Matrizes).
2. **DASGUPTA, Sanjoy; PAPADIMITRIOU, Christos; VAZIRANI, Umesh.** *Algorithms*. McGraw-Hill, 2006.
   - *Capítulo 0:* Prologue - Fibonacci numbers (Análise comparativa detalhada da recursão ingênua, programação dinâmica e exponenciação matricial).
3. **KNUTH, Donald E.** *The Art of Computer Programming, Volume 1: Fundamental Algorithms*. 3. ed. Addison-Wesley, 1997.
   - Seção 1.2.8: Propriedades matemáticas da sequência de Fibonacci e representação matricial.
4. **SEDGEWICK, Robert; WAYNE, Kevin.** *Algorithms*. 4. ed. Addison-Wesley, 2011.

---

## 7. Como Executar os Scripts

```bash
# Execução da Versão 1
py 1_fibonacci_definicao.py

# Execução da Versão 2
py 2_fibonacci_intermediarios.py

# Execução da Versão 3
py 3_fibonacci_matrizes.py

# Comparativo Geral
py 4_comparativo_geral.py

# Geração dos Gráficos
py 5_gerar_graficos.py
```
