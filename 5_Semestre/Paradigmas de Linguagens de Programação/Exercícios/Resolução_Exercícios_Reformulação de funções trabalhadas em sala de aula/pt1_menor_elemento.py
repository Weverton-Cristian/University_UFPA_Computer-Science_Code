# Discente: Weverton Cristian de Sousa Duarte

# Função que retonar o menor elemento, sem utilixar return.

# Versão Original:

# def menor(l):
#    return cabeca(l) if tamanho(l) == 1 else menor2(cabeca(l),menor(cauda(l))) 

def cabeca(lista):
    return lista[0]

def cauda(lista):
    return lista[1:]

def tamanho(lista):
    return 0 if lista == [] else tamanho(cauda(lista)) + 1

def menor(l):
    if tamanho(l) == 1:
        return cabeca(l)
    cb = cabeca(l)
    menor_cd = menor(cauda(l))
    if cb < menor_cd:
        return cb
    else:
        return menor_cd

# Teste
print(menor([4, 2, 1, 7, 6]))
