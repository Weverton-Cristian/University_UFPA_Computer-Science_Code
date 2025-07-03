# Discente: Weverton Cristian de Sousa Duarte

# Representação de um grafo com lista de adjacência

class Grafo:
    def __init__(self, vertices):
        self.V = vertices  # número de vértices
        self.adj = {v: [] for v in vertices}  # lista de adjacência

    def adicionar_aresta(self, u, v):
        self.adj[u].append(v)  # para grafo dirigido
        # Para grafo não-dirigido, descomente a próxima linha:
        # self.adj[v].append(u)

# Implementação do DFS com base no Cormen
class DFS:
    def __init__(self, grafo):
        self.grafo = grafo
        self.tempo = 0
        self.cor = {u: 'white' for u in grafo.V}
        self.d = {u: 0 for u in grafo.V}
        self.f = {u: 0 for u in grafo.V}
        self.pi = {u: None for u in grafo.V}

    def executar(self):
        for u in self.grafo.V:
            if self.cor[u] == 'white':
                self.dfs_visita(u)

    def dfs_visita(self, u):
        self.tempo += 1
        self.d[u] = self.tempo
        self.cor[u] = 'gray'

        for v in self.grafo.adj[u]:
            if self.cor[v] == 'white':
                self.pi[v] = u
                self.dfs_visita(v)

        self.cor[u] = 'black'
        self.tempo += 1
        self.f[u] = self.tempo

    def imprimir_resultados(self):
        for u in self.grafo.V:
            print(f"Vértice {u}: d = {self.d[u]}, f = {self.f[u]}, π = {self.pi[u]}")

# Exemplo de uso:
vertices = ['u', 'v', 'w', 'x', 'y', 'z']
g = Grafo(vertices)
g.adicionar_aresta('u', 'v')
g.adicionar_aresta('u', 'x')
g.adicionar_aresta('x', 'v')
g.adicionar_aresta('v', 'y')
g.adicionar_aresta('y', 'x')
g.adicionar_aresta('w', 'y')
g.adicionar_aresta('w', 'z')
g.adicionar_aresta('z', 'z')

# Abaixo eu explico o grafo escolhido

# O grafo mostrado acima é direcionado onde o primeiro vertice aponta para o segundo, então nessa análise
# podemos perceber que o algoritmo é iniciado no vértice "U" e segue a ordem alfabetica, portanto quando chegamos
# no vértice "X" vindo do vértice "y" o algortimo percebe que não tem para onde ir e finaliza "x"  e
# retorna para "y", após ele vai finalizando e voltando até chegar no inicio e finaliza, após isso 
# ele escolhe outro vértice de acordo com a ordem alfabetica o "W" depois é só ir para o "Z" e finalizar 
# ambos os vértices sendo o "W" o ultimo vértice a ser finalizado.


dfs = DFS(g)
dfs.executar()
dfs.imprimir_resultados()

