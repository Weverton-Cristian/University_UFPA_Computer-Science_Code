# Aluno: Weverton Cristian de Sousa Duarte
# Data 30/12/2022

#A série de Fibonacci é formada da seguinte maneira: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,…
#Ou seja, os dois primeiros elementos, F0 e F1 são fixos (0 e 1) e os demais, Fn , são sempre a soma
#dos dois anteriores. Faça um programa que gere a série até que se alcance um valor maior que 2000.
#Empregar uma função que receba n e retorne o enésimo termo da sequencia, isto é, Fn. Empregue,
#tanto na função quanto no corpo principal do programa a estrutura de repetição que julgar mais
#conveniente. 

n = 20
a = 0
b = 1
s = 0

for i in range(n+1):
    print(s,end=' ')

    if s > 2000:
        s = a + b
        b = a 
        a = s

def enesimo (x):
    fib = []
    a = 0 
    b = 1
    s = 0

    for j in range(x):
        s = a + b
        b = a
        a = s

        fib.append(s)
        return max(fib)
print(f'O enesimo termo dos valores é: {enesimo(n)}')
