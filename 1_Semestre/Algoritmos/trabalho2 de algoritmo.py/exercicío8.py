# Aluno: Weverton Cristian De Sousa Duarte
#Programa que leia a idade de uma pessoa e diga se ela é obrigada ou não a votar
idade = int(input('informe sua idade: '))
if idade >= 18 and idade < 70:
    print('O cidadão é obrigado a votar')
else:
    print('O cidadão não é obrigado a votar, portando pode ir embora')
    