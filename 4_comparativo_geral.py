import time
import sys

def fib_definicao(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fib_definicao(n - 1) + fib_definicao(n - 2)

def fib_intermediarios(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def _mult_matrizes(A, B):
    return [
        [A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
        [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]
    ]

def fib_matrizes(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1
    
    res = [[1, 0], [0, 1]]
    base = [[1, 1], [1, 0]]
    exp = n
    
    while exp > 0:
        if exp % 2 == 1:
            res = _mult_matrizes(res, base)
        base = _mult_matrizes(base, base)
        exp //= 2
        
    return res[0][1]

def medir(func, n):
    inicio = time.perf_counter()
    resultado = func(n)
    fim = time.perf_counter()
    return resultado, fim - inicio

def main():
    valores = [5, 15, 30]
    
    print("=" * 80)
    print("COMPARATIVO DE EXECUCAO - FIBONACCI")
    print("=" * 80)
    print(f"{'n':<6} | {'F(n)':<12} | {'Definicao O(2^n)':<20} | {'Intermediarios O(n)':<20} | {'Matrizes O(log n)'}")
    print("-" * 80)
    
    for n in valores:
        res1, t1 = medir(fib_definicao, n)
        _, t2 = medir(fib_intermediarios, n)
        _, t3 = medir(fib_matrizes, n)
        
        t1_str = f"{t1 * 1000:.4f} ms"
        t2_str = f"{t2 * 1000:.4f} ms"
        t3_str = f"{t3 * 1000:.4f} ms"
        
        print(f"{n:<6} | {res1:<12} | {t1_str:<20} | {t2_str:<20} | {t3_str}")
        
    print("=" * 80)

if __name__ == "__main__":
    main()
