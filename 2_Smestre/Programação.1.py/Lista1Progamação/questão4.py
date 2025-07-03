#Aluno: Weverton Cristian de Sousa Duarte N° 20220492554
#Lista 1 de progrmação 1

#4) Faça um programa que leia um vetor de 10 valores inteiros e positivos. A partir 
#do vetor original, criar um segundo vetor da seguinte forma: os elementos de 
#índice par receberão os respectivos valores multiplicados por 2; e os elementos 
#de índice ímpar receberão os respectivos valores multiplicados por 3. Imprima 
#os vetores gerados.

MeuVetor = [7,13,10,9,22,13,17,27,35,48]
NovoVetor = []

for c in MeuVetor:
    if(c%2==0):
        NovoVetor.insert(c,c*2)
    
    else:
        NovoVetor.insert(c,c*3)
    
print(f"Aqui está o vetor transformando {NovoVetor}")