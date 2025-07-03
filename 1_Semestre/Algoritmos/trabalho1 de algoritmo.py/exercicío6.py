# 6. fazer um programa que receba o número de pessoas e o número de laranjas a serem repartidas e forneça a quantidade que caberá a cada um
#  a sobra após a repartição.

np = int(input(' informe o número de pessoas '))
nl = int(input('informe o numero de lajanras'))

repartiçao = nl/np
resto = nl%np
print('a divisao resultou em:',repartiçao,'e o resto é:',resto)