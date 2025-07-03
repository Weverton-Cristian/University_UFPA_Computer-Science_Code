
# Discente: Weverton Cristian de Sousa Duarte; 202204940050

# O algoritmo heurístico de Bellmore e neuhauser trata-se de uma estratégia gulosa
# para solucionar o problema do caixeiro viajante(TSP), no entanto esse algoritmo 
# não garante uma solução ótima, entretanto é eficiente para encontrar um caminho viável

# Funcionamento do Algoritmo:

# Primeiro ele começa com o menor ciclo de três vértices

# Insere de maneira iterativa o vértice que ainda não está incluído que causa o ModuleNotFoundErroraumento de custo ao ser inserido entre dois vértices consecutivos do ciclo.

# Repete até que todos os vértices estarem incluídos.

# Após ter o conhecimento, partimos para a implementação:

import numpy as np

class TSP_Bellmore_Neuhauser:
    def __init__(self, distancias):
        self.dist = np.array(distancias)
        self.n = len(distancias)
        self.caminho = []

    def custo_total(self, caminho):
        # Calcula o custo total do ciclo fechado
        custo = 0
        for i in range(len(caminho)):
            custo += self.dist[caminho[i]][caminho[(i + 1) % len(caminho)]]
        return custo

    # Passo 1: Encontrar o ciclo inicial de 3 vértices com menor custo
    def executar(self):
        min_ciclo = None
        min_custo = float('inf')

        for i in range(self.n):
            for j in range(i + 1, self.n):
                for k in range(j + 1, self.n):
                    ciclo = [i, j, k]
                    custo = self.custo_total(ciclo)
                    if custo < min_custo:
                        min_custo = custo
                        min_ciclo = ciclo

        caminho = min_ciclo[:]
        restantes = [v for v in range(self.n) if v not in caminho]

        # Passo 2: Inserir os vértices restantes no melhor lugar
        while restantes:
            melhor_vertice = None
            melhor_pos = None
            menor_aumento = float('inf')

            for v in restantes:
                for i in range(len(caminho)):
                    u = caminho[i]
                    w = caminho[(i + 1) % len(caminho)]
                    aumento = (self.dist[u][v] + self.dist[v][w]) - self.dist[u][w]

                    if aumento < menor_aumento:
                        menor_aumento = aumento
                        melhor_vertice = v
                        melhor_pos = i + 1  # inserir entre u e w

            caminho.insert(melhor_pos, melhor_vertice)
            restantes.remove(melhor_vertice)

        self.caminho = caminho
        return caminho, self.custo_total(caminho)

# Abaixo temos um exemplo de entrada 

# Matriz de distâncias (simétrica)
distancias = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

tsp = TSP_Bellmore_Neuhauser(distancias)
rota, custo = tsp.executar()

print("Rota encontrada:", rota)
print("Custo total:", custo)

# =================================================================================================================

# Abaixo está a explicação de como o algoritmo funciona:

# Matriz de entrada :     0    1    2    3 
#                     0   0   10   15   20
#                     1  10    0   35   25
#                     2  15   35    0   30
#                     3  20   25   30    0

# A matriz acima demonstra as conexoes dos elementos e o custo total de cada um deles

# Passo 1: Encontra o melhor ciclo de tês cidades

# O algoritmo irá realizar calculos para encontrar o menor ciclo, mas abaixo irei demonstrar testando 
# todos os ciclos possiveis 

# Ciclo (0,1,2):
# (0,1,2,0) = 10 + 35 + 15 = 60

# Ciclo (0,1,3):
# (0,1,3,0) = 10 + 25 + 20 = 55 = menor

# Ciclo (0,2,3):
# (0,2,3,0) = 15 + 30 + 20 = 65

# Ciclo (1,2,3):
# (1,2,3,1) = 35 + 30 + 25 = 90

# Portanto, ciclo inicial = [0, 1, 3] com custo 55

# =================================================================================================================

# Passo 2: Inserir o vértice restante (2)
# O algoritmo irá verificar onde a cidade 2 pode ser inserida entre pares consecutivos de [0, 1, 3]:

# Entre 0 e 1:
# 0→2→1 - 0→1 = (15 + 35) - 10 = 40

# Entre 1 e 3:
# 1→2→3 - 1→3 = (35 + 30) - 25 = 40

# Entre 3 e 0:
# 3→2→0 - 3→0 = (30 + 15) - 20 = 25 

# Melhor inserção: entre 3 e 0 → nova rota: [0, 1, 3, 2]

# Portanto temos como caminho final:

# 0 → 1 → 3 → 2 → 0

# =================================================================================================================
