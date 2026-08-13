import time
import sys

# Abordagem de Referencia: Recursao Pura por Convolucao
# Complexidade de Tempo: O(4^n / n^1.5)
# Complexidade de Espaco: O(n) na pilha de recursao
# Esta versao aplica diretamente o somatorio da definicao matematica de Segner:
# C_n = Somatorio(C_i * C_{n-1-i}) para i de 0 ate n-1
def catalan_recursivo(n: int) -> int:
    # Caso base: C_0 = 1, e consideramos C_n <= 0 como 1 por definicao.
    if n <= 0:
        return 1
    
    soma = 0
    # Calcula recursivamente a arvore de possibilidades (Gera MUITA redundancia)
    for i in range(n):
        soma += catalan_recursivo(i) * catalan_recursivo(n - 1 - i)
        
    return soma

def medir_tempo(n: int):
    inicio = time.perf_counter()
    resultado = catalan_recursivo(n)
    fim = time.perf_counter()
    return resultado, fim - inicio

def main():
    # Usamos n muito menores aqui porque a complexidade O(4^n) eh brutal
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
    print("Observacao: Devido ao O(4^n), n=16 em diante ja inviabiliza a execucao rapida.")

if __name__ == "__main__":
    main()
