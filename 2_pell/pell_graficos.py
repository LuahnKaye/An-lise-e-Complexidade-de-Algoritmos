import time
import os
import matplotlib.pyplot as plt

_DIR = os.path.dirname(os.path.abspath(__file__))

# As 3 funcoes de Pell para plotagem

def pell_definicao(n: int) -> int:
    # O((1+√2)^n) - Extremamente lento
    if n <= 0: return 0
    if n == 1: return 1
    return 2 * pell_definicao(n - 1) + pell_definicao(n - 2)

def pell_iterativo(n: int) -> int:
    # O(n) - Linear
    if n <= 0: return 0
    if n == 1: return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, 2 * b + a
    return b

def _mult_matrizes(A, B):
    return [
        [A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
        [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]
    ]

def pell_matrizes(n: int) -> int:
    # O(log n) - Logaritmico
    if n <= 0: return 0
    if n == 1: return 1
    res = [[1, 0], [0, 1]]
    base = [[2, 1], [1, 0]]
    exp = n
    while exp > 0:
        if exp % 2 == 1:
            res = _mult_matrizes(res, base)
        base = _mult_matrizes(base, base)
        exp //= 2
    return res[0][1]

def medir(func, n):
    inicio = time.perf_counter()
    func(n)
    fim = time.perf_counter()
    return (fim - inicio) * 1000

def main():
    print("Gerando dados para os graficos (isso pode levar alguns segundos)...")
    
    # ---------------------------------------------------------
    # EXPERIMENTO 1: Valores pequenos (n=1 até 26)
    # ---------------------------------------------------------
    ns_pequenos = list(range(1, 27))
    tempos_def = [medir(pell_definicao, n) for n in ns_pequenos]
    tempos_int_pequenos = [medir(pell_iterativo, n) for n in ns_pequenos]
    tempos_mat_pequenos = [medir(pell_matrizes, n) for n in ns_pequenos]

    # ---------------------------------------------------------
    # EXPERIMENTO 2: Valores grandes (n=50k até 300k)
    # ---------------------------------------------------------
    ns_grandes = [1000, 10000, 25000, 50000, 100000, 200000, 300000]
    tempos_int_grandes = [medir(pell_iterativo, n) for n in ns_grandes]
    tempos_mat_grandes = [medir(pell_matrizes, n) for n in ns_grandes]

    # --- GERACAO DOS GRAFICOS ---
    plt.style.use('default')
    fig, axes = plt.subplots(1, 2, figsize=(15, 6), dpi=100)
    
    # Painel Esquerdo
    axes[0].plot(ns_pequenos, tempos_def, 'o-', color='#e74c3c', linewidth=2.5, markersize=4, label='Definicao O((1+√2)^n)')
    axes[0].plot(ns_pequenos, tempos_int_pequenos, '-', color='#3498db', linewidth=2.5, label='Iterativo O(n)')
    axes[0].plot(ns_pequenos, tempos_mat_pequenos, '-', color='#2ecc71', linewidth=2.5, label='Matrizes O(log n)')
    axes[0].set_title('Numeros de Pell: n = 1 ate 26 (Escala Linear)', fontsize=14, fontweight='bold')
    axes[0].set_xlabel('Valor de n', fontsize=12)
    axes[0].set_ylabel('Tempo de Execucao (ms)', fontsize=12)
    axes[0].grid(True, linestyle='--', alpha=0.6)
    axes[0].legend(fontsize=11)

    # Painel Direito
    axes[1].plot(ns_grandes, [t/1000 for t in tempos_int_grandes], 's-', color='#3498db', linewidth=2.5, label='Iterativo O(n)')
    axes[1].plot(ns_grandes, [t/1000 for t in tempos_mat_grandes], '^-', color='#2ecc71', linewidth=2.5, label='Matrizes O(log n)')
    axes[1].set_title('Numeros de Pell para Grandes Valores: Iterativo vs Matrizes', fontsize=14, fontweight='bold')
    axes[1].set_xlabel('Valor de n', fontsize=12)
    axes[1].set_ylabel('Tempo de Execucao (segundos)', fontsize=12)
    axes[1].grid(True, linestyle='--', alpha=0.6)
    axes[1].legend(fontsize=11)

    plt.tight_layout()
    plt.savefig(os.path.join(_DIR, 'graficos_pell.png'), dpi=300)
    print("Grafico salvo com sucesso: graficos_pell.png")
    
    print("\nExibindo graficos na tela...")
    plt.show()

if __name__ == "__main__":
    main()
