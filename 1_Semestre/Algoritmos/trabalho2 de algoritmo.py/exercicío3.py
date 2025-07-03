# Aluno: Weverton Cristian De Sousa Duarte
# 3. Faça um programa que leia um número e informe se este número é par ou ímpar.

número = float(input('Insira um número: '))
resultado = número % 2
if resultado == 0:
    print('O valor',número,'é PAR')
else:
   print('O valor',número,'é ÍMPAR')
