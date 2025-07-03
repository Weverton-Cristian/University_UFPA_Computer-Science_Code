# Aluno : Weverton Cristian de Sousa Duarte 
# Ultima atualização 21/11/2022

# Altere o programa anterior para exibir os valores na ordem inversa (de n  a 1)

n = int(input('Forneça o valor limite: '))
c = 1

if n > 0:
    for c in range(c,n+1):
        print(n)
        n -= 1
else:
    for c in range (n,2):
        print(n)
        n += 1

    