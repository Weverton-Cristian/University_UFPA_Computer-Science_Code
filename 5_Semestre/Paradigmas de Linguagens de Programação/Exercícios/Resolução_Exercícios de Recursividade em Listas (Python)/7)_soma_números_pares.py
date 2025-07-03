"""
7) Crie uma função recursiva que some apenas os
números pares de uma lista.

"""
numeros = [1, 2, 3, 4, 5, 6]

def soma_pares(lista):
    if not lista:
        return 0  # Caso base: lista vazia
    elif lista[0] % 2 == 0:
        return lista[0] + soma_pares(lista[1:])  # Soma se for par
    else:
        return soma_pares(lista[1:])  # Ignora se for ímpar

print(soma_pares([1, 2, 3, 4, 5, 6]))  # Saída: 12
