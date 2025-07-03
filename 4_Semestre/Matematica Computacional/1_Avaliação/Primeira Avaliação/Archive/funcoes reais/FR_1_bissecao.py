import math

def bisseccao(f, a, b, e):
    i = 0
    ai = a
    bi = b
    while abs(bi - ai) > e:
        pi = (ai + bi) / 2  # Calcula o ponto médio
        if f(ai) * f(pi) < 0:  # Se os sinais forem opostos, a raiz está no intervalo [ai, pi]
            bi = pi
        else:  # Caso contrário, a raiz está no intervalo [pi, bi]
            ai = pi
        i += 1  # Número de iterações
    return (ai + bi) / 2  # Retorna a melhor estimativa para a raiz

def contar_raizes(f, a, b, passo, e):
    """Conta o número de raízes no intervalo [a, b] com um passo dado e retorna as raízes e seus valores"""
    raiz_count = 0
    raizes = []  # Lista para armazenar as raízes encontradas
    # Divide o intervalo [a, b] em subintervalos de tamanho `passo`
    for i in range(int((b - a) / passo)):
        start = a + i * passo
        end = start + passo
        if f(start) * f(end) < 0:  # Se houver troca de sinais, há uma raiz
            raiz_count += 1
            raiz = bisseccao(f, start, end, e)  # Aplica bisseção no subintervalo para encontrar a raiz
            raizes.append((raiz, f(raiz)))  # Adiciona a raiz e seu valor na função
            print(f"Raiz encontrada no intervalo [{start}, {end}]: {raiz} com f({raiz}) = {f(raiz)}")
    return raiz_count, raizes

# Função fornecida
def f(x):
    return x**math.log(x) + x**2 - x**3 * math.sin(x)

# Contar as raízes da função no intervalo [1, 20], com precisão 10^-9 e passo 0.1
numero_de_raizes, raizes = contar_raizes(f, 1, 20, 0.1, 0.000000001)
print(f"Número de raízes no intervalo [1, 20]: {numero_de_raizes}")
print("Raízes e valores encontrados:")
for raiz, valor in raizes:
    print(f"Raiz: {raiz}, f(Raiz): {valor}")
