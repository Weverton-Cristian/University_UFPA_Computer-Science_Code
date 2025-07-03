#Aluno: Weverton Cristian de Sousa Duarte N° 20220492554
#Lista 1 de progrmação 1

#2) Escreva um programa que encontre o maior elemento de um vetor e sua posição 
#correspondente.

MeuVetor = int(input("Forneça a quantidade de valores do seu vetor: "))
vetor = []
m = 0
pos = 0
for c in range(MeuVetor):
    vetor.append(int(input("Infomer os elementos do seu vetor:")))
    if vetor[c] > m:
        m = vetor[c]

for c,i in enumerate(vetor):
    if i == m:
        pos = c
    
print(f"Os valores do vetor que voçe forneceu estão aqui {vetor}")
print(f"O maior elemento do seu vetor é {m} e sua posição é {pos}")





