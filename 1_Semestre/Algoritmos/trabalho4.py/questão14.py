# Aluno : Weverton Cristian de Sousa Duarte 
# Ultima atualização 21/11/2022

# Programa que receba um valor n>=0 e forneça o seu fatorial

n = int(input('Fatorial de: '))
fat = 1
for c in range(1,n+1):
    fat *= c
print(fat)
# fat vai inicializar com 1
