class GrafoLista:
    def __init__(self, num_vertices):
        # Inicializa o número de vértices
        self.num_vertices = num_vertices
        # Cria uma lista vazia para cada vértice
        # Ex: lista[0] terá os vértices conectados ao vértice 0
        self.lista = [[] for _ in range(num_vertices)]

    def adicionar_aresta(self, u, v):
        # Adiciona uma aresta entre os vértices u e v
        self.lista[u].append(v)  # Adiciona v à lista de u
        self.lista[v].append(u)  # Adiciona u à lista de v (grafo não-direcionado)

    def imprimir_lista(self):
        # Imprime a lista de adjacência
        for i in range(self.num_vertices):
            print(f"{i}: {self.lista[i]}")  # Mostra os vizinhos do vértice i

    def grau_vertice(self, v):
        # O grau de um vértice é o tamanho da lista de vizinhos
        return len(self.lista[v])


# Exemplo de uso
g = GrafoLista(5)  # Cria um grafo com 5 vértices
g.adicionar_aresta(0, 1)  # Adiciona aresta entre 0 e 1
g.adicionar_aresta(0, 2)  # Adiciona aresta entre 0 e 2
g.adicionar_aresta(3, 4)  # Adiciona aresta entre 3 e 4

g.imprimir_lista()  # Mostra as conexões
print("Grau do vértice 0:", g.grau_vertice(0))  # Deve mostrar 2
