import telebot
import config
import search

# Настраиваем соединение с нашим ботом

bot = telebot.TeleBot(config.token)

# Бот отвечает на команды

#стандартный вывод клавиатуры
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я маленький бот Мирчеус!")
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row('/start', 'stop')
    user_markup.row('Заполнить анкету')
    user_markup.row('Найти анкету по имени')
    bot.send_message(message.from_user.id, 'Добро пожаловать...', reply_markup=user_markup)


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, search.qna(message.text))



# @bot.message_handler(content_types="text")
# def handle_text(message):
#     if message.text == 'Заполнить анкету':
#         search.qna(message.text)




@bot.message_handler(content_types="text")
def handle_text(message):
    if message.text == 'Заполнить анкету':
        bot.send_message(message.from_user.id, 'Введите своё имя')
        @bot.message_handler(content_types="text")
        def handle_text(message):
            name = message.text
            bot.send_message(message.from_user.id, 'Вы ввели ' + message.text)


@bot.message_handler(content_types="text")
def handle_text(message):
    name = message.text
    bot.send_message(message.from_user.id, 'Вы ввели вот эту инфу - ' + message.text)

# запускаем бота
bot.polling(none_stop=True)
