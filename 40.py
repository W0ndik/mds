import numpy as np

A = np.array([
    [4, -1, 0, -1, 0, -1],
    [-1, 4, -1, 0, -1, 0],
    [0, -1, 4, 0, 0, -1],
    [-1, 0, 0, 4, -1, 0],
    [0, -1, 0, -1, 4, -1],
    [0, 0, -1, 0, -1, 4]
], dtype=float)
b = np.array([0, 5, 0, 6, -2, 6])

def manual_norm(vector):
    return np.sqrt(sum(v**2 for v in vector))

y = np.zeros(6)

tolerance = 1e-6
max_iterations = 1000
iteration = 0

while True:
    grad = 2 * A @ y - 2 * b
    grad_norm = manual_norm(grad)
    
    if grad_norm < tolerance or iteration >= max_iterations:
        break
    
    grad_A_grad = sum(g1 * sum(A[i][j] * g2 for j, g2 in enumerate(grad)) for i, g1 in enumerate(grad))
    alpha = grad_norm**2 / (2 * grad_A_grad)
    y = [yi - alpha * gi for yi, gi in zip(y, grad)]
    iteration += 1

extremum_norm = manual_norm(y)
print(extremum_norm)
