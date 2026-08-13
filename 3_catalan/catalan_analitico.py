import time
import sys

sys.set_int_max_str_digits(5_000_000)

# Abordagem 2: Formula Multiplicativa
# Complexidade: Tempo O(n) e Espaco O(1)
# O numero de Catalan pode ser encontrado utilizando coeficientes binomiais
# ou simplesmente a formula multiplicativa: C_n = C_{n-1} * 2(2n-1) / (n+1)
# Esta e de longe a melhor abordagem em comparacao ao O(n^2) da DP.
def catalan_analitico(n: int) -> int:
    if n <= 0:
        return 1
    
    c = 1 # c representara C_0
    
    for i in range(1, n + 1):
        # A divisao inteira e necessaria para mantermos a precisao exata
        # ao longo de milhoes de digitos
        c = (c * 2 * (2 * i - 1)) // (i + 1)
        
    return c

def medir_tempo(n: int):
    inicio = time.perf_counter()
    resultado = catalan_analitico(n)
    fim = time.perf_counter()
    return resultado, fim - inicio

def main():
    valores = [5, 15, 30]
    
    print("=" * 60)
    print("NUMEROS DE CATALAN - FORMULA MULTIPLICATIVA O(n)")
    print("=" * 60)
    print(f"{'n':<6} | {'C(n)':<22} | {'Tempo (s)':<16} | {'Tempo (ms)'}")
    print("-" * 60)
    
    for n in valores:
        res, t = medir_tempo(n)
        print(f"{n:<6} | {res:<22} | {t:<16.8f} | {t * 1000:.4f} ms")
    
    print("=" * 60)
    print("\nTestes com valores grandes (O(n) brilha aqui tambem):")
    # Aqui o O(n) permite que calculemos C(100.000) facilmente, ao contrario da versao O(n^2)
    for n in [1000, 10000, 50000, 100000]:
        res, t = medir_tempo(n)
        bits = res.bit_length()
        digitos = int(bits * 0.30103) + 1
        print(f"C({n}) calculado em {t:.4f} s (~{digitos} digitos)")

if __name__ == "__main__":
    main()
