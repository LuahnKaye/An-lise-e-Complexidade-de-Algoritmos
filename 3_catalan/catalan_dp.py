import time
import sys

# Permite calcular fatoriais grandes sem estourar o limite de string do interpretador
sys.set_int_max_str_digits(5_000_000)

# Abordagem 1: Usando Programacao Dinamica
# Complexidade: Tempo O(n^2) e Espaco O(n)
# Por que O(n^2)? Porque usamos 2 loops: um para varrer i de 1 a n, 
# e um loop interno para varrer j de 0 a i-1 realizando a convolucao.
def catalan_dp(n: int) -> int:
    if n <= 0:
        return 1
    
    # Criamos um array dp de tamanho n+1 para guardar as respostas calculadas
    dp = [0] * (n + 1)
    dp[0] = 1 # O primeiro Catalan e 1
    dp[1] = 1 # O segundo tambem
    
    # Preenchimento Bottom-up (de baixo para cima)
    for i in range(2, n + 1):
        # A formula eh dp[i] = somatorio(dp[j] * dp[i-1-j])
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
    print("\nTestes com valores maiores (mostrando a queda do O(n^2)):")
    # Em n=3000 o algoritmo O(n^2) ja sofre bastante (demorando muitos segundos)
    for n in [100, 500, 1000, 3000]:
        res, t = medir_tempo(n)
        bits = res.bit_length()
        digitos = int(bits * 0.30103) + 1
        print(f"C({n}) calculado em {t:.4f} s ({digitos} digitos)")

if __name__ == "__main__":
    main()
