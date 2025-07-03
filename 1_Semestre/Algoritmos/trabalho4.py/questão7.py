# Aluno : Weverton Cristian de Sousa Duarte 
# Ultima atualização 21/11/2022

# Criar um programa que receba todas as idades e forneça oque é pedido

cont = 0
soma = 0 

for c in range(1, 10+1):

    idade = int(input(f'Forneça a idade: {cont+1}'))
    
    soma += idade 
    cont += 1 
mediaIda = soma/cont
print('A média das idades dos netos é igual a:',mediaIda)
