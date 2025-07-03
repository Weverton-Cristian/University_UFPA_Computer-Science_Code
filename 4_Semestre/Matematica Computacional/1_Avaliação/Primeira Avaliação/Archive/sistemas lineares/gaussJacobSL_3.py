import numpy as np

def gaussJacob(A, b, tol=1e-6, max_iter=100):
    """
    Método iterativo de Gauss-Jacobi para resolver sistemas lineares.

    Parâmetros:
        A (ndarray): Matriz de coeficientes (n x n).
        b (ndarray): Vetor de constantes (n x 1).
        tol (float): Tolerância para o critério de parada.
        max_iter (int): Número máximo de iterações.

    Retorna:
        x (ndarray): Solução aproximada do sistema.
        convergiu (bool): Indica se o método convergiu.
    """
    n = len(b)
    x = np.zeros_like(b, dtype=np.float64)  # Aproximação inicial
    x_new = np.zeros_like(x)

    # Verificar critério de convergência
    for i in range(n):
        if abs(A[i, i]) <= sum(abs(A[i, j]) for j in range(n) if j != i): # Ocorre quando a soma das matrizes supera a diagonal principal.
            raise ValueError("Critério de convergência não satisfeito. Reorganize a matriz.")

    # Iteração do método
    for k in range(max_iter):
        for i in range(n):
            sum_ = sum(A[i, j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - sum_) / A[i, i]

        # Verificar tolerância
        if np.max(np.abs(x_new - x)) < tol:
            return x_new, True

        print("Quantidade de Interações:", k)

        x = x_new.copy()

    return x, False  # Retorna False se não convergiu

# Exemplo de uso
A = np.array([[15, -1, 0, 0, 4],
              [-1, 20, -1, 0, 3],
              [0, -1, 23, -1, 2],
              [0, 0, -1, 27, 2],
              [1, 2, 3, 4, 30]], dtype=np.float64) # Se aumentarmos a matrix A, temos que aumentar no vetor B.

b = np.array([15, 10, 10, 10,10], dtype=np.float64)

x, convergiu = gaussJacob(A, b)

if convergiu:
    print("Solução encontrada:", x)
else:
    print("O método não convergiu com os parâmetros fornecidos.")

