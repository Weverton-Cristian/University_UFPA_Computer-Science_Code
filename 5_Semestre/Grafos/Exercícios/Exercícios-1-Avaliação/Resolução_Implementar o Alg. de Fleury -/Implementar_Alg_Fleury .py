# Discente: Weverton Cristian de Sousa Duarte; 202204940050

# Algoritmo de Fleury:
# Começa em um vértice qualquer (com grau > 0).
# A cada passo, escolhe uma aresta que não seja uma ponte (se possível).
# Remove a aresta escolhida e continua a partir do outro vértice.
# Para haver ciclo Euleriano, o grafo precisa ser conexo e todos os vértices devem ter grau par.

class Grafo:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.grafo = [[] for _ in range(num_vertices)]

# Abaixo adicionei um exemplo explicativo como funciona as conexões do vértice
# Exemplo: grafo[0] = [1, 2] significa que o vértice 0 está ligado aos vértices 1 e 2.

    # A função abaixo chamada de "adicionar_aresta" serve para adiciona aresta nos dois sentidos (grafo não-direcionado)
    def adicionar_aresta(self, u, v):
        self.grafo[u].append(v)
        self.grafo[v].append(u)

    def remover_aresta(self, u, v):
        self.grafo[u].remove(v)
        self.grafo[v].remove(u)

    def dfs_contagem(self, v, visitado):
        visitado[v] = True
        count = 1
        for vizinho in self.grafo[v]:
            if not visitado[vizinho]:
                count += self.dfs_contagem(vizinho, visitado)
        return count

    #Essa função serve para contar os vértices alcaçáveis antes da remoção 
    def eh_ponte(self, u, v):
        visitado = [False] * self.num_vertices
        cont1 = self.dfs_contagem(u, visitado)

        # Remove a aresta e conta novamente
        self.remover_aresta(u, v)
        visitado = [False] * self.num_vertices
        cont2 = self.dfs_contagem(u, visitado)

        # Recoloca a aresta
        self.adicionar_aresta(u, v)

        # Se remover a aresta reduzir a conectividade, é ponte
        return cont2 < cont1

    def imprimir_caminho_euleriano(self, u):
        for v in self.grafo[u][:]:  # cópia da lista
            if not self.eh_ponte(u, v) or len(self.grafo[u]) == 1:
                print(f"{u} -> {v}")
                self.remover_aresta(u, v)
                self.imprimir_caminho_euleriano(v)
                break  # reinicia a verificação com novo vértice

    def tem_ciclo_euleriano(self):
        # Todos os vértices devem ter grau par
        for i in range(self.num_vertices):
            if len(self.grafo[i]) % 2 != 0:
                return False
        return True

    def encontrar_vertice_inicio(self):
        # Retorna um vértice com pelo menos uma aresta
        for i in range(self.num_vertices):
            if len(self.grafo[i]) > 0:
                return i
        return 0  # fallback

# Exemplo de uso
g = Grafo(5)

# Adiciona as arestas do ciclo euleriano
g.adicionar_aresta(0, 1)
g.adicionar_aresta(1, 2)
g.adicionar_aresta(2, 0)
g.adicionar_aresta(0, 3)
g.adicionar_aresta(3, 4)
g.adicionar_aresta(4, 0)

if g.tem_ciclo_euleriano():
    print("Ciclo Euleriano encontrado:")
    inicio = g.encontrar_vertice_inicio()
    g.imprimir_caminho_euleriano(inicio)
else:
    print("O grafo não possui ciclo euleriano.")


