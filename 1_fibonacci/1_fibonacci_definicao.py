import time
import sys

# Versao 1: Fibonacci pela definicao matematica (recursao pura)
# Complexidade: O(2^n) - cada chamada gera duas novas chamadas
# Muito lento para n > 40 pois repete calculos desnecessariamente

def fibonacci_definicao(n: int) -> int:
    # Casos base da sequencia
    if n <= 0:
        return 0
    if n == 1:
        return 1
    # Chamada recursiva: F(n) = F(n-1) + F(n-2)
    return fibonacci_definicao(n - 1) + fibonacci_definicao(n - 2)

def medir_tempo(n: int):
    # Mede o tempo de execucao com alta precisao
    inicio = time.perf_counter()
    resultado = fibonacci_definicao(n)
    fim = time.perf_counter()
    return resultado, fim - inicio

def main():
    valores = [5, 15, 30]
    
    print("=" * 60)
    print("FIBONACCI - VERSAO 1: PELA DEFINICAO")
    print("=" * 60)
    print(f"{'n':<6} | {'F(n)':<15} | {'Tempo (s)':<18} | {'Tempo (ms)'}")
    print("-" * 60)
    
    for n in valores:
        res, t = medir_tempo(n)
        print(f"{n:<6} | {res:<15} | {t:<18.8f} | {t * 1000:.4f} ms")
    
    print("=" * 60)

if __name__ == "__main__":
    main()
