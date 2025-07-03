# Fazer um programa que receba as 4 notas semestrais de um aluno, e forneça a média anual. 
nota1 = float(input('Digite a primeira nota do aluno '))
nota2 = float(input('Digite a segunda nota do aluno '))
nota3 = float(input('Digite a terceira nota do aluno '))
nota4 = float(input('Digite a quarta nota do aluno '))
média = (nota1*2 + nota2*2 + nota3*3 + nota4*5)/(2+3+5)
print('A média ponderada vale:',média)
