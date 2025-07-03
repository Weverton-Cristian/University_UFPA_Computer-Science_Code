# Aluno: Weverton Cristian de Sousa Duarte
# Data 30/12/2022

#Faça um programa que inicialmente leia um valor n, e na sequência, leia n números reais entre 0
#e dez (garantir que essa faixa será obedecida pelo usuário). O programa deve fornecer:
# o maior e o menor elemento , a média dos elementos, o desvio padrão dos elementos
#quantos elementos estão acima de 5, e qual a média desses elementos
# quantos valores ficaram entre 9 e 10 (inclusive) e qual a média desses elementos

n = int(input('Forneça o número de repetiçoes: '))

maior = -2
menor = 100
media = 0
acim5 = 0 
media5 = 0
acim9 = 0
medi9 = 0
for c in range(1,n+1):
    i = float(input('forneça um valor entre 0 e 10: '))
    while i < 0 or i > 10:
        i = float(input('forneça um valor entre 0 e 10: '))
    if i > maior:
        maior = i
    if i < menor:
        menor = i
    media = i + media 
    mediaf = media/n
    if i > 5:
        acim5 = acim5 + 1
        medi5 = i + acim5
        medi5f = medi5/acim5
    if i > 9:
        acim9  = acim9 + 1
        medi9 = i + acim9
        media9f = medi9/acim9

print('O maior valor é:',maior) 
print('O menor valor é:',menor)      
print('A media geral é:',mediaf)
print('O número de valores acima de 5 é:',acim5)
print('A média dos valores acima de 5 é:',medi5f)
print('O número de valores acima de 9 é:',acim9)
print('A média dos valores acima de 9 é:',media9f)