#5 Fazer um algoritmo que calcule o volume de um cubo(em cm**3), dada a área de sua face(em cm**2).
areaf = float(input('Informe o valor da área de uma face em cm² '))
aresta = float(areaf ** 0.5)
volume = float(aresta ** 3)
print('O volume do cubo é:', volume, 'O valor da aresta é:', aresta, 'O valor da area mencinada é:',areaf)