import time
import sys

# Permite que o Python lide com conversao de numeros gigantes para string (necessario para F(500000))
sys.set_int_max_str_digits(1_000_000)

# Versao 2.1: Usando Programacao Dinamica com Tabela (Array/Lista)
# Complexidade: Tempo O(n) e Espaco O(n)
# Resolve o problema da recursao armazenando cada calculo em uma lista (dp).
def fibonacci_tabela(n: int) -> int:
    if n <= 0: return 0
    if n == 1: return 1
    
    # Cria uma lista (tabela) de tamanho n+1 iniciada com zeros
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    
    # Preenche a tabela iterativamente. O calculo de dp[i] usa apenas dp[i-1] e dp[i-2]
    # garantindo que cada numero de Fibonacci seja calculado exatamente UMA vez.
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        
    return dp[n]

# Versao 2.2: Usando Memoizacao (Dicionario + Recursao)
# Complexidade: Tempo O(n) e Espaco O(n) na call stack
# Memoriza os resultados para nao recalcular, porem sofre com o limite de recursao do Python para n > 1000.
def fibonacci_memoizacao(n: int, memo: dict = None) -> int:
    if memo is None:
        memo = {0: 0, 1: 1} # Casos base iniciais
    
    # Se ja calculei antes, simplesmente retorno o valor da memoria (evita a arvore de recursao O(2^n))
    if n in memo:
        return memo[n]
        
    # Se nao, calculo, guardo na memoria, e retorno
    memo[n] = fibonacci_memoizacao(n - 1, memo) + fibonacci_memoizacao(n - 2, memo)
    return memo[n]

# Versao 2.3: Iterativo Otimizado (Apenas duas variaveis - Bottom-up)
# Complexidade: Tempo O(n) e Espaco O(1)
# O metodo mais eficiente desta categoria. Nao guarda o historico completo, 
# apenas os dois ultimos numeros necessarios para o proximo passo.
def fibonacci_iterativo(n: int) -> int:
    if n <= 0: return 0
    if n == 1: return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        # O novo 'a' recebe 'b', e o novo 'b' recebe a soma 'a + b'
        a, b = b, a + b
        
    return b

def medir_tempo(func, *args):
    # Mede o tempo de execucao
    inicio = time.perf_counter()
    resultado = func(*args)
    fim = time.perf_counter()
    return resultado, fim - inicio

def main():
    valores = [5, 15, 30]
    
    print("=" * 65)
    print("FIBONACCI - VERSAO 2: RESULTADOS INTERMEDIARIOS")
    print("=" * 65)
    print(f"{'n':<6} | {'F(n)':<15} | {'Tempo Tabela':<18} | {'Tempo Iterativo'}")
    print("-" * 65)
    
    for n in valores:
        res, t_tab = medir_tempo(fibonacci_tabela, n)
        _, t_ite = medir_tempo(fibonacci_iterativo, n)
        print(f"{n:<6} | {res:<15} | {t_tab * 1000:<15.4f} ms | {t_ite * 1000:.4f} ms")
    
    print("=" * 65)
    print("\nTestes com valores maiores (provando a complexidade O(n)):")
    for n in [1000, 10000, 100000, 500000]:
        res, t = medir_tempo(fibonacci_iterativo, n)
        digitos = len(str(res))
        print(f"F({n}) calculado em {t:.4f} s ({digitos} digitos)")

if __name__ == "__main__":
    main()
