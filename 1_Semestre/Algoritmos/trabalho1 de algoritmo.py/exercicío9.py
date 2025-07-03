# 9 Fazer um programa que calcule a soma dos N primeiros termos de uma PA, dados o primeiro termo, a razão e N(Número de termos a somar)
a1 = int(input('Digite o valor do Primeiro termo: '))
r = int(input('Digite o valor da razão aritimética:'))
n = int(input('Informe a quantidade dos primeiros termos a serem somados:'))
termoEnesimo = a1 + ((n-1)*r)
soma = (n*(a1+termoEnesimo))/2
print('A soma dos',n,'primeiros termos da PA é:',int(soma))
