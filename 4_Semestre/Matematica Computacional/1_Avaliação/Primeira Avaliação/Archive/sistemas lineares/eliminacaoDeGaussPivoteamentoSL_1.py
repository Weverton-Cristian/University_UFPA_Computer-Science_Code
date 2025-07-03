import numpy as np

def eliminacaoDeGaussPivoteamento(A, b):
    """
    Resolve um sistema linear Ax = b usando o método de eliminação de Gauss
    com pivoteamento parcial.

    :param A: Matriz dos coeficientes (numpy.ndarray)
    :param b: Vetor das constantes (numpy.ndarray)
    :return: Vetor solução x (numpy.ndarray)
    """
    n = len(b)
    A = A.astype(float)  # Garante que os cálculos sejam feitos com ponto flutuante
    b = b.astype(float)

    # tranformando A em uma matriz triangular superior
    for k in range(n - 1):
        # Pivoteamento parcial: encontra o maior elemento na coluna k
        max_row = k + np.argmax(np.abs(A[k:, k]))
        if max_row != k:
            # Troca as linhas para colocar o maior elemento como pivô
            A[[k, max_row]] = A[[max_row, k]]
            b[[k, max_row]] = b[[max_row, k]]

        print("Quantidade de Interações:", k)

        # Eliminação para zerar os elementos abaixo do pivô
        for i in range(k + 1, n):
            m = A[i, k] / A[k, k]
            A[i, k:] -= m * A[k, k:]
            b[i] -= m * b[k]


    # Substituição regressiva para encontrar as soluções
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        s = np.dot(A[i, i + 1:], x[i + 1:])
        x[i] = (b[i] - s) / A[i, i]

    return x

def main():

    # Entrada: matriz dos coeficientes e vetor das constantes
    A = np.array([[15, -1, 0, 0, 4],
              [-1, 20, -1, 0, 3],
              [0, -1, 23, -1, 2],
              [0, 0, -1, 27, 2],
              [1, 2, 3, 4, 30]])  # Matriz dos coeficientes

    b = np.array([15, 10, 10, 10,10])  # Vetor das constantes

    # Solução
    x = eliminacaoDeGaussPivoteamento(A, b)

    print("Solução:", x)

main()
