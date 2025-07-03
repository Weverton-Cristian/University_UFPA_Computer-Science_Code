#Refazer o programa anterior, de modo que seja solicitada ao usuário uma faixa de valores,
#delimitadas por x e y (x <= y). Caso o usuário informe um valor de x maior que y, imprimir
#mensagem de erro, até que os valores adequados sejam informados.

x = float(input('Informe o valor: '))
y = float(input('Informe um valor maior: '))

while x > y:
    print('Erro o primeiro valor tem que ser menor')
    
