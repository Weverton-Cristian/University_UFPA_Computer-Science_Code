#Construa um programa que realize 5 vezes o seguinte processamento: receba 3 valores e
#forneça a média entre esses valores.

n = 1
while n <= 5: 
   not1 = float(input('Forneça o valor da primeira nota: '))
   not2 = float(input('Forneça o valor da segunda nota: '))
   not3 = float(input('Forneça o valor da terceira nota: '))
   média = (not1 + not2 + not3)/3
   print('A média é:',média)
   n +=1


