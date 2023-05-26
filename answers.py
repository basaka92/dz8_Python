import telebot

bot = telebot.TeleBot("6134436206:AAEwRTxQJJHnD8KjTFkq-HNHvosXak-S35s")

with open("log.txt", mode="r", encoding="utf-8") as data:
    answers_list = data.read().split("\n")
data.close()
print("Список текущих сообщений от пользователей. Для завершения программы введите 'exit'. Для пропуска вопроса введите 'next'\n")
for item in answers_list[:-1]:
    id = item.split(": ", 1)[0]
    message = item.split(": ", 1)[1]
    print(f"ID пользователя: {id}")
    print(f"Сообщение пользователя: {message} \n")
    answer = input("Ваш ответ: ")
    if answer.lower() == "exit":
        break
    elif answer.lower() == "next":
        continue
    else:
        bot.send_message(chat_id=id, text=answer)
        list.remove(answers_list, item)
with open("log.txt", mode="w", encoding="utf-8") as data:
    for item in answers_list[:-1]:
        data.write(f"{item} \n")
