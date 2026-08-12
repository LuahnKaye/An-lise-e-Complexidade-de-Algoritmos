import time
import matplotlib.pyplot as plt

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

def medir(func, n, repeticoes=1):
    inicio = time.perf_counter()
    for _ in range(repeticoes):
        func(n)
    fim = time.perf_counter()
    return (fim - inicio) / repeticoes

def gerar_graficos():
    print("Coletando tempos para valores pequenos/medios (n = 1 a 34)...")
    valores_n1 = list(range(1, 35))
    tempos_def = []
    tempos_inter1 = []
    tempos_mat1 = []

    for n in valores_n1:
        tempos_def.append(medir(fib_definicao, n) * 1000)
        tempos_inter1.append(medir(fib_intermediarios, n, repeticoes=100) * 1000)
        tempos_mat1.append(medir(fib_matrizes, n, repeticoes=100) * 1000)

    print("Coletando tempos para valores grandes (n = 10.000 a 400.000)...")
    valores_n2 = [1000, 10000, 25000, 50000, 100000, 200000, 300000, 400000]
    tempos_inter2 = []
    tempos_mat2 = []

    for n in valores_n2:
        tempos_inter2.append(medir(fib_intermediarios, n))
        tempos_mat2.append(medir(fib_matrizes, n))

    fig, axes = plt.subplots(1, 2, figsize=(15, 6))

    axes[0].plot(valores_n1, tempos_def, label='Definicao O(2^n)', color='#e74c3c', linewidth=2.5, marker='o', markersize=4)
    axes[0].plot(valores_n1, tempos_inter1, label='Intermediarios O(n)', color='#3498db', linewidth=2.5)
    axes[0].plot(valores_n1, tempos_mat1, label='Matrizes O(log n)', color='#2ecc71', linewidth=2.5)
    axes[0].set_title('Comparativo Geral: n = 1 ate 34 (Escala Linear)', fontsize=13, fontweight='bold')
    axes[0].set_xlabel('Valor de n', fontsize=11)
    axes[0].set_ylabel('Tempo de Execucao (ms)', fontsize=11)
    axes[0].grid(True, linestyle='--', alpha=0.6)
    axes[0].legend(fontsize=11)

    axes[1].plot(valores_n2, tempos_inter2, label='Intermediarios O(n)', color='#3498db', linewidth=2.5, marker='s', markersize=5)
    axes[1].plot(valores_n2, tempos_mat2, label='Matrizes O(log n)', color='#2ecc71', linewidth=2.5, marker='^', markersize=6)
    axes[1].set_title('Desempenho com Grandes Numeros: Intermediarios vs Matrizes', fontsize=13, fontweight='bold')
    axes[1].set_xlabel('Valor de n', fontsize=11)
    axes[1].set_ylabel('Tempo de Execucao (segundos)', fontsize=11)
    axes[1].grid(True, linestyle='--', alpha=0.6)
    axes[1].legend(fontsize=11)

    plt.tight_layout()
    plt.savefig('graficos_fibonacci.png', dpi=300)
    print("Grafico salvo com sucesso: graficos_fibonacci.png")

    fig2, ax2 = plt.subplots(figsize=(9, 6))
    ax2.plot(valores_n1, tempos_def, label='Definicao O(2^n)', color='#e74c3c', linewidth=2.5, marker='o')
    ax2.plot(valores_n1, tempos_inter1, label='Intermediarios O(n)', color='#3498db', linewidth=2.5, marker='s')
    ax2.plot(valores_n1, tempos_mat1, label='Matrizes O(log n)', color='#2ecc71', linewidth=2.5, marker='^')
    ax2.set_yscale('log')
    ax2.set_title('Comparativo em Escala Logaritmica (n = 1 ate 34)', fontsize=13, fontweight='bold')
    ax2.set_xlabel('Valor de n', fontsize=11)
    ax2.set_ylabel('Tempo de Execucao (ms) - Escala Log', fontsize=11)
    ax2.grid(True, which='both', linestyle='--', alpha=0.6)
    ax2.legend(fontsize=11)
    
    plt.tight_layout()
    plt.savefig('grafico_escala_log.png', dpi=300)
    print("Grafico em escala logaritmica salvo com sucesso: grafico_escala_log.png")
    
    print("\nExibindo graficos na tela...")
    plt.show()

if __name__ == "__main__":
    gerar_graficos()
