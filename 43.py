import numpy as np

# Данные
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
Z = np.log(X)
Y = np.array([2.11, 2.45, 2.61, 2.73, 2.75, 2.81, 2.87, 2.91, 2.96, 3.03, 3.05, 3.12])

mean_Z = np.mean(Z)
mean_Y = np.mean(Y)

# Коэффициент наклона (k)
k = np.sum((Z - mean_Z) * (Y - mean_Y)) / np.sum((Z - mean_Z)**2)

# Свободный член (b)
b = mean_Y - k * mean_Z

# Сумма модулей параметров
sum_abs_params = abs(k) + abs(b)
print(k)
print(b)
print(sum_abs_params)

# http://www.mathprofi.ru/linejnyj_koefficient_korrelyacii.html