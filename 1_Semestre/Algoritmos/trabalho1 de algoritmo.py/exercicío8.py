# 8. Fazer um programa que calcule e mostre o enésimo termo de uma PA. Serão fornecidos o primero termo, a razão e n.
a1 = int(input('Digite o valor do Primero termo;\n'))
r = int(input('Informe o valor da Razão aritimética:\n'))
n = int(input('Digite o valor do Número de termos:\n'))
termoénesimo = a1 + ((n-1)*r)
print('O valor do enésimo termo é:', termoénesimo)

