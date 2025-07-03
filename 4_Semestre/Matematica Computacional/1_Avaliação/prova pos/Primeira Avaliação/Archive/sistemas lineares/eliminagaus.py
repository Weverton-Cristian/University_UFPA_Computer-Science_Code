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
    A = np.array([[128,371, 300,77,15,68,118,275,262],
                  [2.5,10,8,0.6,1.1,2.0,25.7,29.9,32.1],
                  [0.2,1.3, 3.1,0.1,0.2,2.1,0.9,16.3,13.9],
                  [28.1,     77.9,     58.6,   18.4,  3.1,   12.3,        0,         0,      0],
                  [4,         17,       16,      17,   7,      5,       7,         4,     18],
                  [0.1,       0.9,       1.0,   0.2,   0.2,   0.6,       1.3,      2.8,    1.3],
                  [1,         7,        648,     3,    1,      2,         30,      51,      62],
                  [0.02,      0.15,     0.13,  0.06,   0.04,  0.19,      0.09,     0.08,    0.09],
                  [0.5,       0.8,      0.8,    0.1,   0.1,   0.4,       0.4,      6.7,    3.3]])  # Matriz dos coeficientes

    b = np.array([5756, 401, 98.8,782.8,344, 27, 1824,2.48, 35.8])  # Vetor das constantes

    # Solução
    x = eliminacaoDeGaussPivoteamento(A, b)

    print("Solução:", x)

main()
