import numpy as np

X = np.array([2.11, 2.45, 2.61, 2.73, 2.75, 2.81, 2.87, 2.91, 2.96, 3.03, 3.05, 3.12])
Y = np.array([0.10, 0.21, 0.43, 0.51, 0.62, 0.81, 1.01, 1.23, 1.47, 1.53, 1.75, 2.25])

X1 = X 
X2 = np.sin(8 * X) 
X0 = np.ones(len(X))

X_matrix = np.vstack([X0, X1, X2]).T

# β = (X^T * X)^(-1) * X^T * Y
coefficients = np.linalg.inv(X_matrix.T @ X_matrix) @ X_matrix.T @ Y

beta_0, beta_1, beta_2 = coefficients
print(beta_0)
print(beta_1)
print(beta_2)

