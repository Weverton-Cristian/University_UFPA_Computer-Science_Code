# Aluno : Weverton Cristian de Sousa Duarte 
# Ultima atualização 21/11/2022
# Fazer um programa que forneça os múltiplos de 3 de x até y e de o produto 



x = int(input('Informe o valor de x: '))
y = int(input('Informe o valor de y: '))

prod = 1

print('Os multiplos de 3 no intervalor escolhido são: ')

if x < y:
    for i in range(x,y+1):
        
        if i%3 == 0:
            print(i)
            prod *= i
else: 
    for i in range(x,y-1,-1):

         if i%3 == 0:
            print(i)
            prod *= i

print('O produto dos valores é:',prod)
    
