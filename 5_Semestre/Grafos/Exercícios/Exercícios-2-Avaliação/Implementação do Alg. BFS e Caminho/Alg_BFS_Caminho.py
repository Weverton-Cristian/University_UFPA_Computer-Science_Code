# Discente: Weverton Cristian de Sousa Duarte 

# Escolhi representar pos listas de adjacência, pois no algoritmo DFS
# as listas são mais eficientes.

# A representação do grafo será feita por dicionario

grafo = {

    "A" : ["B" , "D"],
    "B" : ["C" , "A"],
    "C" : ["D" , "A"],
    "D" : ["B" , "C"]
}

verticeIn = input("Forneça o Vértice Inicial entre A, B, C e D : ")
verticeFin = input("Forneça o Vértice Final entre A, B, C e D : ")

from collections import deque # Deque(filas duplas) da biblioteca collections

def bfs(grafo, s):  # Recebe o dicionário(lista de adjacência) e o vértice inicial
    color = {}      # cores possiveis: ('WHITE', 'GRAY', 'BLACK').
    d = {}          # distancia de s até cada vértice 
    pi = {}         # vértice predecessor 

    for v in grafo.keys():
        color[v] = "WHITE"
        d[v] = float('inf') # inf: definimos a distância como infinito, pois não sabemos a distância.
        pi[v] = None 

    color[s] = 'GRAY'   # Iniciando o vértice inicial 
    d[s] = 0            # Distância dele para ele mesmo 
    pi[s] = None        # None, poi não possui antecessor 

    Q = deque()     # Cria fila 
    Q.append(s)     # Adiciona s na fila

    while Q:  # Enquanto a fila não estiver vazia continue
        u = Q.popleft()                 # Remove o vértice u do começo para explorar os vizinhos
        for v in grafo[u]:              
            if color[v] == 'WHITE':     # Se v ainda não foi visitado (WHITE).
                color[v] = 'GRAY'       # Marca v como GRAY (descoberto, mas ainda não completamente explorado).
                d[v] = d[u] + 1         # Define a distância d[v] como d[u] + 1 (é uma aresta a mais que u).
                pi[v] = u               # Define o predecessor π[v] como u (para reconstruir o caminho depois).
                Q.append(v)
        color[u] = 'BLACK'              # Coloca v na fila para visitar seus vizinhos depois.
    return d, pi 

# Execução do BFS
distancias, predecessores = bfs(grafo, verticeIn)

print(f"Tamanho do caminho de {verticeIn} até o {verticeFin} é : {distancias[verticeFin]}")

# A função abaixo serve paraa reconstruir o caminho feito:

def reconstruir_caminho(predecessores, s, v):
    caminho = []
    while v is not None:
        caminho.insert(0, v)
        v = predecessores[v]
    if caminho[0] == s:
        return caminho
    else:
        return None  # Não existe caminho

caminho = reconstruir_caminho(predecessores, verticeIn, verticeFin)
print(f"Caminho: {caminho}")





