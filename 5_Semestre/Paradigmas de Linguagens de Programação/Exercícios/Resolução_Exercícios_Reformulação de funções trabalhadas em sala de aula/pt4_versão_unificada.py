# Discente: Weverton Cristian de Sousa Duarte

# Aqui está presente todas as alterações feitas em casa uma das três funções fornecidas

def cabeca(lista):
    return lista[0]

def cauda(lista):
    return lista[1:]

def tamanho(lista):
    if lista == []:
        return 0
    else:
        return tamanho(cauda(lista)) + 1

def menor(l):
    if tamanho(l) == 1:
        return cabeca(l)
    cb = cabeca(l)
    menor_cd = menor(cauda(l))
    if cb < menor_cd:
        return cb
    else:
        return menor_cd

def retElem(l, x):
    if x == cabeca(l):
        return cauda(l)
    else:
        primeiro = cabeca(l)
        resto = retElem(cauda(l), x)
        resultado = [primeiro] + resto
        return resultado

def selecao(l):
    if not l:
        return []
    else:
        menor_elem = menor(l)
        resto = retElem(l, menor_elem)
        resultado = [menor_elem] + selecao(resto)
        return resultado

# Exemplo de uso:
print(selecao([4, 2, 1, 7, 6]))  # Resultado esperado: [1, 2, 4, 6, 7]
# Pode ser alterado para testar cada função
