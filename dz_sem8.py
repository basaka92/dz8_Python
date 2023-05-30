import numpy as np
import random


def task1(obj):
    count = 0
    uniq_elements, uniq_counts = np.unique(obj, return_counts=True)
    for elem in uniq_counts:
        if elem == 1:
            count += 1
    print(f"Количество уникальных элементов в списке: {count}")


def task2():
    rows = 4
    columns = 4
    array = np.random.randint(1, 3, [rows, columns])
    print(array)
    corrcoef_array = np.corrcoef(array)
    check = False
    print(corrcoef_array)
    for row in range(rows):
        if 1 in corrcoef_array[row, row+1:]:
            check = True
    if check == True:
        print("В этом массиве есть одинаковые строки.")
    else:
        print("В этом массиве нет одинаковых строк.")


def task3():
    rows = columns = random.randint(2, 5)
    array = np.random.randint(1, 10, [rows, columns])
    print(array)
    min_index = np.unravel_index(np.argmin(array), array.shape)
    max_index = np.unravel_index(np.argmax(array), array.shape)
    print(
        f"Индексы минимального и макисмального элементов массива равны соответственно: {min_index, max_index}")
    print(
        f"Элементы главной диагонали массива: {np.diagonal(array, offset=0)}")
