# Aluno: Weverton Cristian De Sousa Duarte
#Programa que receba o valor do SM, e o número de peças montadas por certo emrepagado e forneça o adicional 
#e o salário bruto
valorsalMin = float(input('Qual o seu salário mínimo: '))
numPeças = float(input('Número de peças que você montou: '))

if numPeças <= 30:
    print('O salário bruto fornecido é de R$:',valorsalMin,'e o valor adicional é de R$: 00.0')
else:
    peçaExtra = numPeças-30
    salAdicional = valorsalMin + ((valorsalMin*(1/100))*peçaExtra)
    print('O salário bruto que será recebido é de R$:', valorsalMin,'e o valor adicional é de',salAdicional)
    