"""
1) Escreva uma função recursiva para calcular a
soma de todos os elementos de uma lista.

"""

lista = [10, 20, 30, 40]

def soma_recursiva(lista):
    if len(lista) == 0:
        return 0 # Caso base de lista vazia 
    
    else:
        return lista[0] + soma_recursiva(lista[1:]) # Soma do primeiro elemento com os demais 
    
print(soma_recursiva(lista))
