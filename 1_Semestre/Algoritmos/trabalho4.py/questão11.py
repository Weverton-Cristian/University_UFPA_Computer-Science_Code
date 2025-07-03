# Aluno : Weverton Cristian de Sousa Duarte 
# Ultima atualização 21/11/2022
#  Fazer um programa que receba informações dos funcionarios e no final forneça o novo salario com desvio e aumentos

n = int(input('Informe o número de funcionarios da empresa: '))

cont = 0
abono = 500
maiorSal = -10000
segMaiorsal = -10000

for i in range(1, n+1):
    
    nome = str(input(f'Informe o nome dos funcionarios: {cont+1}'))
    salAtual = float(input(f'Informe o salário do funcionario:{cont+1}'))

    salReaj = salAtual + 20/100
    print(f'O funcionario', nome, 'tem agora o salario igual a:',salReaj )

    if salReaj > maiorSal:
        if maiorSal > segMaiorsal:
            segMaiorsal = maiorSal
        maiorSal = salReaj
        nomeMaiorSal = nome 
    elif salReaj > segMaiorsal:
        segMaiorsal = salReaj
    cont +=1

print('O maior sálario é',maiorSal,'do funcionario:', nomeMaiorSal)
print('O Segundo maior salário é giual a:', segMaiorsal)
