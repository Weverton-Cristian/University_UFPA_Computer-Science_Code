
"""
8) Fazer um programa que resolva o seguinte
problema:
matriz = [
    [X5, 8, 0, 7, 4, 9, 6],
    [3, 1, 3, 1, 3, 3, 4],
    [5, 2, 2, 0, 5, 0, 3],
    [8, 4, 0, 0, 1, 5, 5],
    [0, 9, 0, 8, 4, 9, 3X] O x marca o começo e o final
]

Qual o menos custo para percorrer a matriz, começando do primeiro elemento e indo até o ultimo
se movendo apenas para direita e para baixo.

Obs: identifique cuidadosamente a condição de
parada e os casos especiais de chamada recursiva.

"""
"""
matriz = [
    [x, 8, 0, 7, 4, 9, 6],
    [x, x, 3, 1, 3, 3, 4],
    [5, x, x, 0, 5, 0, 3],
    [8, 4, x, x, x, x, x],
    [0, 9, 0, 8, 4, 9, x]
]
    O caminho mais curto está denotado pelos X, custando um total de 27.
"""

matriz = [
    [5, 8, 0, 7, 4, 9, 6],
    [3, 1, 3, 1, 3, 3, 4],
    [5, 2, 2, 0, 5, 0, 3],
    [8, 4, 0, 0, 1, 5, 5],
    [0, 9, 0, 8, 4, 9, 3]
]

def menor_custo(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    memo = {}

    def custo(i, j):
        # Se estamos fora dos limites da matriz, retorna infinito (não válido)
        if i >= linhas or j >= colunas:
            return float('inf')
        
        # Se chegamos no destino, retorna o custo da célula final
        if i == linhas - 1 and j == colunas - 1:
            return matriz[i][j]
        
        # Memoização: se já calculamos, retorna
        if (i, j) in memo:
            return memo[(i, j)]
        
        # Calcula o menor custo para baixo ou para a direita
        menor_caminho = matriz[i][j] + min(custo(i + 1, j), custo(i, j + 1))
        memo[(i, j)] = menor_caminho
        return menor_caminho

    return custo(0, 0)

print(menor_custo(matriz))  # Saída: menor custo possível