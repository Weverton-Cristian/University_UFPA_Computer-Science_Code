# Aluno: Weverton Cristian de Sousa Duarte
# Data 30/12/2022

#Faça um programa que mostre todos os números primos entre 1 e n (n será um número inteiro
#maior que 1 fornecido pelo usuário). Criar uma função que receba n e retorne True ou False,
#informando, respectivamente, se n é primo ou não.
#OBS: Um número é primo se ele é maior do que um e é divisível apenas por um e por ele mesmo.
#Por exemplo, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, … 

def primoTrueFalse(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def numPrimos(n):
    primos = []
    for i in range(2,n + 1):
        if primoTrueFalse(i):
            primos.append(i)
    
    return print(f'Os números primos entre 1 e {n} são: {primos}')

n = int(input('Informe o número para sua verificação: '))

if primoTrueFalse(n):
    print(f'{n} é um número primo')
else:
    print(f'{n} não é um número primo')

numPrimos(n)
