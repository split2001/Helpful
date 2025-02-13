from random import random

import numpy as np

arr =  np.array([1, 2, 3, 4, 5])  # создание массива
arr_2 = np.array([[1, 2, 3,],[4, 5, 6]])  # создание двумерного массива
print(arr_2)
print(arr)
print(type(arr))

ones = np.ones((2, 4))  # 2x4 массив из единиц
print(ones)

zeros = np.zeros((3, 3))  # 3x3 массив из нулей
print(zeros)

arr1 = np.arange(0, 11, 2)  # Числа от 0 до 10 с шагом 2
print(arr1)

# arr2 = np.linspace(0, 5, 10)  # 10 чисел от 0 до 5 равномерно
# print(arr2)


rand1 = np.random.rand(3, 3)  # 3x3 массив случайных чисел от 0 до 1
print(rand1)

rand2 = np.random.randint(1, 10, (2, 2))  # 2x2 массив случайных целых чисел от 1 до 10
print(rand2)

arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr.shape)  # Размерность массива
print(arr.size)   # Количество элементов
print(arr.dtype)  # Тип данных элементов

''' Работа со срезами в массивах '''
arr = np.array([10, 20, 30, 40, 50])

print(arr[0])  # Первый элемент (10)
print(arr[-1])  # Последний элемент (50)
print(arr[2:])  # Срез с третьего элемента до конца ([30, 40, 50])
print(arr[:3])  # Первые три элемента ([10, 20, 30])
print(arr[1:4:2])  # От второго до четвертого с шагом 2 ([20, 40])


''' Работа со срезами в двумерных массивах '''

matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print(matrix[0, 0])  # Первый элемент (1)
print(matrix[1, -1])  # Последний элемент второй строки (6)
print(matrix[0, :])  # Вся первая строка ([1, 2, 3])
print(matrix[:, 1])  # Все элементы второго столбца ([2, 5, 8])
print(matrix[1:, :2])  # Нижние две строки, первые два столбца ([[4, 5], [7, 8]])


'''Изменение элементов в массивах '''

arr = np.array([10, 20, 30, 40, 50])
arr[1] = 99  # Меняем второй элемент
print(arr)  # [10, 99, 30, 40, 50]

matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix)
matrix[0, 1] = 99  # Меняем элемент в первой строке, втором столбце
print(matrix)


'''Фильтрация в массивах '''

arr = np.array([10, 20, 30, 40, 50])

mask = arr > 25  # Создаем маску для чисел больше 25
print(arr[mask])  # Выводит только [30, 40, 50]

# Еще пример:
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix[matrix > 3])  # Выведет только [4, 5, 6]


'''Логические операторы'''

arr = np.array([10, 20, 30, 40, 50])

# Выбрать элементы больше 15 и меньше 45
print(arr[(arr > 15) & (arr < 45)])  # [20 30 40]

# Выбрать элементы меньше 20 или больше 40
print(arr[(arr < 20) | (arr > 40)])  # [10 50]

# Выбрать элементы НЕ больше 30 (т.е. меньше или равные 30)
print(arr[~(arr > 30)])  # [10 20 30]

''' Задача '''

arr = np.array([12, 25, 37, 45, 53, 62, 78])
mask =  (arr > 30) & (arr % 3 !=0)
arr = np.array([12, 25, 37, 45, 53, 62, 78])
arr[arr % 2 == 0] = 100
print(arr[mask])
print(arr)


'''Преобразование одномерного массива в матрицу'''

arr = np.array([1, 2, 3, 4, 5, 6])
reshaped = arr.reshape(2, 3)  # Делаем из 1D массива (6,) матрицу 2x3
reshaped2 = arr.reshape(-1, 2)  # NumPy сам подберёт число строк -1 означает: «Подбери количество строк автоматически».
print(arr)
print(reshaped)
print(reshaped2)


'''Преобразование матрицы в одномерный массива  '''
matrix = np.array([[1, 2, 3], [4, 5, 6]])

flat1 = matrix.ravel()  # "Сплющивание" массива (быстрое представление)
flat2 = matrix.flatten()  # То же самое, но создаёт копию данных

print(flat1)  # [1 2 3 4 5 6]
print(flat2)  # [1 2 3 4 5 6]


'''Объединение массивов (hstack, vstack, concatenate)  '''

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

horiz = np.hstack((arr1, arr2))
vert = np.vstack((arr1, arr2))
print(vert)
print(horiz)  # [1 2 3 4 5 6]


arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6]])

concat1 = np.concatenate((arr1, arr2), axis=0)  # По строкам
print(concat1)

concat2 = np.concatenate((arr1, arr2.T), axis=1)  # По столбцам (T - транспонирование)
print(concat2)

'''Разъединение массивов (hstack, vstack, concatenate)  '''

arr = np.array([10, 20, 30, 40, 50, 60])
parts = np.split(arr, 3)  # Разбиваем на 3 части
print(parts)

matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8]])

split_h = np.hsplit(matrix, 2)  # Разбиваем на 2 части по столбцам
print(split_h)


split_v = np.vsplit(matrix, 2)  # Разбиваем по строкам
print(split_v)


'''Задание '''

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])  # создаем массив
print(arr)
matrix = arr.reshape(4,3)  # преобразуем в матрицу 3х4
print(matrix)
split_mt = np.hsplit(matrix,3)  # разъединяем матрицу
print(split_mt)
concat_mt = np.concatenate(split_mt, axis=1)  # объединяем матрицу
print(concat_mt)
transposed = concat_mt.T   # транспонировать матрицу (строки становятся столбцами, а столбы строками)
print(transposed)



'''Арифметические операции ''' # количество элементов должно совпадать
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([10, 20, 30, 40])

print(arr1 + arr2)  # [11 22 33 44]
print(arr1 - arr2)  # [-9 -18 -27 -36]
print(arr1 * arr2)  # [10 40 90 160]
print(arr1 / arr2)  # [0.1 0.1 0.1 0.1]
print(arr1 ** 2)    # [ 1  4  9 16] (возведение в квадрат)

''' операции с числами'''
arr = np.array([1, 2, 3, 4])

print(arr + 10)  # [11 12 13 14] (прибавляет 10 к каждому элементу)
print(arr * 3)   # [ 3  6  9 12] (умножает каждый элемент на 3)
print(arr / 2)   # [0.5 1.0 1.5 2.0] (делит каждый элемент на 2)

''' агрегатные функции'''

arr = np.array([5, 10, 15, 20, 25])

print(arr.sum())       # 75 (сумма всех элементов)
print(arr.mean())      # 15.0 (среднее значение)
print(arr.min())       # 5 (минимальное)
print(arr.max())       # 25 (максимальное)
print(arr.std())       # 7.07 (стандартное отклонение)
print(arr.var())       # 50.0 (дисперсия)


''' Задание'''

arr = np.arange(1,11)
arr_2 = arr * 5
summa = arr_2.sum()
middle = arr_2.mean()
std = arr_2.std()
print(summa)
print(arr_2)
print(arr)

# Одно случайное число из нормального распределения
print(np.random.randn())

# Массив из 5 случайных чисел из нормального распределения
print(np.random.randn(5))

# Матрица 3x3 из нормального распределения
print(np.random.randn(3, 3))


''' Задание'''
matrix = np.random.randint(0,50,(4,4))
matrix_2 = np.random.normal(loc=5, scale=2, size=10)  # Среднее = 5, отклонение = 2
print(matrix)
print(matrix_2)

np.random.seed(7)  # Фиксируем случайность. указываем точку старта
print(np.random.randint(0,100,3))  # Эти числа будут одинаковыми при каждом запуске



np.random.seed(100)
print(np.random.rand(4))
np.random.seed(100)
print(np.random.rand(4))


''' Задание'''
arr = np.arange(10, 50, 5)
print(arr * 2)
print(arr.sum())

arr2 = np.random.randint(1, 100, 15)
print(arr2[:5])
mask = arr2 % 2 == 0
print(arr2[mask])
arr2[arr2 > 50] = -1
print(arr2)

matrix = np.random.randint(1,20,(3,3))
print(matrix)
rows_sum = np.sum(matrix,axis=1)
print(rows_sum)
transposed = matrix.T
print(transposed)


arr = np.random.normal(loc=50, scale=10, size =1000)
print(arr.std())
print(arr.mean())
median = np.median(arr)
print(median)

matrix = np.random.randint(1, 100, (5,5))
mean = matrix.mean()
max_index = np.argmax(matrix)
print(max_index)
matrix[matrix > mean] = 0
print(matrix)

arr = np.random.randint(0, 100, 500)
print(arr.max())
print(arr.min())
print(arr.mean())
mediana = np.median(arr)
percentile= np.percentile(arr,[25, 75])
print(mediana)
print(percentile)


matrix = np.random.randint(1,100,(6,6))
summ = np.trace(matrix)  # сумма элементов на главное диагонали
print(summ)
matrix[matrix % 2 == 0] = 0
print(matrix)



arr = np.random.randint(-10,35,365)
print(arr.max())
arr_mean = arr.mean()
matrix = arr[:360].reshape(12,30)
mean_temp = np.mean(matrix,axis=1)
top_temp = np.where(mean_temp > arr_mean)[0]
print(top_temp)

matrix_2 = arr[:360].reshape(4,90)
mean_temp_year = np.mean(matrix_2, axis=1)
top_temp_year = np.where(mean_temp_year > arr_mean)[0]
print(top_temp_year)

''' #2'''

matrix = np.random.randint(0,100,(6,2))  # Доходы
matrix_2 = np.random.randint(0,100,(6,2))  # Расходы

mean1 = np.mean(matrix, axis=1)
mean2 = np.mean(matrix_2, axis=1)
profit = mean1 - mean2
print("Прибыль по месяцам:",profit)

best_month = np.argmax(profit)
print('Месяц с наибольшей прибылью:',best_month)


''' #2'''
start = np.datetime64('2024-01-01')
end = np.datetime64('2024-12-31')
arr = np.random.choice(np.arange(start, end, dtype ='datetime64[D]'), size=10)
print('Массив:')
timestamps = arr.astype('datetime64[s]').astype(int)
print(arr)
print(timestamps)
arr_max = arr.max()
arr_min = arr.min()
dif = arr_max - arr_min
print(dif)

sorted_arr = np.sort(arr)
diffs = np.diff(sorted_arr)  # находим разницы между соседними датами (это массив временных дельт).
print(diffs.mean())


''' #2'''

arr = np.random.randint(0,100,500)
print('Средний балл:',arr.mean())
mask = arr > arr.mean()
print(arr[mask].size)
arr_min = arr[arr < 40].size
print((arr_min / 500) *100)



''' #2'''

matrix = np.random.randint(0,50,(30,1))
print(matrix)
summa = matrix.sum()
print(summa)
max_day = np.argmax(matrix)
print(max_day)

mediana = np.median(matrix)
print(mediana)