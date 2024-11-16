import numpy as np

# Данные
X = np.array([51, 67, 84, 81, 101, 109, 71, 97, 109, 51, 105, 89])
Y = np.array([25, 30, 43, 44, 57, 58, 43, 46, 62, 45, 55, 45])

# Средние значения
mean_X = np.mean(X)
mean_Y = np.mean(Y)

# Коэффициент наклона (k)
k = np.sum((X - mean_X) * (Y - mean_Y)) / np.sum((X - mean_X)**2)

# Свободный член (b)
b = mean_Y - k * mean_X

# Сумма модулей параметров
sum_abs_params = abs(k) + abs(b)
print(k)
print(b)
print(sum_abs_params)

# http://www.mathprofi.ru/linejnyj_koefficient_korrelyacii.html