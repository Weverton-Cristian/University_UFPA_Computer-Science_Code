# Discente: Weverton Cristian de Sousa Duarte

from collections import defaultdict # Importa defaultdict da biblioteca collections.


grafo = {  # Grafo como dicionário de listas de adjacência:
    "A": ["B", "D"],
    "B": ["C", "A"],
    "C": ["D", "A"],
    "D": ["B", "C"]
}

# Variáveis globais para controle do ciclo
color = {}      #armazena o estado de cada vértice (WHITE, GRAY, BLACK).
pi = {}         #armazena o predecessor de cada vértice na árvore DFS.
ciclo = []      #vai guardar o ciclo encontrado.

# Flag para parar a DFS assim que encontrar o ciclo
ciclo_encontrado = False

def dfs(grafo):
    global ciclo_encontrado # global para poder modificar a varável global cicloencontrado
    for u in grafo:
        color[u] = 'WHITE'  # Inicializa todos os vértices como não visitados (WHITE).
        pi[u] = None        # porque no começo ninguém tem predecessor.

    for u in grafo:
        if color[u] == 'WHITE':     # Se ele não foi visitado (WHITE)
            dfs_visit(grafo, u)     # Chama dfs_visit para fazer a busca em profundidade a partir dele.
            if ciclo_encontrado:    # Se encontrar um ciclo, para tudo (break).
                break

def dfs_visit(grafo, u):
    global ciclo_encontrado, ciclo
    color[u] = 'GRAY'
    for v in grafo[u]:
        if color[v] == 'WHITE':
            pi[v] = u
            dfs_visit(grafo, v)
            if ciclo_encontrado:
                return
        elif color[v] == 'GRAY' and v != pi[u]:
            # Encontrou um ciclo!
            ciclo_encontrado = True
            reconstruir_ciclo(u, v)
            return
    color[u] = 'BLACK'

def reconstruir_ciclo(u, v):
    # Reconstrói o ciclo de u até v usando pi
    caminho = [v]
    while u != v:
        caminho.append(u)
        u = pi[u]
    caminho.append(v)  # Fecha o ciclo
    caminho.reverse()
    global ciclo
    ciclo = caminho

# Executa o DFS para procurar ciclo
dfs(grafo)

if ciclo_encontrado:
    print("Ciclo encontrado:", ciclo)
else:
    print("Nenhum ciclo encontrado.")
