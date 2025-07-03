import numpy as np

def fatoracaoLuComPivoteamento(A, b):
    """
    Realiza a fatoração LU com pivoteamento parcial para resolver o sistema Ax = b.
    """
    n = len(A)
    L = np.eye(n)  # Matriz identidade inicial para L
    U = A.copy()
    P = np.eye(n)  # Matriz identidade para permutação
    p = list(range(n))  # Vetor de permutações

    # Fatoração LU com pivoteamento parcial
    for k in range(n - 1):
        # Encontra o maior pivô na coluna abaixo de k
        max_row = max(range(k, n), key=lambda i: abs(U[i][k]))
        if U[max_row][k] == 0:
            raise ValueError("A matriz é singular.")

        # Permutação das linhas
        if max_row != k:
            U[[k, max_row]] = U[[max_row, k]]
            P[[k, max_row]] = P[[max_row, k]]
            p[k], p[max_row] = p[max_row], p[k]

        # Atualização de L e U
        for i in range(k + 1, n):
            L[i][k] = U[i][k] / U[k][k]
            U[i, k:] -= L[i][k] * U[k, k:]

        print("Quantidade de Interações:", k)

    # Resolver o sistema com as matrizes L e U
    Pb = np.dot(P, b)

    # Solução de Ly = Pb
    y = np.zeros_like(b)
    for i in range(n):
        y[i] = Pb[i] - sum(L[i][j] * y[j] for j in range(i))

    # Solução de Ux = y
    x = np.zeros_like(b)
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - sum(U[i][j] * x[j] for j in range(i + 1, n))) / U[i][i]

    return L, U, P, x

# Exemplo de uso
A = np.array([[15, -1, 0, 0, 4],
              [-1, 20, -1, 0, 3],
              [0, -1, 23, -1, 2],
              [0, 0, -1, 27, 2],
              [1, 2, 3, 4, 30]], dtype=float)

b = np.array([15, 10, 10, 10,10], dtype=float)

L, U, P, x = fatoracaoLuComPivoteamento(A, b)

print("Matriz L:")
print(L)
print("\nMatriz U:")
print(U)
print("\nMatriz de permutação P:")
print(P)
print("\nSolução x:")
print(x)
