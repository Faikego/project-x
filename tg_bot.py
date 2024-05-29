import telebot
from initializer import initializer
token_telega='6451064217:AAGw4nf-4IKVDknIii7HrILbp2g6dsfZUaQ'
bot = telebot.TeleBot(token_telega)

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


