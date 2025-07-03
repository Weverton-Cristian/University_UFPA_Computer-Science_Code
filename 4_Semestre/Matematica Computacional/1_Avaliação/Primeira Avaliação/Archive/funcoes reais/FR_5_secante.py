def f(x):
    # Exemplo de função f(x). Modifique conforme a sua necessidade.
    return x**3 - x - 2  # Exemplo: f(x) = x^3 - x - 2

def secante(x0, x1, epsilon1, epsilon2, max_iter=100):
    # Inicialização
    k = 1
    
    # Passo 2: Verificar o critério para x0
    if abs(f(x0)) < epsilon1:
        print(f"Solução encontrada: x = {x0}, f(x) = {f(x0)}, Iterações: {k}")
        return x0, k
    
    # Passo 3: Verificar o critério para x1
    if abs(f(x1)) < epsilon1 or abs(x1 - x0) < epsilon2:
        print(f"Solução encontrada: x = {x1}, f(x) = {f(x1)}, Iterações: {k}")
        return x1, k

    # Iteração principal
    while k <= max_iter:
        # Passo 5: Calcular x2 usando a fórmula
        f_x0 = f(x0)
        f_x1 = f(x1)
        
        if f_x1 - f_x0 == 0:  # Para evitar divisão por zero
            print("Divisão por zero! Tente usar aproximações diferentes.")
            return None, k
        
        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        
        # Passo 6: Verificar os critérios de parada
        if abs(f(x2)) < epsilon1 or abs(x2 - x1) < epsilon2:
            print(f"Solução encontrada: x = {x2}, f(x) = {f(x2)}, Iterações: {k}")
            return x2, k
        
        # Passo 7: Atualizar x0 e x1 para a próxima iteração
        x0 = x1
        x1 = x2
        k += 1
        
    print("Número máximo de iterações atingido sem convergência.")
    return None, k

# Dados iniciais
x0 = 1.0  # Aproximação inicial 1
x1 = 2.0  # Aproximação inicial 2
epsilon1 = 1e-8  # Precisão para f(x)
epsilon2 = 1e-8  # Precisão para |x2 - x1|

# Chamando o método iterativo
solucao, iteracoes = secante(x0, x1, epsilon1, epsilon2)

# Testar o resultado na função
if solucao is not None:
    resultado = f(solucao)
    print(f"\nValor da função f(x) na solução encontrada x = {solucao:.9f} é f(x) = {resultado:.9e}")
    print(f"Número de iterações: {iteracoes}")
else:
    print("\nSolução não encontrada.")
