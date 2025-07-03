# Aluno: Weverton Cristian de Sousa Duarte
# Prova de algoritimo

# 2 refazer o exercicío anterior com medidas recebidas em metros e trnsformadas em cm3
# após o calculo dizer se passou ou não de 100 cm3

a = float(input('Forneça a altura do paralelepípedo em metros: '))
b = float(input('Forneça a largura do paralelepípedo em metros: '))
c = float(input('Forneça a profundidade do paralelepípedo metros: '))

volume = a*b*c
volcm3 = volume * 10**6

print('O volume obtido em cm3 é:',volcm3)

if volcm3 > 100:
    print('passou de 100cm3')
else:
    print('não passou de 100cm3')