import numpy as np
import matplotlib.pyplot as plt

# Данные
X = np.array([0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0])
Y = np.array([0.4, 0.3, 1.0, 1.7, 2.1, 3.4, 4.1, 5.8, 7.7, 9.4, 11.4, 13.6, 15.6, 18.6, 21.2, 24.1])

# Ввод степени полинома
m = 3  # Можно изменить или сделать вводимым пользователем

# Построение матрицы Х для полиномиальной регрессии
X_matrix = np.vander(X, N=m + 1, increasing=True)

# Решение методом наименьших квадратов
beta = np.linalg.lstsq(X_matrix, Y, rcond=None)[0]

# Построение прогнозных значений
Y_pred = X_matrix @ beta

# Визуализация
plt.scatter(X, Y, color="blue", label="Исходные данные")
plt.plot(X, Y_pred, color="red", label=f"Полиномиальная регрессия (степень {m})")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Полиномиальная регрессия")
plt.legend()
plt.grid(True)
plt.show()

# Вывод коэффициентов
beta

# Вопросы?