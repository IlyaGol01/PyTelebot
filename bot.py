import telebot
from bot_logic import gen_pass, flip_coin, gen_emodji
from config import api_token


bot = telebot.TeleBot(api_token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
        bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")
    
@bot.message_handler(commands=['hello'])
def send_hello(message):
        bot.reply_to(message, "Привет! Как дела?")
    
@bot.message_handler(commands=['bye'])
def send_bye(message):
        bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['commands'])
def send_commands(message):
        bot.reply_to(message, "Cписок комманд: /bye /hello /start /commands")

@bot.message_handler(commands=['password'])
def send_password(message):
        bot.reply_to(message, gen_pass(7))

@bot.message_handler(commands=['emodji'])
def send_emodji(message):
        bot.reply_to(message, gen_emodji())

@bot.message_handler(commands=['coin'])
def send_coin(message):
        bot.reply_to(message, flip_coin())
    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
        bot.reply_to(message, message.text)


bot.polling()
