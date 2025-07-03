import math

# Método de Bisseção
def bisseccao(f, intervalos, e):
    for (a, b) in intervalos:
        print(f"\nTestando intervalo [{a}, {b}]")
        i = 0
        ai = a
        bi = b

        # Enquanto a diferença entre os limites do intervalo for maior que a precisão e
        while abs(bi - ai) > e:
            pi = (ai + bi) / 2  # Ponto médio
            print(f"Iteração {i}: a{i}: {ai}, b{i}: {bi}, p{i}: {pi}, f(p{i}): {f(pi)}")
            if f(ai) * f(pi) < 0:
                bi = pi  # A raiz está no intervalo [ai, pi]
            else:
                ai = pi  # A raiz está no intervalo [pi, bi]
            i += 1  # Incrementa o número de iterações

        raiz = (ai + bi) / 2  # A raiz encontrada
        print(f"\nRaiz encontrada no intervalo [{a}, {b}]: {raiz} com f(raiz) = {f(raiz)}")

# Definindo os intervalos a serem testados
intervalos = [
    (1.6, 2.1),
    (4.1, 4.6)
]

# Testando a função f(x) = x^3 - 9x + 3 nos intervalos definidos
bisseccao(lambda x: 1 + 5 * x**2 * math.log(x)*math.sin(x**2) - x**3, intervalos, 0.000000001)

# Caso queira testar outras funções, basta alterar a função e os intervalos
# Exemplo:
# bisseccao(lambda x: math.sqrt(x) - 5 * math.exp(-x), intervalos, 0.000000001)
