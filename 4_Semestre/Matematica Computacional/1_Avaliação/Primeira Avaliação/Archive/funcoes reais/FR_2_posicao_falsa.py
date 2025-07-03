# Função que implementa o método da posição falsa
def posicaoFalsa(f, a, b, epsilon1, epsilon2):
    """
    Implementa o método da posição falsa para encontrar uma raiz no intervalo [a, b].
    Retorna uma lista com os resultados de cada iteração.
    """
    iteracao = 1
    resultados = []  # Para armazenar resultados de cada iteração
    
    # Garantir que f(a) e f(b) têm sinais opostos
    if f(a) * f(b) > 0:
        print(f"Intervalo [{a}, {b}] não é válido. f(a) e f(b) têm o mesmo sinal.")
        return None  # Retorna None para indicar que não há raiz neste intervalo

    while True:
        # Calcula x usando o método da posição falsa
        x = (a * f(b) - b * f(a)) / (f(b) - f(a))  # Cálculo do ponto X
        fx = f(x)  # Calcula f(x)
        intervalo = b - a  # Tamanho do intervalo atual
        
        # Armazena os resultados da iteração atual
        resultados.append((iteracao, x, fx, intervalo))
        
        # Verifica se |f(x)| < epsilon2 ou (b - a) < epsilon1
        if abs(fx) < epsilon2 or intervalo < epsilon1:  # Parar quando atingir a precisão desejada
            break
        
        # Atualiza os extremos do intervalo
        if f(a) * fx > 0:
            a = x  # Ajusta o extremo esquerdo
        else:
            b = x  # Ajusta o extremo direito
        
        iteracao += 1  # Incrementa o contador de iterações
    
    return resultados

# Função de teste: f(x) = x³ - 9x + 3
def funcao(x):
    return x**3 - 9*x + 3

# Lista de intervalos a serem testados
intervalos = [(0, 1), (2, 3), (-3, -2)]  # Exemplo com 3 intervalos possíveis

# Precisões
epsilon1 = epsilon2 = 5e-4  # Precisão do intervalo e de f(x)

# Testa todos os intervalos
for i, (a, b) in enumerate(intervalos, start=1):
    print(f"\n>>> Testando intervalo {i}: [{a}, {b}]")

    resultados = posicaoFalsa(funcao, a, b, epsilon1, epsilon2)

    if resultados:  # Apenas imprime se um resultado válido foi encontrado
        for iteracao, x, fx, intervalo in resultados:
            print(f"Iteração {iteracao}: x = {x:.9f}, f(x) = {fx:.9e}, b - a = {intervalo:.9f}")

        # Resultado final
        x_final, fx_final, _ = resultados[-1][1:]
        print(f"\nRaiz encontrada em x̄ = {x_final:.9f}, f(x̄) = {fx_final:.2e}")
