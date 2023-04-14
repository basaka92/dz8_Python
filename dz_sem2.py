def task1():
    try:
        factorialList = [1]
        N = int(input("Введите целое положительное число: "))
        multiplier = factorial = 1
        if N == 0:
            print(f"Факториал от нуля равен 1")
        elif N < 0:
            print(f"Вы ввели отрицательное число!")
        else:
            while multiplier < N:
                factorial *= multiplier+1
                multiplier += 1
                factorialList.append(factorial)
            print(f"Список факториалов от 1 до {N}: {factorialList}")
    except ValueError:
        print("Неверный тип введёных данных!")


def task2():
    print("x | y | z | ¬(X ∧ Y) ∨ Z")
    for x in range(2):
        for y in range(2):
            for z in range(2):
                print(f"{x} | {y} | {z} | {int(not(x and y) or z):^12}")


def task3():
    string1 = input("Введите первую строку: ")
    string2 = input("Введите вторую строку: ")
    print("Количество вхождений символов[] первой строки во вторую:", end=" ")
    duplicateList = []
    for elem1 in range(len(string1)):
        count = 0
        if not (string1[elem1] in duplicateList):
            for elem2 in range(len(string2)):
                if string1[elem1] == string2[elem2]:
                    count += 1
            duplicateList.append(string1[elem1])
            print(f"[{string1[elem1]}] - {count}", end="; ")


def task4():
    try:
        N = int(input("Введите целое положительное число больше нуля: "))
        if N <= 0:
            print("Введённое число меньше либо равно нулю!")
        else:
            numbersList = []
            for element in range(-N, N+1):
                numbersList.append(element)
            print(
                f"Список из элементов в промежутке [{-N},{N}]: {numbersList}")
            temp = numbersList[N*2-1:]
            numbersList[2:] = numbersList[:N*2-1]
            numbersList[:2] = temp
            print(
                f"Результат сдвига всех элементов списка на 2 позиции вправо: {numbersList}")
    except ValueError:
        print("Неверный тип введёных данных!")

