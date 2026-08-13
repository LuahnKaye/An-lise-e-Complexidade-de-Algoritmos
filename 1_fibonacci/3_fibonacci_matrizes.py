import time
import sys

# Ajuste para permitir calcular valores gigantescos (F(5.000.000) tem mais de 1 milhao de digitos)
sys.set_int_max_str_digits(5_000_000)

# Multiplica duas matrizes 2x2. Fundamental para a algebra linear do calculo
def multiplicar_matrizes(A, B):
    return [
        [
            A[0][0] * B[0][0] + A[0][1] * B[1][0], # Linha 0, Coluna 0
            A[0][0] * B[0][1] + A[0][1] * B[1][1]  # Linha 0, Coluna 1
        ],
        [
            A[1][0] * B[0][0] + A[1][1] * B[1][0], # Linha 1, Coluna 0
            A[1][0] * B[0][1] + A[1][1] * B[1][1]  # Linha 1, Coluna 1
        ]
    ]

# Eleva uma matriz M a potencia 'exp' utilizando Exponenciacao Rapida (Binary Exponentiation)
# Complexidade O(log n) - o segredo da velocidade desta abordagem
def potencia_matriz(M, exp: int):
    # Matriz Identidade (elemento neutro da multiplicacao de matrizes)
    resultado = [
        [1, 0],
        [0, 1]
    ]
    base = [
        [M[0][0], M[0][1]],
        [M[1][0], M[1][1]]
    ]
    
    # Em vez de multiplicar N vezes (O(n)), dividimos o expoente por 2 e elevamos a base ao quadrado
    # Isso reduz drasticamente o numero de operacoes. Ex: 2^10 = (2^2)^5
    while exp > 0:
        if exp % 2 == 1:
            # Se o expoente atual for impar, acumulamos a base no resultado
            resultado = multiplicar_matrizes(resultado, base)
        # Quadramos a base e reduzimos o expoente pela metade
        base = multiplicar_matrizes(base, base)
        exp //= 2
        
    return resultado

# Versao 3: Calculo usando a relacao matricial de Fibonacci
# Complexidade: Tempo O(log n) e Espaco O(1)
# Baseado na propriedade: [1 1 ; 1 0]^n = [F(n+1) F(n) ; F(n) F(n-1)]
def fibonacci_matriz(n: int) -> int:
    if n <= 0: return 0
    if n == 1: return 1
    
    # Matriz M geradora de Fibonacci
    M = [
        [1, 1],
        [1, 0]
    ]
    
    # Elevamos a matriz M a potencia n em tempo logaritmico
    Mn = potencia_matriz(M, n)
    
    # Retornamos o elemento F(n) que estara na linha 0, coluna 1
    return Mn[0][1]

def medir_tempo(n: int):
    inicio = time.perf_counter()
    resultado = fibonacci_matriz(n)
    fim = time.perf_counter()
    return resultado, fim - inicio

def main():
    valores = [5, 15, 30]
    
    print("=" * 60)
    print("FIBONACCI - VERSAO 3: UTILIZANDO MATRIZES O(log n)")
    print("=" * 60)
    print(f"{'n':<6} | {'F(n)':<15} | {'Tempo (s)':<18} | {'Tempo (ms)'}")
    print("-" * 60)
    
    for n in valores:
        res, t = medir_tempo(n)
        print(f"{n:<6} | {res:<15} | {t:<18.8f} | {t * 1000:.4f} ms")
    
    print("=" * 60)
    print("\nTestes com valores GIGANTESCOS (mostrando o poder do O(log n)):")
    # Gracas ao O(log n), podemos calcular n = 5 milhoes rapidamente!
    for n in [1000, 10000, 100000, 1000000, 5000000]:
        res, t = medir_tempo(n)
        # Ao inves de converter para string (que trava o python), calculamos a qtd de digitos usando logaritmo base 10
        bits = res.bit_length()
        digitos = int(bits * 0.30103) + 1 
        print(f"F({n}) calculado em {t:.4f} s (~{digitos} digitos)")

if __name__ == "__main__":
    main()
