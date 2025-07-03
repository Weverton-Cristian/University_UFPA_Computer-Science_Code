#Aluno: Weverton Cristian de Sousa Duarte N° 20220492554
#Lista 1 de progrmação 1

#1) Desenvolva um programa que calcula e mostra na tela o valor de b**n. O valor de 
#n deverá ser maior do que 1 e inteiro e o valor de b maior ou igual a 2 e inteiro.

b = int(input("Forneça um valor inteiro maior ou igual a 2: "))
while b < 2:
    print("Valor inválido")
    b = int(input("Forneça um valor inteiro maior ou igual a 2: "))

n = int(input("Forneça um valor inteiro maior que 1: "))
while n < 1:
    print("Valor inválido")
    n = int(input("Forneça um valor inteiro maior que 1: "))

conta = b**n

print(f"O valor calculado utilizando {b} e {n} é igual a: {conta}")








