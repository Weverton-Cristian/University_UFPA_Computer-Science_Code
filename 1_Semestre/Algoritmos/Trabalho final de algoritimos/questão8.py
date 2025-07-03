# Aluno: Weverton Cristian de Sousa Duarte
# Data 30/12/2022

# Numa eleição para síndico de um prédio podem existir n candidatos (n >= 2). Faça um programa
#que peça o número total de eleitores k. Peça para cada um dos k eleitores votar (candidato 1, 2, …
#n) e ao final mostrar o número de votos de cada candidato. Informar o vencedor e o suplente
#(segundo colocado).

n = int(input('Informe o número de candidatos: '))

while n < 2:
    n = int(input('Informe o número de candidatos: '))

k = int(input('Informe o número de eleitores: '))

i = 1
j = 0
candidatos = []
maisV = -100
segmaisV = -100
tercmaisV = -100

while i < n+1:
    candidatos.append(0)
    i += 1

for j in range(k):
    voto = int(input('Digite o número do seu candidato: '))
    while voto < 1:
        print('Voto invalido, por favor escolha novamente.')
        voto = int(input('Digite o número do seu candidato: '))

    candidatos[voto-1] += 1

for h in range(len(candidatos)):
    if candidatos[h] > maisV:
        if maisV > segmaisV:
            if segmaisV > tercmaisV:
                tercmaisV = segmaisV
            segmaisV = maisV
        maisV = candidatos[h]
    elif candidatos[h] > segmaisV:
        if segmaisV > tercmaisV:
            tercmaisV = segmaisV
        segmaisV = candidatos[h]
    elif candidatos[h] > tercmaisV:
        tercmaisV = candidatos[h]

print(f'Candidatos:{candidatos}')

if maisV == segmaisV:
    print('Ocorreu empate entre os candidatos')
else:
    print(f'O vencedor foi o candidato:{candidatos.index(maisV)+1} tendo {maisV} votos')

    if segmaisV == tercmaisV:
        print('Ocorreu empate entre os candidatos que seriam suplentes')
    else:
        print(f'O segundo colocado foi o candidato:{candidatos.index(segmaisV)+1} tendo {segmaisV} votos')

      
    