import time
import sys

sys.set_int_max_str_digits(5_000_000)

def multiplicar_matrizes(A, B):
    return [
        [
            A[0][0] * B[0][0] + A[0][1] * B[1][0],
            A[0][0] * B[0][1] + A[0][1] * B[1][1]
        ],
        [
            A[1][0] * B[0][0] + A[1][1] * B[1][0],
            A[1][0] * B[0][1] + A[1][1] * B[1][1]
        ]
    ]

def potencia_matriz(M, exp: int):
    resultado = [
        [1, 0],
        [0, 1]
    ]
    base = [
        [M[0][0], M[0][1]],
        [M[1][0], M[1][1]]
    ]
    
    while exp > 0:
        if exp % 2 == 1:
            resultado = multiplicar_matrizes(resultado, base)
        base = multiplicar_matrizes(base, base)
        exp //= 2
        
    return resultado

def fibonacci_matriz(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1
    
    M = [
        [1, 1],
        [1, 0]
    ]
    
    Mn = potencia_matriz(M, n)
    return Mn[0][1]

def medir_tempo(n: int):
    inicio = time.perf_counter()
    resultado = fibonacci_matriz(n)
    fim = time.perf_counter()
    return resultado, fim - inicio

def main():
    valores = [5, 15, 30]
    
    print("=" * 60)
    print("FIBONACCI - VERSAO 3: UTILIZANDO MATRIZES")
    print("=" * 60)
    print(f"{'n':<6} | {'F(n)':<15} | {'Tempo (s)':<18} | {'Tempo (ms)'}")
    print("-" * 60)
    
    for n in valores:
        res, t = medir_tempo(n)
        print(f"{n:<6} | {res:<15} | {t:<18.8f} | {t * 1000:.4f} ms")
    
    print("=" * 60)
    print("\nTestes com valores grandes:")
    for n in [1000, 10000, 100000, 1000000, 5000000]:
        res, t = medir_tempo(n)
        bits = res.bit_length()
        digitos = int(bits * 0.30103) + 1
        print(f"F({n}) calculado em {t:.4f} s (~{digitos} digitos)")

if __name__ == "__main__":
    main()
