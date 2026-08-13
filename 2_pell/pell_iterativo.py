import time
import sys

# Suporte a numeros gigantescos para testar os limites do O(n)
sys.set_int_max_str_digits(5_000_000)

# Abordagem 1: Iterativo (Programacao Dinamica / Bottom-up)
# Complexidade: Tempo O(n) e Espaco O(1)
# O algoritmo "lembra" apenas os dois ultimos calculos, economizando toda a 
# memoria que uma recursao ou lista usaria.
def pell_iterativo(n: int) -> int:
    if n <= 0: return 0
    if n == 1: return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        # A formula eh P(n) = 2*P(n-1) + P(n-2)
        # Entao o novo b eh (2 * b + a)
        a, b = b, 2 * b + a
        
    return b

# Versao alternativa O(n) que guarda num array O(n) espaço (apenas para comparar)
def pell_tabela(n: int) -> int:
    if n <= 0: return 0
    if n == 1: return 1
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = 2 * dp[i - 1] + dp[i - 2]
    return dp[n]

def medir_tempo(func, n):
    inicio = time.perf_counter()
    resultado = func(n)
    fim = time.perf_counter()
    return resultado, fim - inicio

def main():
    valores = [5, 15, 30]
    
    print("=" * 65)
    print("NUMEROS DE PELL - ABORDAGEM 1: ITERATIVA / TABELA")
    print("=" * 65)
    print(f"{'n':<6} | {'P(n)':<18} | {'Tempo Iterativo':<18} | {'Tempo Tabela'}")
    print("-" * 65)
    
    for n in valores:
        res, t_ite = medir_tempo(pell_iterativo, n)
        _, t_tab = medir_tempo(pell_tabela, n)
        print(f"{n:<6} | {res:<18} | {t_ite * 1000:<15.4f} ms | {t_tab * 1000:.4f} ms")
    
    print("=" * 65)
    print("\nTestes com valores grandes (Mostrando a escalabilidade do O(n)):")
    # Chega em n=300k facil!
    for n in [1000, 10000, 100000, 300000]:
        res, t = medir_tempo(pell_iterativo, n)
        bits = res.bit_length()
        digitos = int(bits * 0.30103) + 1
        print(f"P({n}) calculado em {t:.4f} s (~{digitos} digitos)")

if __name__ == "__main__":
    main()
