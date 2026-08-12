import time
import sys

sys.set_int_max_str_digits(1_000_000)

def catalan_dp(n: int) -> int:
    if n <= 0:
        return 1
    
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(1, n + 1):
        for j in range(i):
            dp[i] += dp[j] * dp[i - 1 - j]
            
    return dp[n]

def medir_tempo(n: int):
    inicio = time.perf_counter()
    resultado = catalan_dp(n)
    fim = time.perf_counter()
    return resultado, fim - inicio

def main():
    valores = [5, 15, 30]
    
    print("=" * 60)
    print("NUMEROS DE CATALAN - PROGRAMACAO DINAMICA O(n^2)")
    print("=" * 60)
    print(f"{'n':<6} | {'C(n)':<22} | {'Tempo (s)':<16} | {'Tempo (ms)'}")
    print("-" * 60)
    
    for n in valores:
        res, t = medir_tempo(n)
        print(f"{n:<6} | {res:<22} | {t:<16.8f} | {t * 1000:.4f} ms")
        
    print("=" * 60)
    print("\nTestes com valores maiores:")
    for n in [100, 500, 1000, 3000]:
        res, t = medir_tempo(n)
        digitos = len(str(res))
        print(f"C({n}) calculado em {t:.4f} s ({digitos} digitos)")

if __name__ == "__main__":
    main()
