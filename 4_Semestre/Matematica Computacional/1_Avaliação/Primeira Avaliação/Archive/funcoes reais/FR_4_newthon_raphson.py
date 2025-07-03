def newthonRaphson(f, f_derivative, x0, epsilon1, epsilon2):
    """
    Método de Newton-Raphson para encontrar raízes de f(x) = 0.
    
    Parâmetros:
    - f: Função f(x), cuja raiz queremos encontrar.
    - f_derivative: Derivada de f(x).
    - x0: Aproximação inicial.
    - epsilon1: Precisão para |f(x)|.
    - epsilon2: Precisão para |x1 - x0|.
    
    Retorna:
    - x_barra: Aproximação final da raiz.
    - iteracoes: Número de iterações realizadas.
    """
    # Passo 2: Verifica se |f(x0)| < epsilon1
    if abs(f(x0)) < epsilon1:
        return x0, 0  # x̄ = x0, fim
    
    # Inicializa contador de iterações
    k = 1
    
    while True:
        # Verifica se a derivada é zero (para evitar divisão por zero)
        if f_derivative(x0) == 0:
            raise ValueError("Derivada é zero. Método de Newton-Raphson não pode continuar.")
        
        # Passo 4: Calcula x1 usando a fórmula de Newton-Raphson
        x1 = x0 - f(x0) / f_derivative(x0)
        
        # Passo 5: Verifica condições de parada
        if abs(f(x1)) < epsilon1 or abs(x1 - x0) < epsilon2:
            return x1, k  # x̄ = x1, fim
        
        # Passo 6: Atualiza x0 para x1
        x0 = x1
        
        # Passo 7: Incrementa o contador de iterações
        k += 1


# EXEMPLO COMPLETO
# Função f(x) = x^2 - 2
def f(x):
    return x**2 - 2

# Derivada de f(x), f'(x) = 2x
def f_derivative(x):
    return 2 * x

# Definições do exemplo
x0 = 1.0           # Aproximação inicial
epsilon1 = 1e-6    # Precisão para |f(x)|
epsilon2 = 1e-6    # Precisão para |x1 - x0|

# Executa o método de Newton-Raphson
try:
    raiz, iteracoes = newthonRaphson(f, f_derivative, x0, epsilon1, epsilon2)
    print("=== Método de Newton-Raphson ===")
    print(f"Aproximação da raiz: x̄ = {raiz:.9f}")
    print(f"f(x̄) = {f(raiz):.2e}")
    print(f"Número de iterações: {iteracoes}")
except ValueError as e:
    print(f"Erro: {e}")
