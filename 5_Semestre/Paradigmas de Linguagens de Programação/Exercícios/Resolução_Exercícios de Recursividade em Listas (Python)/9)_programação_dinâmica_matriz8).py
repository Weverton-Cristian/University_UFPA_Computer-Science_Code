"""
9) Acrescente no programa anterior a técnica de
programação dinâmica, guardando os resultados
parciais calculados, a fim de evitar recálculo.

"""

"""
Eztratégia de Progrmação Dinâmica utilizada:
    memoização (top-down) é uma forma de armazenar os resultados parciais
      de chamadas recursivas em um dicionário (memo) para evitar recálculo.
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
    
    memo = {} # Dicionário para armazenar os menores custos já calculados

    def custo(i, j):
        # Verificação de limites da matriz
        if i >= linhas or j >= colunas:
            return float('inf')  # Caminho inválido
        
        # Caso base: chegou no destino
        if i == linhas - 1 and j == colunas - 1:
            return matriz[i][j]

        # Se o resultado já foi calculado, retorna ele (programação dinâmica)
        if (i, j) in memo:
            return memo[(i, j)]

        # Calcula o menor custo a partir da célula atual para os caminhos possíveis
        menor = matriz[i][j] + min(custo(i + 1, j), custo(i, j + 1))

        # Guarda o resultado calculado para uso futuro
        memo[(i, j)] = menor

        return menor

    return custo(0, 0)

print("Menor custo:", menor_custo(matriz))  # Saída: menor custo possível