# Aluno: Weverton Cristian de Sousa Duarte
# Prova de algoritimo

# 5 Fazer um programa que, empregando a estrutura while, caucule a sequencia dos primeiros n termos
# fornecidos


n = float(input('Informe o números de termos: '))
while n < 0:
    n = float(input('Informe o números de termos: '))

numerador = 1
denominador = 2
cont = 1
soma = 0

while cont <= n:
    soma += numerador/denominador
    numerador += 1
    denominador *= 2
    cont += 1

print('A soma dos termos mencionados é:',soma)