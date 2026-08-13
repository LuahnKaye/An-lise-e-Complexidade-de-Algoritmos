import time
import sys

def pell_definicao(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return 2 * pell_definicao(n - 1) + pell_definicao(n - 2)

def medir_tempo(n: int):
    inicio = time.perf_counter()
    resultado = pell_definicao(n)
    fim = time.perf_counter()
    return resultado, fim - inicio

def main():
    valores = [5, 15, 30]
    
    print("=" * 60)
    print("NUMEROS DE PELL - DEFINICAO RECURSIVA")
    print("=" * 60)
    print(f"{'n':<6} | {'P(n)':<18} | {'Tempo (s)':<18} | {'Tempo (ms)'}")
    print("-" * 60)
    
    for n in valores:
        res, t = medir_tempo(n)
        print(f"{n:<6} | {res:<18} | {t:<18.8f} | {t * 1000:.4f} ms")
        
    print("=" * 60)

if __name__ == "__main__":
    main()
