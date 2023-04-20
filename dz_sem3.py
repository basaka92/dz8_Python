import json


def task1():
    try:
        N = int(input("Введите целое число больше нуля: "))
        if N <= 0:
            print("Вы ввели число меньше либо равное нулю!")
            return
        fibonachiList = [1]
        prevNumber = 0
        currNumber = 1
        for _ in range(N-1):
            nextNumber = prevNumber + currNumber
            fibonachiList.append(prevNumber + currNumber)
            prevNumber = currNumber
            currNumber = nextNumber
        print(f"{N} первых элементов последовательности Фибоначчи: ", end="")
        print(*fibonachiList)
    except ValueError:
        print("Вы ввели данные не верного типа!")


def task2():
    fruitList = [
        "яблоко",
        "абрикос",
        "авокадо",
        "банан",
        "бергамот",
        "дуриан",
        "грейпфрут",
        "киви",
        "лайм",
        "лимон",
        "локва",
        "манго",
        "дыня",
        "нектарин",
        "апельсин",
        "маракуйя",
        "папайя",
        "персик",
        "груша",
        "хурма",
        "ананас",
        "слива",
        "гранат",
        "помело",
        "мандарин",
        "айва"
    ]
    letter = input("Введите первую букву названия фрукта: ")
    if len(letter) > 1:
        print("Вы ввели больше одного символа!")
        return
    result = []
    for fruit in fruitList:
        if fruit[0] == letter:
            result.append(fruit)
    if len(result) == 0:
        print("Таких фруктов нет в списке!")
    else:
        print("Подходящие фрукты:", end=" ")
        print(*result, sep=", ", end=".")


def task3():
    botD = open("bot.txt").read()
    botDictRes = json.loads(botD)
    check = False
    loop = True
    print("Добро пожаловать в программу Bot. Для завершения работы программы введите слово 'стоп'.")
    while loop == True:
        text = input("(Bot) Введите ваше сообщение и я отвечу на него: ")
        if text.lower() == "стоп":
            return
        for key, value in botDictRes.items():
            if key == text.lower():
                print(f"(Bot) {value}")
                check = True
        if check == False:
            print(
                "(Bot) Я не знаю как ответить на ваше сообщение, но могу научиться делать это.")
            print(
                "Введите какой бы ответ на данный вопрос вы бы хотели от меня услышать: ", end="")
            botDictRes[text.lower()] = input()
            json.dump(botDictRes, open("bot.txt", "w"))
        check = False