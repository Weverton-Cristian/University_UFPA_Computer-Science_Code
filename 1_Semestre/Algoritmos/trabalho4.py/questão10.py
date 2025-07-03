# Aluno : Weverton Cristian de Sousa Duarte 
# Ultima atualização 21/11/2022
# Fazer um programa que leia n valores entre 0 e 100 e no final forneça o maior o segundo maior e o terceiro maior
n  = int(input('Informe quantos valores serão lidos: '))

maior = 0
segMaior = 0
tercMaior = 0

for i in range(1, n+1):

    val = int(input('Informe um valor entre 0 e 100: '))

    while val < 0 or val > 100:
        val = int(input('Informe um valor entre 0 e 100: '))

if val > maior:
    if maior > segMaior:
       if segMaior > tercMaior:
        tercMaior = segMaior
        segMaior = maior
    maior = val
elif val > segMaior:
    if segMaior > tercMaior:
        tercMaior = segMaior
    segMaior = val
else:
    tercMaior = val   
print('O maior valor é:',maior)
print('O segundo maior valor é:',segMaior)
print('O terceiro maior valor é:',tercMaior)