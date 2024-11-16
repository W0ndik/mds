import numpy as np

# Данные
X = np.array([51, 67, 84, 81, 101, 109, 71, 97, 109, 51, 105, 89])
Z = np.exp(X*0.1)
print(Z)
Y = np.array([25, 30, 43, 44, 57, 58, 43, 46, 62, 45, 55, 45])

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