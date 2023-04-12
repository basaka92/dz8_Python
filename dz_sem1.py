def task1():
    try:
        numberDay = int(input("Введите номер дня недели (целое число): "))
        daysDict = {
            1: "Понедельник",
            2: "Вторник",
            3: "Среда",
            4: "Четверг",
            5: "Пятница",
            6: "Суббота",
            7: "Воскресенье"
        }
        if numberDay in daysDict:
            print(f"Это {daysDict[numberDay]}.")
        else:
            print("Такого дня недели не существует!")
    except ValueError:
        print("Неверный тип введёных данных!")


def task2():
    try:
        xFirstPoint = float(input("Введите координату X первой точки: "))
        yFirstPoint = float(input("Введите координату Y первой точки: "))
        xSecondPoint = float(input("Введите координату X второй точки: "))
        ySecondPoint = float(input("Введите координату Y второй точки: "))
        distance = (
            ((xSecondPoint-xFirstPoint)**2) +
            ((ySecondPoint-yFirstPoint)**2)
        )**0.5
        if distance == 0:
            print("Заданные точки совпадают!")
        else:
            print(f"Расстояние между двуия точками равно {distance}")
    except ValueError:
        print("Неверный тип введёных данных!")

def task3():
    try:
        quarter = int(input("Введите номер четверти (целое число): "))
        coordDict = {
            1: "x>0, y>0",
            2: "x<0, y>0",
            3: "x<0, y<0",
            4: "x>0, y<0"
        }
        if quarter in coordDict:
            print(
                f"Диапазон возможных координат в {quarter} четверти: " + coordDict[quarter])
        else:
            print("Четверти под таким номер не существует!")
    except ValueError:
        print("Неверный тип введёных данных!")


def task4():
    try:
        N = int(input("Введите конец промежутка (положительное число больше нуля): "))
        count = 2
        listRes = [2]
        if N == 1:
            print(f"Не существут чётных чисел в заданном промежутке!")
        elif N <= 0:
            print("Введено число меньше либо равное нулю!")
        else:
            while count < N and count != N-1:
                count += 2
                listRes.append(count)
            print(f"Чётные числа от 1 до {N}: {listRes}")
    except ValueError:
        print("Неверный тип введёных данных!")

