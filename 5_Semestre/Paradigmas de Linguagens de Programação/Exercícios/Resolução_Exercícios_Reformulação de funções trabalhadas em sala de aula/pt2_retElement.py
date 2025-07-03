# Discente: Weverton Cristian de Sousa Duarte

# Função que remove um item assim que aparece na lista

# Versão Original:

# def retElem(l,x): 
#    return cauda(l) if x == cabeca(l) else [cabeca(l)] + retElem(cauda(l),x)

def cabeca(lista):
    return lista[0]

def cauda(lista):
    return lista[1:]

def retElem(l, x):
    if x == cabeca(l):
        return cauda(l)
    else:
        primeiro = cabeca(l)
        resto = retElem(cauda(l), x)
        resultado = [primeiro] + resto
        return resultado

# Teste
print(retElem([4, 2, 1, 7, 6], 1))  # Deve remover o 1
