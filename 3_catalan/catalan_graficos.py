import time
import matplotlib.pyplot as plt

def catalan_recursivo(n: int) -> int:
    if n <= 0:
        return 1
    total = 0
    for i in range(n):
        total += catalan_recursivo(i) * catalan_recursivo(n - 1 - i)
    return total

def catalan_dp(n: int) -> int:
    if n <= 0:
        return 1
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for j in range(i):
            dp[i] += dp[j] * dp[i - 1 - j]
    return dp[n]

def catalan_analitico(n: int) -> int:
    if n <= 0:
        return 1
    c = 1
    for i in range(1, n + 1):
        c = (c * 2 * (2 * i - 1)) // (i + 1)
    return c

def medir(func, n, repeticoes=1):
    inicio = time.perf_counter()
    for _ in range(repeticoes):
        func(n)
    fim = time.perf_counter()
    return (fim - inicio) / repeticoes

def gerar_graficos():
    print("Coletando tempos de execucao dos Numeros de Catalan...")
    
    valores_n1 = list(range(1, 16))
    tempos_rec = []
    tempos_dp1 = []
    tempos_ana1 = []

    for n in valores_n1:
        tempos_rec.append(medir(catalan_recursivo, n) * 1000)
        tempos_dp1.append(medir(catalan_dp, n, repeticoes=100) * 1000)
        tempos_ana1.append(medir(catalan_analitico, n, repeticoes=100) * 1000)

    valores_n2 = [50, 100, 200, 400, 800, 1200, 1600, 2000, 2500]
    tempos_dp2 = []
    tempos_ana2 = []

    for n in valores_n2:
        tempos_dp2.append(medir(catalan_dp, n))
        tempos_ana2.append(medir(catalan_analitico, n))

    fig, axes = plt.subplots(1, 2, figsize=(15, 6))

    axes[0].plot(valores_n1, tempos_rec, label='Recursao Pura O(4^n / n^1.5)', color='#e74c3c', linewidth=2.5, marker='o', markersize=4)
    axes[0].plot(valores_n1, tempos_dp1, label='Prog. Dinamica O(n^2)', color='#f39c12', linewidth=2.5)
    axes[0].plot(valores_n1, tempos_ana1, label='Formula Multiplicativa O(n)', color='#2ecc71', linewidth=2.5)
    axes[0].set_title('Numeros de Catalan: n = 1 ate 15 (Escala Linear)', fontsize=13, fontweight='bold')
    axes[0].set_xlabel('Valor de n', fontsize=11)
    axes[0].set_ylabel('Tempo de Execucao (ms)', fontsize=11)
    axes[0].grid(True, linestyle='--', alpha=0.6)
    axes[0].legend(fontsize=11)

    axes[1].plot(valores_n2, tempos_dp2, label='Prog. Dinamica O(n^2)', color='#f39c12', linewidth=2.5, marker='s', markersize=5)
    axes[1].plot(valores_n2, tempos_ana2, label='Formula Multiplicativa O(n)', color='#2ecc71', linewidth=2.5, marker='^', markersize=6)
    axes[1].set_title('Numeros de Catalan para Grandes Valores: DP vs Multiplicativo', fontsize=13, fontweight='bold')
    axes[1].set_xlabel('Valor de n', fontsize=11)
    axes[1].set_ylabel('Tempo de Execucao (segundos)', fontsize=11)
    axes[1].grid(True, linestyle='--', alpha=0.6)
    axes[1].legend(fontsize=11)

    plt.tight_layout()
    plt.savefig('3_catalan/graficos_catalan.png', dpi=300)
    print("Grafico salvo com sucesso: 3_catalan/graficos_catalan.png")
    
    print("\nExibindo graficos na tela...")
    plt.show()

if __name__ == "__main__":
    gerar_graficos()
