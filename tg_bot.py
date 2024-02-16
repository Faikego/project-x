import telebot
from Css import token
from initializer import initializer

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = ("Введите '/search название товара котрый хотите найти.'")
    bot.reply_to(message, text)


@bot.message_handler(commands=['search'])
def search(message):

    keywords = message.text[8:]

    if not keywords:
        bot.reply_to(message, "Пожалуйста, укажите ключевые слова для поиска")
    else:
        bot.reply_to(message, 'Поиск займет около 2 минут')
        bot.reply_to(message, initializer(keywords))


bot.polling(none_stop=True)


