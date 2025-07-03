# Aluno: Weverton Cristian de Sousa Duarte
# Data 30/12/2022

#Faça um programa que peça para n pessoas seu nome e sua idade e sexo (M/F). O valor n
#seráfornecido pelo usuário. Calcule e mostre a média de idade das mulheres e dos homens,
#compare-as e informe qual grupo tem a maior média de idade. Informe a maior idade para as
#mulheres e a menor idade para os homens.



n = int(input('Forneça o número de participantes: '))

totalM = 0
somaIM = 0
totalF = 0
somaIF = 0
menorM = 100000
mediaIM = 0
maiorF = -100
mediaIF = 0

for i in range(1,n+1):
    nome = input('Forneça o seu nome: ')
    idade = int(input('Forneça a sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]: ')).strip().upper()[0]
    
    if sexo == 'M':
        somaIM = somaIM + idade
        totalM = totalM + 1
        if idade < menorM:
            menorM = idade
    mediaIM = somaIM/totalM

    if sexo == 'F':
        somaIF = somaIF + idade
        totalF = totalF + 1
        if idade > maiorF:
            maiorF = idade
        mediaIF = somaIF/totalF
    
print('A media de idade dos homens é:',mediaIM)
print('A média de idade das mulheres é:',mediaIF)
print('A menor idade dos homens é:',menorM)
print('A maior idade das mulhesres é:',maiorF)

if mediaIM > mediaIF:
        print('A média de idade dos homens é maior:',mediaIM)
if mediaIF > mediaIM:
         print('A média de idade das mulhesres é maior:',mediaIF)
if mediaIM == mediaIF:
        print('A média de homens e mulhesres é igual a:',mediaIF)    

