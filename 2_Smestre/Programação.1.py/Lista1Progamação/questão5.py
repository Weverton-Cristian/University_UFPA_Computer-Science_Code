#Aluno: Weverton Cristian de Sousa Duarte N° 20220492554
#Lista 1 de progrmação 1

#5) Dados dois vetores A e B de mesmo tamanho, calcule o produto escalar desses 
#vetores, que é a soma dos produtos dos elementos correspondentes: 
#A[0]*B[0] + A[1]*B[1] + ... + A[n]*B[n].
#Exemplo de Entrada: A = [1, 2, 3], B = [4, 5, 6]
#Exemplo de Saída: 32 (1*4 + 2*5 + 3*6)


vetorA = []

vetorB = []

for c in range(3):
    coordenadas = float(input("Forneça os elementos do primeiro vetor: "))
    vetorA.append(coordenadas)

for c in range(3):
    coordenadas = float(input("Forneça os elementos do segundo vetor: "))
    vetorB.append(coordenadas)

#Produto escalar
res = 0

for c in range(3):
    res = res + vetorA[c] * vetorB[c]

print(f"O produto escalar dos vetores {vetorA} e {vetorB} é igual a {res}")


