"""
4) Crie uma função recursiva que verifique a posição
(índice) de um determinado elemento em uma lista.
Caso não encontrado esse elemento, retornar o
valor -1.

"""
lista = ['Weverton', 'Benedito', 'Paradigmas']

def verifica_posicao(lista, elemento, indice=0):
    if indice == len(lista):
        return -1
    elif lista[indice] == elemento:
        return indice
    else:
        return verifica_posicao(lista, elemento, indice + 1)

# Testes corrigidos
print(verifica_posicao(lista, 'Weverton'))    # Saída: 0
print(verifica_posicao(lista, 'Benedito'))    # Saída: 1
print(verifica_posicao(lista, 'Paradigmas'))  # Saída: 2
print(verifica_posicao(lista, 'Outro'))       # Saída: -1

