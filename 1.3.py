import numpy as np  #імпортуємо numpy
#3(виконайте добуток двох квадратних матриць 3*3, врахуйте розмірність.
#Результати множення елементів занесіть до нової матриці та виведіть її на екран)
a = np.array([[3, 7, 1],[4, 2, 5],[2, 3, 8]])  #перша задана матриця 3 на 3
b = np.array([[-2, 5, 6],[1, -3, 3],[4, 8, -9]])  #друга задана матриця 3 на 3
print(a)  #виведемо нашу першу матрицю
print(b)  #виведемо нашу другу матрицю
c11 = a[0][0] * b[0][0] + a[0][1] * b[1][0] +a[0][2] * b[2][0]
c12 = a[0][0] * b[0][1] + a[0][1] * b[1][1] +a[0][2] * b[2][1]
c13 = a[0][0] * b[0][2] + a[0][1] * b[1][2] + a[0][2] * b[2][2]
c21 = a[1][0] * b[0][0] + a[1][1] * b[1][0] + a[1][2] * b[2][0]
c22 = a[1][0] * b[0][1] + a[1][1] * b[1][1] + a[1][2] * b[2][1]  #знайдемо за математичним алгоритмом
c23 = a[1][0] * b[0][2] + a[1][1] * b[1][2] + a[1][2] * b[2][2]  #елементи третьої матриці, яка є
c31 = a[2][0] * b[0][0] + a[2][1] * b[1][0] + a[2][2] * b[2][0]  #добутком двох попередніх
c32 = a[2][0] * b[0][1] + a[2][1] * b[1][1] + a[2][2] * b[2][1]
c33 = a[2][0] * b[0][2] + a[2][1] * b[1][2] + a[2][2] * b[2][2]
c = np.array([[c11, c12, c13],[c21, c22, c23],[c31, c32, c33]])  #наша третя матриця
print(c)  #вивід третьої матриці(добутку першої і другої)
