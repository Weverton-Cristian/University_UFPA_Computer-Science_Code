# Aluno: Weverton Cristian de Sousa Duarte
# Data 30/12/2022

 #Faça um programa que peça para n pessoas seu nome e sua idade (n fornecido pelo usuário). Ao
#finalizar essas leituras verificar se a média de idade da turma varia entre 0 e 25, acima de 25, porém
#menor que 60, ou maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a
#média calculada. Informar também o nome da pessoa mais velha e o da segunda mais velha; o nome
#da pessoa mais nova e o da segunda mais nova.

import os

n = int (input ('Digite o número de pessoas para a pesquisa: '))

i = 0
somaId = 0
maisVelho = 0
segMaisVelho = 0
nomeMaisVelho = ''
nomeSegMaisVelho = ''
maisNovo = 1000
segMaisNovo = 1000
nomeMaisNovo = ''
nomeSegMaisNovo = ''

for i in range(n):
    
    os.system('cls')
    nome = str (input ('Informe o seu nome: '))
    idade = int (input ('Informe a sua idade : '))

    somaId += idade 

    if idade > maisVelho:
        if maisVelho > segMaisVelho:
            segMaisVelho = maisVelho
            nomeSegMaisVelho = nomeMaisVelho
        maisVelho = idade
        nomeMaisVelho = nome
    elif idade > segMaisVelho:
        segMaisVelho = idade
        nomeSegMaisVelho = nome

    if idade < maisNovo:
        if maisNovo < segMaisNovo:
            segMaisNovo = maisNovo
            nomeSegMaisNovo = nomeMaisNovo
        maisNovo = idade
        nomeMaisNovo = nome
    elif idade < segMaisNovo: 
        segMaisNovo = idade
        nomeSegMaisNovo = nome

med = somaId/n

os.system('cls')

if med >= 0 and med <= 25:
    print('\nStatus Da Turma: Turma jovem ! ')
elif med < 60 :
    print('\nStatus Da Turma: Turma adulta !')
else:
    print('\nStatus Da Turma: Turma idosa !')


print(f'\nAluno Mais velho: {nomeMaisVelho}\n \nSegundo aluno Mais velho: {nomeSegMaisVelho} \n \nAluno mais novo: {nomeMaisNovo} \n \nSegundo aluno mais novo {nomeSegMaisNovo}')