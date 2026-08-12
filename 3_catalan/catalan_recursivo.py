import time
import sys

def catalan_recursivo(n: int) -> int:
    if n <= 0:
        return 1
    
    total = 0
    for i in range(n):
        total += catalan_recursivo(i) * catalan_recursivo(n - 1 - i)
    return total

def medir_tempo(n: int):
    inicio = time.perf_counter()
    resultado = catalan_recursivo(n)
    fim = time.perf_counter()
    return resultado, fim - inicio

def main():
    valores = [3, 6, 10, 14]
    
    print("=" * 60)
    print("NUMEROS DE CATALAN - RECURSAO PURA (CONVOLUCAO)")
    print("=" * 60)
    print(f"{'n':<6} | {'C(n)':<18} | {'Tempo (s)':<18} | {'Tempo (ms)'}")
    print("-" * 60)
    
    for n in valores:
        res, t = medir_tempo(n)
        print(f"{n:<6} | {res:<18} | {t:<18.8f} | {t * 1000:.4f} ms")
        
    print("=" * 60)

if __name__ == "__main__":
    main()
