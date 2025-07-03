# Aluno: Weverton Cristian de Sousa Duarte
# Prova de algoritimo

a = float(input('Forneça a altura do paralelepípedo em metros: '))
b = float(input('Forneça a largura do paralelepípedo em metros: '))
c = float(input('Forneça a profundidade do paralelepípedo metros: '))


volume = a*b*c
volcm3 = volume * 10**6

print('O volume obtido em cm3 é:',volcm3)

if volcm3 < 20:
    print('Baixo Volume')
elif volcm3 <=100:
    print('Volume Moderado')
else: 
    print('Volume Elevado')
if volcm3 == 0:
    print('Volume Nulo')
if volcm3 == 200:
    print('Volume crítico atingido')


