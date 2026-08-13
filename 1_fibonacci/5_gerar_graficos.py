import time
import os
import matplotlib.pyplot as plt

# Garante que os graficos serao salvos na mesma pasta do script, nao importando de onde ele for executado
_DIR = os.path.dirname(os.path.abspath(__file__))

# As 3 funcoes de Fibonacci que estao sendo comparadas visualmente

def fib_definicao(n: int) -> int:
    # O(2^n) - Recursivo ingênuo
    if n <= 0: return 0
    if n == 1: return 1
    return fib_definicao(n - 1) + fib_definicao(n - 2)

def fib_intermediarios(n: int) -> int:
    # O(n) - Iterativo
    if n <= 0: return 0
    if n == 1: return 1
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
    # O(log n) - Matrizes
    if n <= 0: return 0
    if n == 1: return 1
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
    func(n)
    fim = time.perf_counter()
    return (fim - inicio) * 1000  # Retorna em milissegundos para os graficos

def main():
    print("Gerando dados para os graficos (isso pode levar alguns segundos)...")
    
    # ---------------------------------------------------------
    # EXPERIMENTO 1: Valores pequenos (n=1 até 34)
    # Mostra a explosao exponencial da recursao O(2^n)
    # ---------------------------------------------------------
    ns_pequenos = list(range(1, 35))
    tempos_def = [medir(fib_definicao, n) for n in ns_pequenos]
    tempos_int_pequenos = [medir(fib_intermediarios, n) for n in ns_pequenos]
    tempos_mat_pequenos = [medir(fib_matrizes, n) for n in ns_pequenos]

    # ---------------------------------------------------------
    # EXPERIMENTO 2: Valores grandes (n=10k até 400k)
    # Compara a Linear O(n) vs Logaritmica O(log n) - O(2^n) ficaria travado aqui
    # ---------------------------------------------------------
    ns_grandes = [10000, 50000, 100000, 200000, 300000, 400000]
    tempos_int_grandes = [medir(fib_intermediarios, n) for n in ns_grandes]
    tempos_mat_grandes = [medir(fib_matrizes, n) for n in ns_grandes]

    # --- GERACAO DOS GRAFICOS (Matplotlib) ---
    plt.style.use('default')
    
    # Gráfico 1: Escala Linear (Dois paineis, um pra peq e outro pra gdes valores)
    fig, axes = plt.subplots(1, 2, figsize=(15, 6), dpi=100)
    
    # Painel Esquerdo: Explosao exponencial da versao O(2^n)
    axes[0].plot(ns_pequenos, tempos_def, 'o-', color='#e74c3c', linewidth=2.5, markersize=4, label='Definição O(2^n)')
    axes[0].plot(ns_pequenos, tempos_int_pequenos, '-', color='#3498db', linewidth=2.5, label='Intermediarios O(n)')
    axes[0].plot(ns_pequenos, tempos_mat_pequenos, '-', color='#2ecc71', linewidth=2.5, label='Matrizes O(log n)')
    axes[0].set_title('Fibonacci: n = 1 até 34 (Escala Linear)', fontsize=14, fontweight='bold')
    axes[0].set_xlabel('Valor de n', fontsize=12)
    axes[0].set_ylabel('Tempo de Execução (ms)', fontsize=12)
    axes[0].grid(True, linestyle='--', alpha=0.6)
    axes[0].legend(fontsize=11)

    # Painel Direito: Batalha de Titãs (Linear vs Log) para Grandes Valores
    axes[1].plot(ns_grandes, [t/1000 for t in tempos_int_grandes], 's-', color='#3498db', linewidth=2.5, label='Intermediarios O(n)')
    axes[1].plot(ns_grandes, [t/1000 for t in tempos_mat_grandes], '^-', color='#2ecc71', linewidth=2.5, label='Matrizes O(log n)')
    axes[1].set_title('Grandes Valores: Iterativo vs Matrizes', fontsize=14, fontweight='bold')
    axes[1].set_xlabel('Valor de n', fontsize=12)
    axes[1].set_ylabel('Tempo de Execução (segundos)', fontsize=12)
    axes[1].grid(True, linestyle='--', alpha=0.6)
    axes[1].legend(fontsize=11)

    plt.tight_layout()
    plt.savefig(os.path.join(_DIR, 'graficos_fibonacci.png'), dpi=300)
    print("Grafico salvo com sucesso: graficos_fibonacci.png")

    # Gráfico 2: Escala Logaritmica
    # Excelente para mostrar a complexidade de algoritmos de categorias muito distantes
    fig2, ax2 = plt.subplots(figsize=(9, 6))
    ax2.plot(ns_pequenos, tempos_def, 'o-', color='#e74c3c', linewidth=2, markersize=4, label='Definição O(2^n)')
    ax2.plot(ns_pequenos, tempos_int_pequenos, 's-', color='#3498db', linewidth=2, markersize=4, label='Intermediarios O(n)')
    ax2.plot(ns_pequenos, tempos_mat_pequenos, '^-', color='#2ecc71', linewidth=2, markersize=4, label='Matrizes O(log n)')
    
    ax2.set_yscale('log') # Transforma o eixo Y em logaritmico!
    ax2.set_title('Fibonacci: Comparativo em Escala Logarítmica', fontsize=14, fontweight='bold')
    ax2.set_xlabel('Valor de n', fontsize=12)
    ax2.set_ylabel('Tempo de Execução (ms) - Escala Log', fontsize=12)
    ax2.grid(True, which="both", ls="--", alpha=0.5)
    ax2.legend(fontsize=11)
    
    plt.tight_layout()
    plt.savefig(os.path.join(_DIR, 'grafico_escala_log.png'), dpi=300)
    print("Grafico em escala logaritmica salvo com sucesso: grafico_escala_log.png")
    
    print("\nExibindo graficos na tela (feche as janelas para finalizar)...")
    plt.show()

if __name__ == "__main__":
    main()
