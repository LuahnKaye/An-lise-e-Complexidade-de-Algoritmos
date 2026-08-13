import time
import sys

sys.set_int_max_str_digits(5_000_000)

def multiplicar_matrizes(A, B):
    # Funcao padrao para multiplicacao de matrizes 2x2
    return [
        [A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
        [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]
    ]

# Abordagem 2: Utilizando Exponenciacao de Matrizes
# Complexidade: Tempo O(log n) e Espaco O(1)
# Matematicamente, a relacao de Pell pode ser expressa matricialmente:
# [P(n+1) P(n)  ] = [2 1]^n
# [P(n)   P(n-1)]   [1 0]
def pell_matriz(n: int) -> int:
    if n <= 0: return 0
    if n == 1: return 1
    
    # Matriz Identidade
    resultado = [[1, 0], [0, 1]]
    # Matriz Base da sequencia de Pell
    base = [[2, 1], [1, 0]]
    exp = n
    
    # Binary Exponentiation: O algoritmo que garante complexidade O(log n)
    while exp > 0:
        if exp % 2 == 1:
            resultado = multiplicar_matrizes(resultado, base)
        base = multiplicar_matrizes(base, base)
        exp //= 2
        
    return resultado[0][1]

def medir_tempo(n: int):
    inicio = time.perf_counter()
    resultado = pell_matriz(n)
    fim = time.perf_counter()
    return resultado, fim - inicio

def main():
    valores = [5, 15, 30]
    
    print("=" * 60)
    print("NUMEROS DE PELL - ABORDAGEM 2: MATRIZES")
    print("=" * 60)
    print(f"{'n':<6} | {'P(n)':<18} | {'Tempo (s)':<18} | {'Tempo (ms)'}")
    print("-" * 60)
    
    for n in valores:
        res, t = medir_tempo(n)
        print(f"{n:<6} | {res:<18} | {t:<18.8f} | {t * 1000:.4f} ms")
    
    print("=" * 60)
    print("\nTestes com valores grandes (O(log n) brilha aqui):")
    # Gracas ao O(log n) logramos elevar a potencia 5.000.000 com extrema facilidade
    for n in [1000, 10000, 100000, 1000000, 5000000]:
        res, t = medir_tempo(n)
        bits = res.bit_length()
        digitos = int(bits * 0.30103) + 1
        print(f"P({n}) calculado em {t:.4f} s (~{digitos} digitos)")

if __name__ == "__main__":
    main()
