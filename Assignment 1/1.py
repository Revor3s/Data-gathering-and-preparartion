import numpy as np


# матрицы
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

# Линейная алгебра

# 1. Умножение матриц
matrix_multiplication = np.dot(matrix_a, matrix_b)

# 2. Транспонирование матрицы
transpose_a = np.transpose(matrix_a)

# 3. Определение обратной матрицы
inverse_a = np.linalg.inv(matrix_a)

# 4. Определение детерминанта матрицы
det_a = np.linalg.det(matrix_a)

# 5. Нахождение собственных значений и собственных векторов
eigenvalues, eigenvectors = np.linalg.eig(matrix_a)

# Вычисления
# 1. Производная через метод градиента
x = np.linspace(0, 10, 100)
y = np.sin(x)
dy_dx = np.gradient(y, x)

# 2. Интеграл методом трапеций
integral = np.trapz(y, x)

# 3. Полином и его производная
polynomial = np.poly1d([2, 3, -5])
poly_derivative = np.polyder(polynomial)

# 4. Интеграл полинома
poly_integral = np.polyint(polynomial)

# Статистика
# 1. Среднее значение
mean_value = np.mean(matrix_a)

# 2. Стандартное отклонение
std_value = np.std(matrix_a)

# 3. Дисперсия
variance_value = np.var(matrix_a)

# 4. Коэффициент корреляции
corrcoef_matrix = np.corrcoef(matrix_a)

# 5. Ковариационная матрица
cov_matrix = np.cov(matrix_a, rowvar=False)

print(f"Умножение матриц:\n{matrix_multiplication}")
print(f"Транспонированная матрица:\n{transpose_a}")
print(f"Обратная матрица:\n{inverse_a}")
print(f"Детерминант:\n{det_a}")
print(f"Собственные значения и векторы:\n{eigenvalues}\n{eigenvectors}")

