import random
import matplotlib.pyplot as plt
import numpy as np

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

    def altura(self):
        if self.raiz is None:
            return 0
        fila = [(self.raiz, 1)]
        altura_maxima = 0
        while fila:
            no, altura = fila.pop(0)
            altura_maxima = max(altura_maxima, altura)
            if no.esquerda:
                fila.append((no.esquerda, altura + 1))
            if no.direita:
                fila.append((no.direita, altura + 1))
        return altura_maxima

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
        self.ajustar_insercao(novo_no)

    def ajustar_insercao(self, no):
        while no.pai and no.pai.cor == 'V':
            if no.pai == no.pai.pai.esquerda:
                tio = no.pai.pai.direita
                if tio and tio.cor == 'V':
                    no.pai.cor = 'P'
                    tio.cor = 'P'
                    no.pai.pai.cor = 'V'
                    no = no.pai.pai
                else:
                    if no == no.pai.direita:
                        no = no.pai
                        self.rotacao_esquerda(no)
                    no.pai.cor = 'P'
                    no.pai.pai.cor = 'V'
                    self.rotacao_direita(no.pai.pai)
            else:
                tio = no.pai.pai.esquerda
                if tio and tio.cor == 'V':
                    no.pai.cor = 'P'
                    tio.cor = 'P'
                    no.pai.pai.cor = 'V'
                    no = no.pai.pai
                else:
                    if no == no.pai.esquerda:
                        no = no.pai
                        self.rotacao_direita(no)
                    no.pai.cor = 'P'
                    no.pai.pai.cor = 'V'
                    self.rotacao_esquerda(no.pai.pai)
        self.raiz.cor = 'P'

    def rotacao_esquerda(self, no):
        filho_direita = no.direita
        no.direita = filho_direita.esquerda
        if filho_direita.esquerda != self.TNULL:
            filho_direita.esquerda.pai = no
        filho_direita.pai = no.pai
        if no.pai is None:
            self.raiz = filho_direita
        elif no == no.pai.esquerda:
            no.pai.esquerda = filho_direita
        else:
            no.pai.direita = filho_direita
        filho_direita.esquerda = no
        no.pai = filho_direita

    def rotacao_direita(self, no):
        filho_esquerda = no.esquerda
        no.esquerda = filho_esquerda.direita
        if filho_esquerda.direita != self.TNULL:
            filho_esquerda.direita.pai = no
        filho_esquerda.pai = no.pai
        if no.pai is None:
            self.raiz = filho_esquerda
        elif no == no.pai.direita:
            no.pai.direita = filho_esquerda
        else:
            no.pai.esquerda = filho_esquerda
        filho_esquerda.direita = no
        no.pai = filho_esquerda

    def altura(self, no=None):
        if no is None:
            no = self.raiz
        if no == self.TNULL:
            return 0
        return 1 + max(self.altura(no.esquerda), self.altura(no.direita))

# Código para teste e geração dos gráficos
valores = random.sample(range(10000), 1000)
bst = ArvoreBST()
rbt = ArvoreRubroNegra()

# Inserção dos valores nas árvores e registro da altura
alturas_bst = []
alturas_rbt = []
n_elementos = []

for i, valor in enumerate(valores, start=1):
    bst.inserir(valor)
    rbt.inserir(valor)
    alturas_bst.append(bst.altura())
    alturas_rbt.append(rbt.altura())
    n_elementos.append(i)

# Gerar gráfico de complexidade (altura da árvore)
plt.figure(figsize=(10, 5))
plt.plot(n_elementos, alturas_bst, label='BST Desbalanceada (O(n))', color='red')
plt.plot(n_elementos, alturas_rbt, label='Árvore Rubro-Negra (O(log n))', color='blue')
plt.plot(n_elementos, np.log2(n_elementos), '--', label='O(log n) Teórico', color='green')
plt.plot(n_elementos, n_elementos, '--', label='O(n) Teórico', color='purple')
plt.xlabel('Número de Elementos Inseridos')
plt.ylabel('Altura da Árvore')
plt.title('Comparação da Complexidade: BST vs. Rubro-Negra')
plt.legend()
plt.show()
