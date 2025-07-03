# Aluno : Weverton Cristian de Sousa Duarte 
# Ultima atualização 21/11/2022
# Construir programa que leia os jogadores e seus numero de gols, cartoes e forneça o desempenho

n = int(input('Informe a quantidade de jogadores: '))
cont = 0
somaD = 0
maiorD = -10000
menorD = -10000

for c in range(1,n+1):
    nome = str(input(f'Informe o nome do jogador{cont+1}'))
    numGoals = int(input('Informe o número de gols marcados: '))
    numCartões = int(input('Informe o número de cartoes recebidos: '))

    desemp = (numGoals*10 -numCartões*2)/5
    somaD += desemp
    
    cont += 1

    if desemp > maiorD:
        maiorD = desemp
        maiorDenome = nome
    if desemp > maiorD:
        menorD  = desemp
        menorDenome = nome
    print('O jogador',nome,'teve o desempenho de',desemp)


mediaD = somaD/cont

print('A média de desempenho foi de:',mediaD)
print('O maior desempenho foi de:',maiorD,'Do jogador:',maiorDenome)
print('O maior desempenho foi de:',menorD,'Do jogador:',menorDenome)

