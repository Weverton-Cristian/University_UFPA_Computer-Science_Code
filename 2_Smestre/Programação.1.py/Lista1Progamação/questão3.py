#Aluno: Weverton Cristian de Sousa Duarte N° 20220492554
#Lista 1 de progrmação 1

#3) Escreva um programa que conte o número de elementos pares e ímpares em um
#vetor.

MeuVetor = int(input("Forneça a quantidade de valores do seu vetor: "))
vetor = []
par = 0
impar = 0
for i in range(MeuVetor):
    vetor.append(int(input("Infomer os elementos do seu vetor:")))
for c in range(MeuVetor):
    if vetor[c] % 2 == 0:
        par += 1
    else:
        impar += 1

    
print(f"O vetor fornecido por você {vetor}")
print(f"O total de números pares é {par} e o total de números impares é {impar}")
