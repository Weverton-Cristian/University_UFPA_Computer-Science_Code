c = 1
par = impar = 0
while c != 0:
    c = float(input('forneça um valor: '))
    if c != 0:
        if c % 2 == 0:
            par += 1
        else:
            impar += 1
print('a quantidade de numeros par é {} enquanto os impares são {}'.format(par,impar))
