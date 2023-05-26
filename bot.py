import telebot

bot = telebot.TeleBot("6134436206:AAEwRTxQJJHnD8KjTFkq-HNHvosXak-S35s")


@bot.message_handler(content_types=['text'])
def write_message(message):
    data = open("log.txt", mode="a", encoding="utf-8")
    text = f"{message.from_user.id}: {message.text}\n"
    data.writelines(text)
    data.close()
    bot.reply_to(message, "Ваше сообщение принято. Ожидайте ответа.")


bot.polling()
