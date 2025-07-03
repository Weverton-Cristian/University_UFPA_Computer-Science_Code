# Aluno : Weverton Cristian de Sousa Duarte 
# Ultima atualização 21/11/2022

# Programa que converta as temperatuas de um mês de celsiu para fahrenheit

n = int(input('Forneça o número de repetições: '))

for c in range(1,n+1):
    
    celT = int(input('Informe a tempreatura em graus celsius: '))

    fahT = celT * 1.8 + 32

    print('A temperatura em fahrenheit é ',{round(fahT,2)})
    
