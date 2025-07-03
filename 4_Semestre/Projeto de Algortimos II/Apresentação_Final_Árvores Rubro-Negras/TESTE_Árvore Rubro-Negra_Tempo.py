import time
import random
import numpy as np
import matplotlib.pyplot as plt

# Classe para um nó da árvore binária de busca (BST desbalanceada)
class NoBST:
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None

# Classe para a BST desbalanceada
class ArvoreBST:
    def __init__(self):
        self.raiz = None

    def inserir(self, chave):
        novo_no = NoBST(chave)
        if self.raiz is None:
            self.raiz = novo_no
            return

        atual = self.raiz
        while True:
            if chave < atual.chave:
                if atual.esquerda is None:
                    atual.esquerda = novo_no
                    return
                atual = atual.esquerda
            else:
                if atual.direita is None:
                    atual.direita = novo_no
                    return
                atual = atual.direita

# Classe para um nó da Árvore Rubro-Negra
class NoRubroNegro:
    def __init__(self, chave, cor='V'):
        self.chave = chave
        self.cor = cor
        self.esquerda = None
        self.direita = None
        self.pai = None

# Classe para a Árvore Rubro-Negra
class ArvoreRubroNegra:
    def __init__(self):
        self.TNULL = NoRubroNegro(None, cor='P')
        self.raiz = self.TNULL

    def inserir(self, chave):
        novo_no = NoRubroNegro(chave)
        novo_no.esquerda = self.TNULL
        novo_no.direita = self.TNULL
        pai = None
        atual = self.raiz

        while atual != self.TNULL:
            pai = atual
            if chave < atual.chave:
                atual = atual.esquerda
            else:
                atual = atual.direita

        novo_no.pai = pai
        if pai is None:
            self.raiz = novo_no
        elif chave < pai.chave:
            pai.esquerda = novo_no
        else:
            pai.direita = novo_no

        novo_no.cor = 'V'

# Código para teste e comparação de tempo
valores = random.sample(range(10000), 1000)
bst = ArvoreBST()
rbt = ArvoreRubroNegra()

# Medir tempo de inserção
tempos_bst = []
tempos_rbt = []
n_elementos = []

for i, valor in enumerate(valores, start=1):
    inicio_bst = time.time()
    bst.inserir(valor)
    fim_bst = time.time()

    inicio_rbt = time.time()
    rbt.inserir(valor)
    fim_rbt = time.time()

    tempos_bst.append(fim_bst - inicio_bst)
    tempos_rbt.append(fim_rbt - inicio_rbt)
    n_elementos.append(i)

# Gerar gráfico de tempo de inserção
plt.figure(figsize=(10, 5))
plt.plot(n_elementos, np.cumsum(tempos_bst), label='BST Desbalanceada (Tempo acumulado)', color='red')
plt.plot(n_elementos, np.cumsum(tempos_rbt), label='Árvore Rubro-Negra (Tempo acumulado)', color='blue')
plt.xlabel('Número de Elementos Inseridos')
plt.ylabel('Tempo (segundos)')
plt.title('Comparação de Tempo: BST vs. Rubro-Negra')
plt.legend()
plt.show()

# Retornar os tempos finais de inserção
print(f"Tempo final BST: {np.cumsum(tempos_bst)[-1]:.6f} segundos")
print(f"Tempo final Rubro-Negra: {np.cumsum(tempos_rbt)[-1]:.6f} segundos")
