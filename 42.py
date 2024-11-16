X_values = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0]
Y_values = [0.4, 0.3, 1.0, 1.7, 2.1, 3.4, 4.1, 5.8, 7.7, 9.4, 11.4, 13.6, 15.6, 18.6, 21.2, 24.1]

def calculate_betas(X_values, Y_values, m):
    n = len(X_values)
    
    X = [[x**j for j in range(m + 1)] for x in X_values]
    
    Y = [[y] for y in Y_values]
    
    XT = [[X[j][i] for j in range(n)] for i in range(m + 1)]
    
    XT_X = [[sum(XT[i][k] * X[k][j] for k in range(n)) for j in range(m + 1)] for i in range(m + 1)]
    
    XT_Y = [[sum(XT[i][k] * Y[k][0] for k in range(n))] for i in range(m + 1)]
    
    def invert_matrix(matrix):
        size = len(matrix)
        identity = [[1 if i == j else 0 for j in range(size)] for i in range(size)]
        for i in range(size):
            diag = matrix[i][i]
            for j in range(size):
                matrix[i][j] /= diag
                identity[i][j] /= diag
            for k in range(size):
                if k != i:
                    factor = matrix[k][i]
                    for j in range(size):
                        matrix[k][j] -= factor * matrix[i][j]
                        identity[k][j] -= factor * identity[i][j]
        return identity
    
    XT_X_inv = invert_matrix(XT_X)
    
    beta = [sum(XT_X_inv[i][j] * XT_Y[j][0] for j in range(m + 1)) for i in range(m + 1)]
    
    return beta

m = 2

betas = calculate_betas(X_values, Y_values, m)

print(betas)
