# Aluno: Weverton Cristian De Sousa Duarte
# Programa que leia as notas de um aluno, número de aulas assistidas e número de aulas ministradas
nota1 = float(input('Informe o valor da primeira nota: '))
nota2 = float(input('Informe o valor da segunda nota: '))
aulaMin =  int(input('Informe número de aulas ministradas: '))
aulaAss = int(input('Informe o número de aulas assistidas: '))

média = (nota1+nota2)/2
frequencia = aulaAss/aulaMin
frequenciaN = frequencia*100

if média >= 6 and frequenciaN >= 75:
    print('O aluno foi aprovado, sua média foi',média,'e sua frequência foi',frequenciaN,'%')
else: 
    print('O aluno foi reprovado, sua média foi',média,'e sua frequência foi',frequenciaN,'%')
