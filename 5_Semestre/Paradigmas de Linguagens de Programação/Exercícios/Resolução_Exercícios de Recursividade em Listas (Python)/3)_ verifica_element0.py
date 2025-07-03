"""
3) Crie uma função recursiva que verifique se um
determinado elemento está presente em uma lista.

"""

lista = [1,3,4,7,9,10]

def verifica_elemento(lista, elemento, indice=0):
    if indice == len(lista):
        return False
    
    elif lista[indice] == elemento:
        return True
    
    else:
        return verifica_elemento(lista, elemento, indice + 1)

print(verifica_elemento(lista,7), "Elemento Encontrado")