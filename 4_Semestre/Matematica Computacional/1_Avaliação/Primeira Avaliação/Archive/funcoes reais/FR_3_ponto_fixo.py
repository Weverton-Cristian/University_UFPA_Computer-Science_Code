import math

# Função f(x) = x^3-9x+3
def f(x):
    return x**3 -9*x + 3

# Função phi(x) para reescrever f(x) = 0 em x = phi(x)
def phi(x):
    return (x**3 + 3) / 9 # Devemos calcular comparando f(x) = 0 e isolar um x.

# Método do ponto fixo
def pontoFixo(phi, f, x0, epsilon1, epsilon2):
    """
    Método do ponto fixo para encontrar raízes de f(x) = 0 usando x = phi(x).
    
    Parâmetros:
    phi: Função de iteração phi(x).
    f: Função f(x), cuja raiz queremos encontrar.
    x0: Aproximação inicial.
    epsilon1: Precisão para |f(x)|.
    epsilon2: Precisão para |x1 - x0|.
    
    Retorna:
    - x_barra: Aproximação final da raiz.
    - iteracoes: Número de iterações realizadas.
    """
    # Passo 2: Verifica se |f(x0)| < epsilon1
    if abs(f(x0)) < epsilon1:
        return x0,  0 # x̄ = x0, fim
    
    # Inicializa contador de iterações
    k = 1
    
    while True:
        # Passo 4: Calcula x1 = phi(x0)
        x1 = phi(x0)
        
        # Passo 5: Condições de parada
        if abs(f(x1)) < epsilon1 or abs(x1 - x0) < epsilon2:
            return x1, k  # x̄ = x1, fim
        
        # Passo 6: Atualiza x0 para x1
        x0 = x1
        
        # Passo 7: Incrementa o contador de iterações
        k += 1

# Parâmetros do teste
x0 = 1.0  # Aproximação inicial
epsilon1 = 1e-4 #  Precisão para |f(x)|
epsilon2 = 1e-4 #  Precisão para |x1 - x0|

# Executa o método do ponto fixo
raiz, iteracoes = pontoFixo(phi, f, x0, epsilon1, epsilon2)

# Exibe os resultados
print(f"Aproximação da raiz: x̄ = {raiz:.9f}")
print(f"f(x̄) = {f(raiz):.2e}")
print(f"Número de iterações: {iteracoes}")

