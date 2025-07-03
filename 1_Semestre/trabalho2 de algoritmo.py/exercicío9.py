# Aluno: Weverton Cristian De Sousa Duarte
#Programa que recebe os valores do salário e da prestação e informe se o empréstimo pode ou nçao ser concedido
salario = float(input('Informe seu salário: '))
prest = float(input('Informe o valor da prestação: '))

salario30 = (salario*30)/100
if prest > salario30:
    print('O funcionário não poderá receber, pois o valor da prestação',prest,
    'é maior que 30% do seu salário que aquivale a :',salario30)
else: 
    print('O funcionáriopoder á receber, pois o valor da prestação',prest,
    'não é maior do que 30% do seu salário que aquivale a :',salario30)