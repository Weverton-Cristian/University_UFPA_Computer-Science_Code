# Aluno: Weverton Cristian De Sousa Duarte
# Programa para ler três valores do maior para o menor e verificar se formam um triângulo 
print('Insira 3 valores')
num1 = float(input('Informe o maior valor:  '))
num2 = float(input('Informe o valor médio:  '))
num3 = float(input('Informe o menor valor:  '))

base = num2 + num3
if base >= num1:
    print('Faz-se possivel forma um triângulo')
else:
    print('Não é possivel formar um triângulo')
