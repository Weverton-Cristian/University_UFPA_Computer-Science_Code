# 7. Fazer um programa que calcule e mostre o décimo termo (a10) de uma progressão aritimetica (PA), dados o primeiro termo (a1) e a razão r.
a1 = int(input('Digite o valor do primeiro termo: '))
r = int(input(' informe o valor da razão aritimética'))
n = 10
décimoT = a1 + ((n-1)*r)
print('O valor do Décimo termo é:',décimoT)