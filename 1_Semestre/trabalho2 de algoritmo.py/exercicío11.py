# Aluno: Weverton Cristian De Sousa Duarte
#Programa que receba o valor da hora normal e a quantidade de horas trabalhadas na semana,
#  e forneça: o salário normal semanal, o salário extra, e o salário total do funcioário.

valorh = float(input('Informe o valor do seu salário por horas de trabalho: '))
horaEx = float(input('Informe a quantidade de horas extras trabalhadas:' ))

qhora = 40

qhorastrab =  qhora + horaEx
salarioN = valorh*qhorastrab
if qhorastrab > 40:
    horaEXTRA = ((valorh*50)/100)
    salarioEX = horaEx * valorh
    salariot = salarioN + salarioEX
    print('O trabalhador tem o salário normal de:',salarioN,'seu salário normal será somado com o extra:'
    ,salarioEX,'o seu salário final é:',salariot)
else:
    print('O trabalhador tem o salário normal de:',salarioN,)