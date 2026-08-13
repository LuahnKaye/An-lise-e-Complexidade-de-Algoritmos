import time
import os
import matplotlib.pyplot as plt

_DIR = os.path.dirname(os.path.abspath(__file__))

# As 3 funcoes de Catalan para plotagem

def catalan_recursivo(n: int) -> int:
    # O(4^n)
    if n <= 0: return 1
    soma = 0
    for i in range(n):
        soma += catalan_recursivo(i) * catalan_recursivo(n - 1 - i)
    return soma

def catalan_dp(n: int) -> int:
    # O(n^2)
    if n <= 0: return 1
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        for j in range(i):
            dp[i] += dp[j] * dp[i - 1 - j]
    return dp[n]

def catalan_analitico(n: int) -> int:
    # O(n)
    if n <= 0: return 1
    c = 1
    for i in range(1, n + 1):
        c = (c * 2 * (2 * i - 1)) // (i + 1)
    return c

def medir(func, n):
    inicio = time.perf_counter()
    func(n)
    fim = time.perf_counter()
    return (fim - inicio) * 1000

def main():
    print("Gerando dados para os graficos (isso pode levar alguns segundos)...")
    
    # ---------------------------------------------------------
    # EXPERIMENTO 1: Valores pequenos (n=1 até 15)
    # A recursao pura de Catalan entra em colapso extremamente rapido
    # ---------------------------------------------------------
    ns_pequenos = list(range(1, 16))
    tempos_def = [medir(catalan_recursivo, n) for n in ns_pequenos]
    tempos_dp_pequenos = [medir(catalan_dp, n) for n in ns_pequenos]
    tempos_an_pequenos = [medir(catalan_analitico, n) for n in ns_pequenos]

    # ---------------------------------------------------------
    # EXPERIMENTO 2: Valores grandes (n=50 até 2500)
    # Comparando O(n^2) com O(n)
    # ---------------------------------------------------------
    ns_grandes = [50, 100, 250, 500, 800, 1200, 1600, 2000, 2500]
    tempos_dp_grandes = [medir(catalan_dp, n) for n in ns_grandes]
    tempos_an_grandes = [medir(catalan_analitico, n) for n in ns_grandes]

    # --- GERACAO DOS GRAFICOS ---
    plt.style.use('default')
    fig, axes = plt.subplots(1, 2, figsize=(15, 6), dpi=100)
    
    # Painel Esquerdo: Explosao da recursao (Convolucao)
    axes[0].plot(ns_pequenos, tempos_def, 'o-', color='#e74c3c', linewidth=2.5, markersize=4, label='Recursao Pura O(4^n / n^1.5)')
    axes[0].plot(ns_pequenos, tempos_dp_pequenos, '-', color='#f39c12', linewidth=2.5, label='Prog. Dinamica O(n^2)')
    axes[0].plot(ns_pequenos, tempos_an_pequenos, '-', color='#2ecc71', linewidth=2.5, label='Formula Multiplicativa O(n)')
    axes[0].set_title('Numeros de Catalan: n = 1 ate 15 (Escala Linear)', fontsize=14, fontweight='bold')
    axes[0].set_xlabel('Valor de n', fontsize=12)
    axes[0].set_ylabel('Tempo de Execucao (ms)', fontsize=12)
    axes[0].grid(True, linestyle='--', alpha=0.6)
    axes[0].legend(fontsize=11)

    # Painel Direito: Distancia enorme entre Quadraticos (n^2) e Lineares (n)
    axes[1].plot(ns_grandes, [t/1000 for t in tempos_dp_grandes], 's-', color='#f39c12', linewidth=2.5, label='Prog. Dinamica O(n^2)')
    axes[1].plot(ns_grandes, [t/1000 for t in tempos_an_grandes], '^-', color='#2ecc71', linewidth=2.5, label='Formula Multiplicativa O(n)')
    axes[1].set_title('Numeros de Catalan para Grandes Valores: DP vs Multiplicativo', fontsize=14, fontweight='bold')
    axes[1].set_xlabel('Valor de n', fontsize=12)
    axes[1].set_ylabel('Tempo de Execucao (segundos)', fontsize=12)
    axes[1].grid(True, linestyle='--', alpha=0.6)
    axes[1].legend(fontsize=11)

    plt.tight_layout()
    plt.savefig(os.path.join(_DIR, 'graficos_catalan.png'), dpi=300)
    print("Grafico salvo com sucesso: graficos_catalan.png")
    
    print("\nExibindo graficos na tela...")
    plt.show()

if __name__ == "__main__":
    main()
