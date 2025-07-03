n = int(input('Forneça um valor limite: '))
c = 1

while c <= n:
    vl1 = float(input('Forneça o primeiro valor: '))
    vl2 = float(input('Forneça o segundo valor: '))
    vl3 = float(input('Forneça o terceiro valor: '))
    média = (vl1+vl2+vl3)/3
    c += 1
    print('O valor da média é:',média)