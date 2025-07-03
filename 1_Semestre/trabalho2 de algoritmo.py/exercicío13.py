# Aluno: Weverton Cristian De Sousa Duarte
# Altere o programa anterior para mostrar o salário liquido também 
valorsalMin = float(input('Qual o seu salário mínimo: '))
numPeças = float(input('Número de peças que você montou: '))

if valorsalMin <= 1000:
    valorImpost = valorsalMin*(2/100)
    salLiquido = valorsalMin - valorImpost

    if numPeças <= 30:
     print('O salário bruto fornecido é de R$:',valorsalMin,'e o valor adicional é de R$: 00.0,'
      'o salário liquido foi de',salLiquido)
    else:
       peçaExtra = numPeças-30
       salAdicional = valorsalMin + ((valorsalMin*(1/100))*peçaExtra)
       print('O salário bruto que será recebido é de R$:', valorsalMin,'e o valor adicional é de',salAdicional,
       'e o salário liquido foi de',salLiquido)

else:
    valorImpost = valorsalMin*(5/100)
    salLiquido = valorsalMin- valorImpost

    if numPeças <= 30: 
        print('O salário bruto fornecido será de R$:',valorsalMin,'e o valor adicional é de R$ 00.0,'
          'o salário líquido fornecido é de:',salLiquido)
    else: 
        peçaExtra = numPeças-30
        salAdicional = valorsalMin + ((valorsalMin*(1/100))*peçaExtra)
        print('O salário bruto fornecido será de R$:',valorsalMin,'e o valor adicional é de R$,',salAdicional,
          'o salário líquido fornecido é de:',salLiquido)

    