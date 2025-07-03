"""
2) Implemente uma função recursiva que conte quantos
elementos existem em uma lista.

"""
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def contagem_elemento(lista, indice=0):
    if indice == len(lista):
        return 0  # Caso base: índice chegou ao fim da lista
    
    else:
        return 1 + contagem_elemento(lista, indice + 1)  # Avança para o próximo índice

print(contagem_elemento(lista))