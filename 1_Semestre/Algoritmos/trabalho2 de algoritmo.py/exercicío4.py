# Aluno: Weverton Cristian De Sousa Duarte
# Programa que leia um número não nulo e diga se é positivo ou negativo
número = float(input('Escolha um valor: '))
if número > 0:
    print(número,'é um valor positivo.')
elif número == 0:
    print('Por favor informe um número diferente de zero')
else:
    print(número,'é um valor negativo.')

