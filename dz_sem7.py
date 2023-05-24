import telebot
import random


def my_map(func, obj):
    new_obj = []
    for elem in obj:
        new_obj.append(func(elem))
    return new_obj


def decorator_repeat(count):
    def my_decorator(func):
        def decorator(*args):
            for _ in range(count):
                func(*args)
        return decorator
    return my_decorator


bot = telebot.TeleBot("6134436206:AAEwRTxQJJHnD8KjTFkq-HNHvosXak-S35s")

number = 0
count = 1


@bot.message_handler(commands=['startgame'])
def send_welcome(message):
    bot.reply_to(message, "Сейчас я загадаю число. Попробуй угадать!")
    global number
    number = random.randint(1, 1000)


@bot.message_handler(content_types=['text'])
def speak(message):
    global count
    text = message.text
    if str(number) in text:
        bot.reply_to(
            message, f"Вы угадали число, {message.from_user.first_name}. Сделано попыток: {count}.")
        count = 0
    else:
        bot.reply_to(
            message, f"Это не то число, {message.from_user.first_name}")
        count += 1


bot.polling()
