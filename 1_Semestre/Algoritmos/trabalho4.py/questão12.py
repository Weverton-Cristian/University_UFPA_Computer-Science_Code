# Aluno : Weverton Cristian de Sousa Duarte 
# Ultima atualização 21/11/2022

# fazer um programa que receba dois valores inteiros positivos x e y (x<y) 
# e forneça a soma de todos no itervalo e até o y

x = int(input('Forneça um valor inteiro positivo: '))
y = int(input('Forneça um valor inteiro positivo maior que o anterior: '))

soma = 0
for c in range(x,y+1):
    soma += c
print('A soma dos valores no intervalo é:',soma)
