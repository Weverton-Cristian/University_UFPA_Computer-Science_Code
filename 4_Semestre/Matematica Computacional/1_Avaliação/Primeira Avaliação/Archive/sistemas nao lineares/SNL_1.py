import numpy as np

def F(x):
    """ Define o sistema de equações não lineares. """
    f1 = x[0]**2 + x[1]**2 - 2  # Exemplo: x^2 + x^2 - 2 = 0, aqui escolhemos a primeira função
    f2 = np.exp(x[0])-1 + x[1]**3-2  # Exemplo: e^x-1 + x³ - 2 = 0, aqui escolhemos a segunda funçao
    return np.array([f1, f2])

def calcular_jacobiana(F, x, h=1e-6):
    """ Calcula a matriz Jacobiana numericamente. """
    n = len(x)
    J = np.zeros((n, n))
    for i in range(n):
        x_perturbado = x.copy()
        x_perturbado[i] += h
        J[:, i] = (F(x_perturbado) - F(x)) / h
    return J

def metodo_de_newton(F, J, x0, epsilon1=1e-1, epsilon2=1e-1, max_iter=100):
    """ Resolve um sistema de equações não lineares usando o método de Newton. """
    x = x0
    for k in range(max_iter):
        Fx = F(x)
        if np.linalg.norm(Fx, np.inf) < epsilon1:
            print(f"Solução encontrada após {k} iterações.")
            return x
        
        Jx = J(F, x)  # Calcula a Jacobiana
        s = np.linalg.solve(Jx, -Fx)  # Resolve J(x) * s = -F(x)
        
        x_new = x + s
        if np.linalg.norm(x_new - x, np.inf) < epsilon2:
            print(f"Solução encontrada após {k} iterações.")
            return x_new
        
        x = x_new
    
    print("Número máximo de iterações atingido.")
    return x

# Aproximação inicial
x0 = np.array([0.5, 0.5])

# Resolve o sistema
solucao = metodo_de_newton(F, calcular_jacobiana, x0)

print("Solução aproximada:", solucao)
print("Provando que x e y são soluçao (=0)", solucao[0]**2 + solucao[1]**2 - 1  )
