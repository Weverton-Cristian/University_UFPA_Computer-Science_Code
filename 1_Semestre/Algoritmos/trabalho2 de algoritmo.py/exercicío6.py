# Aluno: Weverton Cristian De Sousa Duarte
#Programa receba um número real e mostre sua raiz quadrada caso ele seja maior ou igual a zero
número = float(input('Digite o número que queira saber a raiz: '))
raiz = número ** (1/2)
if número >= 0:
    print('A raiz desse número é:',raiz)
else: 
    print('Por favor escolha um valor positivo, pois números negativos não tem raiz')
    