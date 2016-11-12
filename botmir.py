import telebot
import config

# Настраиваем соединение с нашим ботом

bot = telebot.TeleBot(config.token)

# Бот отвечает на команды

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

# Бот отвечает на все сообщения по умолчанию

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)

# запускаем бота

bot.polling()
