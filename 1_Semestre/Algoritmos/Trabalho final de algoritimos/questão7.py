# Aluno: Weverton Cristian de Sousa Duarte
# Data 30/12/2022

#Numa eleição para síndico de um prédio há 3 candidatos. Faça um programa que peça o número
#total de eleitores n. Peça para cada eleitor votar (candidato 1, 2 ou 3) e ao final mostrar o número de
#votos de cada candidato. Informar o vencedor e o suplente (segundo colocado).

n = int(input('Forneça o número total de eleitores: '))

cand1 = 0
cand2 = 0
cand3 = 0
maior = 0

for c in range(0,n):
    voto = input('Escolha entre o cand1, cand2 e cand3: ')
    if voto == 'cand1':
        cand1 = cand1 + 1
    elif voto == 'cand2':
        cand2 = cand2 +1
    elif voto == 'cand3':
        cand3 = cand3 + 1
    else:
        print('voto nulo')

print('número de votos do canditado 1:',cand1)
print('número de votos do canditado 2:',cand2)
print('número de votos do canditado 3:',cand3)
if cand1 > cand2 and cand1 > cand3:
    print('O canditato 1 ficou em primeiro')
    if cand2 > cand3:
        print('O candidato 2 ficou em segundo')
    elif cand3 > cand2:
        print('O candidato 3 ficou em segundo')
    elif cand2 == cand3:
        print('Os candidatos 2 e 3 terminaram em ampate')
if cand2 > cand1 and cand2 > cand3:
    print('O canditato 2 ficou em primeiro')
    if cand1 > cand3:
        print('O candidato 1 ficou em segundo')
    elif cand3 > cand1:
        print('O candidato 3 ficou em segundo')
    elif cand1 == cand3:
        print('Os candidatos 1 e 3 terminaram em ampate')
if cand3 > cand1 and cand3 > cand2:
    print('O canditato 3 ficou em primeiro')
    if cand2 > cand1:
        print('O candidato 2 ficou em segundo')
    elif cand1 > cand2:
        print('O candidato 1 ficou em segundo')
    elif cand2 == cand3:
        print('Os candidatos 1 e 2 terminaram em ampate')    








