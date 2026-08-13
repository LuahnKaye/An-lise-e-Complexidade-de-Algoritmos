import time
import os
import matplotlib.pyplot as plt

_DIR = os.path.dirname(os.path.abspath(__file__))

def pell_definicao(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return 2 * pell_definicao(n - 1) + pell_definicao(n - 2)

def pell_iterativo(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, 2 * b + a
    return b

def _mult(A, B):
    return [
        [A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]],
        [A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]]
    ]

def pell_matriz(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1
    res = [[1, 0], [0, 1]]
    base = [[2, 1], [1, 0]]
    exp = n
    while exp > 0:
        if exp % 2 == 1:
            res = _mult(res, base)
        base = _mult(base, base)
        exp //= 2
    return res[0][1]

def medir(func, n, repeticoes=1):
    inicio = time.perf_counter()
    for _ in range(repeticoes):
        func(n)
    fim = time.perf_counter()
    return (fim - inicio) / repeticoes

def gerar_graficos():
    print("Coletando tempos de execucao dos Numeros de Pell...")
    
    valores_n1 = list(range(1, 27))
    tempos_def = []
    tempos_iter1 = []
    tempos_mat1 = []

    for n in valores_n1:
        tempos_def.append(medir(pell_definicao, n) * 1000)
        tempos_iter1.append(medir(pell_iterativo, n, repeticoes=100) * 1000)
        tempos_mat1.append(medir(pell_matriz, n, repeticoes=100) * 1000)

    valores_n2 = [1000, 10000, 25000, 50000, 100000, 200000, 300000]
    tempos_iter2 = []
    tempos_mat2 = []

    for n in valores_n2:
        tempos_iter2.append(medir(pell_iterativo, n))
        tempos_mat2.append(medir(pell_matriz, n))

    fig, axes = plt.subplots(1, 2, figsize=(15, 6))

    axes[0].plot(valores_n1, tempos_def, label='Definicao O((1+√2)^n)', color='#e74c3c', linewidth=2.5, marker='o', markersize=4)
    axes[0].plot(valores_n1, tempos_iter1, label='Iterativo O(n)', color='#3498db', linewidth=2.5)
    axes[0].plot(valores_n1, tempos_mat1, label='Matrizes O(log n)', color='#2ecc71', linewidth=2.5)
    axes[0].set_title('Numeros de Pell: n = 1 ate 26 (Escala Linear)', fontsize=13, fontweight='bold')
    axes[0].set_xlabel('Valor de n', fontsize=11)
    axes[0].set_ylabel('Tempo de Execucao (ms)', fontsize=11)
    axes[0].grid(True, linestyle='--', alpha=0.6)
    axes[0].legend(fontsize=11)

    axes[1].plot(valores_n2, tempos_iter2, label='Iterativo O(n)', color='#3498db', linewidth=2.5, marker='s', markersize=5)
    axes[1].plot(valores_n2, tempos_mat2, label='Matrizes O(log n)', color='#2ecc71', linewidth=2.5, marker='^', markersize=6)
    axes[1].set_title('Numeros de Pell para Grandes Valores: Iterativo vs Matrizes', fontsize=13, fontweight='bold')
    axes[1].set_xlabel('Valor de n', fontsize=11)
    axes[1].set_ylabel('Tempo de Execucao (segundos)', fontsize=11)
    axes[1].grid(True, linestyle='--', alpha=0.6)
    axes[1].legend(fontsize=11)

    plt.tight_layout()
    plt.savefig(os.path.join(_DIR, 'graficos_pell.png'), dpi=300)
    print("Grafico salvo com sucesso: graficos_pell.png")
    
    print("\nExibindo graficos na tela...")
    plt.show()

if __name__ == "__main__":
    gerar_graficos()
