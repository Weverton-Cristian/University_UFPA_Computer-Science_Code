# Aluno: Weverton Cristian De Sousa Duarte
#Programa que receba o valor de uma compra percentual de desconto,
#  o valor do desconto concedido e o valor final a ser pago.
valorc = float(input('Informe o valor da compra: '))
desconto100 = (valorc * 5 )/100
descontoM = (valorc * 10)/100
valorF1 = valorc - desconto100
valorF2 = valorc - descontoM
if valorc <= 100:
    print('Sua compra foi encerrada, seu desconto foi de 5%, o valor do desconto foi de:',desconto100,'reais.'
    'O valor final a ser pago é:',valorF1)
elif valorc >= 101:
    print('Sua compra foi encerrada, seu desconto foi de 10%, o valor do desconto foi de:',descontoM,'reais.'
    'O valor final a ser pago é:',valorF2)
    

   