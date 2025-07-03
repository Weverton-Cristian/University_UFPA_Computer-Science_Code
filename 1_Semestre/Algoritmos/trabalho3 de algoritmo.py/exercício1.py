# 1. Construa um programa para imprimir lado-a-lado, duas seqüencias de valores: uma que vai
#de 1 a n (valor fornecido pelo usuário) e outra que vai de n a 1, conforme o modelo abaixo. 

n = float(input('Informe o valor limite'))
i = 1 
while i <= n: 
    print(i,'   ',n-1+1)
    