import math

# Exemplo de função f(x)
def f(x):
    return x**math.log(x) + x**2 - x**3 * math.sin(x)  # Exemplo de função (pode ser modificada)

# Função que gera a tabela de f(x) e o sinal de f(x)
def tabela_com_sinal(f, a, b, passo):
    print(f"{'x':<10} {'f(x)':<15} {'Sinal(f(x))'}")  # Cabeçalho da tabela
    x = a
    while x <= b:
        fx = f(x)
        sinal = "Positivo" if fx > 0 else "Negativo" if fx < 0 else "Zero"
        print(f"{x:<10} {fx:<15} {sinal}")  # Imprime o valor de f(x) e seu sinal
        x += passo  # Incrementa o valor de x pelo passo

# Definindo o intervalo [a, b] e o passo
a = 1  # Início do intervalo
b = 20   # Fim do intervalo
passo = 0.5  # Passo para avaliar os pontos

# Gerando a tabela
tabela_com_sinal(f, a, b, passo)
