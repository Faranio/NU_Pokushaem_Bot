import telebot
import os
import re
from datetime import datetime
from telebot import types

bot = telebot.TeleBot('878935881:AAFtZVhTsrXC4-8vtr5QqTZ6ik8hH8fBxRw')

@bot.message_handler(regexp="Что поесть?"):
def handle_email(message):
    user = message.from_user.id
    # log server
    # print('Start')
    # print('User: ' + str(user))
    bot.send_message(user_id, "You chosen Chto")

@bot.message_handler(regexp="Где поесть?"):
def handle_email(message):
    user = message.from_user.id
    # log server
    # print('Start')
    # print('User: ' + str(user))
    bot.send_message(user_id, "You chosen gde")

@bot.message_handler(regexp="Рейтинг"):
def handle_email(message):
    user = message.from_user.id
    # log server
    # print('Start')
    # print('User: ' + str(user))
    bot.send_message(user_id, "You chosen rating")

def keyboard_first(user_id):
    markup = types.ReplyKeyboardMarkup()
    item_chto = types.KeyboardButton('Что поесть?')
    item_gde = types.KeyboardButton('Где поесть?')
    item_rate = types.KeyboardButton('Рейтинг')
    markup.row(item_chto)
    markup.row(item_gde)
    markup.row(item_rate)
    bot.send_message(user_id, "Выберите способ поиска", reply_markup=markup)

# response to \start
@bot.message_handler(commands=['start'])
def react_start(message):
    user = message.from_user.id
    # log server
    # print('Start')
    # print('User: ' + str(user))

    bot.send_message(user, "Пожалуйста, введите email для регистрации.")

# response to email address
@bot.message_handler(regexp="@")
def handle_email(message):
    user = message.from_user.id
    text = message.text

     # log server
    # print('Text request.')
    # print('User: ' + str(user))
    # print('Text: ' + text)

    #check domain
    if (re.search("@nu.edu.kz", text)):
        # TO-DO handle email
        bot.send_message(user, "Вы успешно зарегистрированы.")
        # go-to options keyboard
        keyboard_first(user)       
    elif (re.search("@", text)):
        bot.send_message(user, "Пожалуйста, введите email с @nu.edu.kz.")

@bot.message_handler(content_types=['voice'])
def get_audio_messages(message):
    user = message.from_user.id
    audio = message.voice

    # log server
    # print('Voice request.')
    # print('User: ' + str(user))

    # print user
    bot.send_message(user, "Can not process audio")

bot.polling(none_stop=True, interval=0)

