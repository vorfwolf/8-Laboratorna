import numpy as np  #імпортуємо numpy
#4(у матриці 4*4, що задана користувачем замініть всі від’ємні елементи на 0)
t = np.array([[-1, 4, 5, 7], [3, -7, 8, -3], [4, 6, -7, 9], [2, -3, 6, 1]])  #задана матриця 4 на 4 числа
print(t)  #виведемо нашу початкову матрицю на екран
for i in range(len(t)):  #пройдемось по елементах матриці
 for j in range(len(t[i])):
  if t[i, j] < 0:  #якщо елементи матриці менше нуля, тобто вони від'ємні
   t[i, j] *= 0  #то ми замінюємо їх на нуль
   print(t)  #виводимо нашу обновлену матрицю
