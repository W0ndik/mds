import numpy as np

# Заданные параметры задачи
A = np.array([
    [4, -1, 0, -1, 0, -1],
    [-1, 4, -1, 0, -1, 0],
    [0, -1, 4, 0, 0, -1],
    [-1, 0, 0, 4, -1, 0],
    [0, -1, 0, -1, 4, -1],
    [0, 0, -1, 0, -1, 4]
], dtype=float)

b = np.array([0, 5, 0, 6, -2, 6], dtype=float)
y0 = np.zeros(6)  # начальная точка
epsilon = 1e-6  # точность

# Функция для вычисления градиента
def gradient(y):
    return 2 * A @ y - 2 * b

# Метод скорейшего спуска
def steepest_descent(A, b, y0, epsilon):
    y = y0
    grad = gradient(y)
    iterations = 0
    while np.linalg.norm(grad) > epsilon:
        # Оптимальный шаг
        alpha = np.dot(grad, grad) / (2 * np.dot(grad, A @ grad))
        # Обновляем точку
        y = y - alpha * grad
        # Пересчитываем градиент
        grad = gradient(y)
        iterations += 1
    return y, iterations

# Поиск минимума
y_min, num_iterations = steepest_descent(A, b, y0, epsilon)

# Вычисление нормы ||X*||_2
norm_result = np.linalg.norm(y_min)
y_min, norm_result

print(norm_result)

# Вопросы?