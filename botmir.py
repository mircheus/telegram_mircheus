import telebot
import config
import search
import database

# Настраиваем соединение с нашим ботом
bot = telebot.TeleBot(config.token)
file = open('text.txt')
# Бот отвечает на команды

#Клавиатура для заполнения анкеты
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я маленький бот Мирчеус!")
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row('/start', 'stop')
    user_markup.row('Заполнить анкету')
    user_markup.row('Найти текст песни')
    bot.send_message(message.from_user.id, 'Добро пожаловать...', reply_markup=user_markup)

#Декоратор для ввода текста песни если была нажата кнопка
# 'Найти текст песни'
# @bot.message_handler(content_types=['text'])
# def handle_message(message):
#     if message == 'Найти текст песни':
#         bot.reply_to(message, search.find(message))



# Функция заполнения анкеты
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, search.qna(message.text))

#Декоратор для поиска текста песни по названию песни(Не работает)
@bot.message_handler(func=lambda m: True)
def second_echo_all(message):
    bot.reply_to(message, database.find_lyrics(message.text))

# Welcome-клавиатура
# @bot.message_handler(commands=['start'])
# def handle_start(message):
#     user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
#     user_markup.row('/start', '/stop')
#     user_markup.row('Найти текст песни')
#     bot.send_message(message.from_user.id, 'Добро пожаловать...', reply_markup=user_markup)

# Реакция на кнопку 'Найти текст песни'
# @bot.message_handler(content_types=['text'])
# def handle_message(message):
#     if message.text == 'Найти текст песни':
#         for line in file:
#             bot.send_message(message.from_user.id, line)


# запускаем бота
if __name__ == '__main__':
    bot.polling(none_stop=True)
