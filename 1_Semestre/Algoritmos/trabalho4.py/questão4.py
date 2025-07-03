# Aluno : Weverton Cristian de Sousa Duarte 
# Ultima atualização 21/11/2022

# Construa um programa que mostre todos os valores inteiros entre -n e n fornecidos pelo usuário

n = int(input('Forneça um número inteiro para o limite: '))


for c in range(-n,n+1):
    print(c)
    c += 1