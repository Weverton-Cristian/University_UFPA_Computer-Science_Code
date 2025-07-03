class GrafoMatriz:
    def __init__(self, num_vertices):
        # Inicializa o número de vértices
        self.num_vertices = num_vertices
        # Cria uma matriz num_vertices x num_vertices preenchida com zeros
        # Cada linha representa um vértice, e cada coluna indica se há conexão com outro vértice
        self.matriz = [[0] * num_vertices for _ in range(num_vertices)]

    def adicionar_aresta(self, u, v):
        # Adiciona uma aresta entre os vértices u e v
        self.matriz[u][v] = 1  # Conecta u em v
        self.matriz[v][u] = 1  # Conecta v em u (grafo não-direcionado)

    def imprimir_matriz(self):
        # Imprime a matriz de adjacência linha por linha
        for linha in self.matriz:
            print(linha)

    def grau_vertice(self, v):
        # O grau de um vértice é o número de conexões (arestas)
        # Aqui, somamos todos os valores da linha correspondente ao vértice v
        return sum(self.matriz[v])


# Exemplo de uso
g = GrafoMatriz(5)  # Cria um grafo com 5 vértices
g.adicionar_aresta(0, 1)  # Adiciona aresta entre 0 e 1
g.adicionar_aresta(0, 2)  # Adiciona aresta entre 0 e 2
g.adicionar_aresta(3, 4)  # Adiciona aresta entre 3 e 4

g.imprimir_matriz()  # Mostra a matriz
print("Grau do vértice 0:", g.grau_vertice(0))  # Deve mostrar 2
