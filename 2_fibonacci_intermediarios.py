import time
import sys

sys.set_int_max_str_digits(1_000_000)

def fibonacci_tabela(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1
    
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        
    return dp[n]

def fibonacci_memoizacao(n: int, memo: dict = None) -> int:
    if memo is None:
        memo = {0: 0, 1: 1}
    if n in memo:
        return memo[n]
    memo[n] = fibonacci_memoizacao(n - 1, memo) + fibonacci_memoizacao(n - 2, memo)
    return memo[n]

def fibonacci_iterativo(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def medir_tempo(func, *args):
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
    print("\nTestes com valores maiores:")
    for n in [1000, 10000, 100000, 500000]:
        res, t = medir_tempo(fibonacci_iterativo, n)
        digitos = len(str(res))
        print(f"F({n}) calculado em {t:.4f} s ({digitos} digitos)")

if __name__ == "__main__":
    main()
