# Aluno: Weverton Cristian de Sousa Duarte
# Data 30/12/2022

#Faça um programa que receba dois números inteiros não negativos, isto é, maiores ou iguais a
#zero (supor que o usuário fornecerá valores válidos), que representam a base (b) e o expoente (e) de
#uma potência b
#e calcule e mostre o resultado desse cálculo. Não utilize nem o operador nem a
#função de potência da linguagem (calcular via estrutura de repetição).

b = int(input('Forneça o valor da base: '))
e = int(input('Forneça o valor do expoente: '))

if e == 0 and b != 0:
    print('O resultado é igual a 1')
elif b == 0 and e != 0:
    print('O resultado é igual a 0')
elif e == 0 and b == 0:
    print('Indeterminado')
else:
    result = 1
    for c in range(1,e+1):
        result *= b
    print(b,'elevado á',e,'é igual á:',result)