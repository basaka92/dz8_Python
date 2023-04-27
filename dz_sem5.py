import random


def task1():
    numbersList = [random.randint(1, 10) for _ in range(10)]
    print("Начальный список: ", end="")
    print(*numbersList, sep=", ")
    numbersList = filter(lambda elem: elem > 5, numbersList)
    print("Конечный список (только элементы больше 5): ", end="")
    print(*numbersList, sep=", ")


def task2():
    numbersList = [random.randint(1, 20) for _ in range(10)]
    print("Список: ", end="")
    print(*numbersList)
    sequence = []
    while len(sequence) < 2:
        start = random.randint(0, 9)
        sequence = [numbersList[start]]
        for element in numbersList[start:]:
            if element > sequence[-1]:
                rand = random.randint(0, 1)
                if len(sequence) == 1 or rand == 1:
                    sequence.append(element)
    print("Случайная возрастающая последовательность для данного списка: ", end="")
    print(*sequence)


def task3():
    numbersList = [random.randint(1, 10) for _ in range(10)]
    print("Начальный список: ", end="")
    print(*numbersList, sep=", ")
    count = 0
    resList = []
    for number in numbersList:
        if numbersList.count(number) > 1:
            count += 1
            if resList.count(number) == 0:
                resList.append(number)
        else:
            resList.append(number)

    print(f"Количество совпадающих элементов: {count}")
    print("Конечный список: ", end="")
    print(*resList, sep=", ")

