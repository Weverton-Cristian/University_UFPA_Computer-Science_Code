# Aluno : Weverton Cristian de Sousa Duarte 
# Ultima atualização 21/11/2022

# Construa um programa que realize n vezes o seguinte processamento: receba 3 valores e forneça a média

n = int(input('Forneça um valor limite: '))

for c in range(1,n+1):
    vl1 = float(input('Forneça o primeiro valor: '))
    vl2 = float(input('Forneça o segundo valor: '))
    vl3 = float(input('Forneça o terceiro valor: '))
    média = (vl1+vl2+vl3)/3
    print('O valor da média é:',média)
    


