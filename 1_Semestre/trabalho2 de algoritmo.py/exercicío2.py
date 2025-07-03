# Aluno: Weverton Cristian De Sousa Duarte
# 2. Escrever um programa para ler dois valores numéricos diferentes e informar e também
# apresentar a diferença entre o  maior e o menor.

valor1 = float(input('Informe o primeiro valor: '))
valor2 = float(input('Informe o segundo valor: '))

diferença = valor1-valor2
diferença1 = valor2-valor1

if valor1 > valor2:
   print ('O maior valor é o:',valor1,'A diferença entre o maior e o menor valor é: ',diferença)

else:
  print('O maior valor é o: ', valor2,'A diferença entre o maior e o menor valor é:  ',diferença1)
  

#não é possivel resolver sem IF