import telebot
from telebot import apihelper
import time


TOKEN = '985414696:AAHUu30CfqTXe6AQlEuHUAYa8zgoa3U9xa4'
BOT_URL = f'https://api.telegram.org/bot{TOKEN}'

proxies = {
    'http': 'http://163.172.168.124:3128',
    'https': 'http://163.172.168.124:3128',
}

apihelper.proxy = proxies
bot = telebot.TeleBot(TOKEN)
name = ''
surname = ''
age = 0

@bot.message_handler(commands= ['reg'])
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Как тебя зовут?")
        bot.register_next_step_handler(message, get_name)
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg')

@bot.message_handler(content_types= ['text'])
def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, get_surname)

@bot.message_handler(content_types= ['text'])
def get_surname(message):
    global surname
    surname = message.text
    bot.send_message('Сколько тебе лет?')
    bot.register_next_step_handler(message, get_age)

@bot.message_handler(content_types= ['text'])
def get_age(message):
    global age
    while age == 0:  # проверяем что возраст изменился
        try:
            age = int(message.text)  # проверяем, что возраст введен корректно
        except Exception:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
    bot.send_message(message.from_user.id, 'Тебе ' + str(age) + ' лет, тебя зовут ' + name + ' ' + surname + '?')


bot.polling()
