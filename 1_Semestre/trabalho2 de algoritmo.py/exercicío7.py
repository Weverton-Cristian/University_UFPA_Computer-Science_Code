# Aluno: Weverton Cristian De Sousa Duarte
#Programa que leia a idade de uma pessoa e diga se ela esta liberada ou não de votar
idade = int(input('informe sua idade: '))
if idade < 18 or idade >= 70:
    print('O cidadão não é obrigado a votar')
else:
    print('O cidadãoé obr igado a votar')

