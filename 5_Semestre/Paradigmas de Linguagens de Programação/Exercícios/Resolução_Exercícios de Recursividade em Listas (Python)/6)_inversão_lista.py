"""
6) Implemente uma função recursiva para encontrar o
maior elemento em uma lista.

"""
nomes = ['Weverton', 'Benedito', 'Paradgimas', 'Informatica'] # lista

def inverter_lista(lista):
    if len(lista) <= 1:
        return lista  # Caso base: lista vazia ou com 1 elemento
    else:
        return [lista[-1]] + inverter_lista(lista[:-1])  # Último + inverso do restante

print(inverter_lista(nomes))  # Saída: ['d', 'c', 'b', 'a']