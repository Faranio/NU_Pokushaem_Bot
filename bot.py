from telebot import types
from firebase import firebase
from operator import itemgetter

import telebot
import re

firebase = firebase.FirebaseApplication("https://nupokushaembot.firebaseio.com/", None)

bot = telebot.TeleBot('878935881:AAFtZVhTsrXC4-8vtr5QqTZ6ik8hH8fBxRw')


@bot.message_handler(regexp="Happy Fox Coffee")
def rate(user_id):
    places = firebase.get('/nupokushaembot/FoodPlace', '')
    place = []
    
    for i in places:
        if places[i]['Name'] == 'Happy Fox Coffee':
            place = places[i]
        break
    
    if len(place) == 8:
        bot.send_message(user_id, "Название: {}\n"
                                  "Расположение в НУ: {}\n"
                                  "Количество отзывов: {}\n"
                                  "Рейтинг: {}\n"
                                  "Тип: {}\n"
                                  "Рабочее время: {}\n"
                                  "Номер телефона: {}".format(places[i]['Name'],
                                                              places[i]['Location'],
                                                              places[i]['Number of reviews'],
                                                              places[i]['Rating'],
                                                              places[i]['Type'],
                                                              places[i]['Working time'],
                                                              places[i]['Manager phone number']))
    else:
        bot.send_message(user_id, "Название: {}\n"
                                  "Расположение в НУ: {}\n"
                                  "Количество отзывов: {}\n"
                                  "Рейтинг: {}\n"
                                  "Тип: {}\n"
                                  "Рабочее время: {}".format(places[i]['Name'],
                                                             places[i]['Location'],
                                                             places[i]['Number of reviews'],
                                                             places[i]['Rating'],
                                                             places[i]['Type'],
                                                             places[i]['Working time']))
    markup = types.ReplyKeyboardMarkup()
    item_1 = types.KeyboardButton('Оценить на 5')
    item_2 = types.KeyboardButton('Оценить на 4')
    item_3 = types.KeyboardButton('Оценить на 3')
    item_4 = types.KeyboardButton('Оценить на 2')
    item_5 = types.KeyboardButton('Оценить на 1')
    markup.row(item_1)
    markup.row(item_2)
    markup.row(item_3)
    markup.row(item_4)
    markup.row(item_5)
    

def write_review(user_id):
    bot.send_message(user_id, "Пожалуйста, оцените один из перечисленных ресторанов.")
    places = firebase.get('/nupokushaembot/FoodPlace', '')
    markup = types.ReplyKeyboardMarkup()
    item_1 = types.KeyboardButton(str(places[0]['Name']))
    item_2 = types.KeyboardButton(str(places[1]['Name']))
    item_3 = types.KeyboardButton(str(places[2]['Name']))
    item_4 = types.KeyboardButton(str(places[3]['Name']))
    item_5 = types.KeyboardButton(str(places[4]['Name']))
    item_6 = types.KeyboardButton(str(places[5]['Name']))
    item_7 = types.KeyboardButton(str(places[6]['Name']))
    item_8 = types.KeyboardButton(str(places[7]['Name']))
    item_9 = types.KeyboardButton(str(places[8]['Name']))
    item_10 = types.KeyboardButton(str(places[9]['Name']))
    markup.row(item_1)
    markup.row(item_2)
    markup.row(item_3)
    markup.row(item_4)
    markup.row(item_5)
    markup.row(item_6)
    markup.row(item_7)
    markup.row(item_8)
    markup.row(item_9)
    markup.row(item_10)
    

@bot.message_handler(regexp="Кофейня")
def show_info(message):
    user = message.from_user.id
    places = firebase.get('/nupokushaembot/FoodPlace', '')
    result = []
    
    for i in places:
        if 'Coffee shop' in places[i]['Type']:
            result.append(i)
    
    bot.send_message(user, "Кофейни:")
    
    for i in result:
        if len(places[i]) == 8:
            bot.send_message(user, "Название: {}\n"
                                   "Расположение в НУ: {}\n"
                                   "Количество отзывов: {}\n"
                                   "Рейтинг: {}\n"
                                   "Тип: {}\n"
                                   "Рабочее время: {}\n"
                                   "Номер телефона: {}".format(places[i]['Name'],
                                                               places[i]['Location'],
                                                               places[i]['Number of reviews'],
                                                               places[i]['Rating'],
                                                               places[i]['Type'],
                                                               places[i]['Working time'],
                                                               places[i]['Manager phone number']))
        else:
            bot.send_message(user, "Название: {}\n"
                                   "Расположение в НУ: {}\n"
                                   "Количество отзывов: {}\n"
                                   "Рейтинг: {}\n"
                                   "Тип: {}\n"
                                   "Рабочее время: {}".format(places[i]['Name'],
                                                              places[i]['Location'],
                                                              places[i]['Number of reviews'],
                                                              places[i]['Rating'],
                                                              places[i]['Type'],
                                                              places[i]['Working time']))
    write_review(user)


@bot.message_handler(regexp="Столовая")
def show_info(message):
    user = message.from_user.id
    places = firebase.get('/nupokushaembot/FoodPlace', '')
    result = []
    
    for i in places:
        if 'Canteen' in places[i]['Type']:
            result.append(i)
    
    bot.send_message(user, "Столовые:")
    
    for i in result:
        if len(places[i]) == 8:
            bot.send_message(user, "Название: {}\n"
                                   "Расположение в НУ: {}\n"
                                   "Количество отзывов: {}\n"
                                   "Рейтинг: {}\n"
                                   "Тип: {}\n"
                                   "Рабочее время: {}\n"
                                   "Номер телефона: {}".format(places[i]['Name'],
                                                               places[i]['Location'],
                                                               places[i]['Number of reviews'],
                                                               places[i]['Rating'],
                                                               places[i]['Type'],
                                                               places[i]['Working time'],
                                                               places[i]['Manager phone number']))
        else:
            bot.send_message(user, "Название: {}\n"
                                   "Расположение в НУ: {}\n"
                                   "Количество отзывов: {}\n"
                                   "Рейтинг: {}\n"
                                   "Тип: {}\n"
                                   "Рабочее время: {}".format(places[i]['Name'],
                                                              places[i]['Location'],
                                                              places[i]['Number of reviews'],
                                                              places[i]['Rating'],
                                                              places[i]['Type'],
                                                              places[i]['Working time']))
    write_review(user)


@bot.message_handler(regexp="Ресторан")
def show_info(message):
    user = message.from_user.id
    places = firebase.get('/nupokushaembot/FoodPlace', '')
    result = []
    
    for i in places:
        if 'Restaurant' in places[i]['Type']:
            result.append(i)
    
    bot.send_message(user, "Рестораны:")
    
    for i in result:
        print(len(places[i]))
        if len(places[i]) == 8:
            bot.send_message(user, "Название: {}\n"
                                   "Расположение в НУ: {}\n"
                                   "Количество отзывов: {}\n"
                                   "Рейтинг: {}\n"
                                   "Тип: {}\n"
                                   "Рабочее время: {}\n"
                                   "Номер телефона: {}".format(places[i]['Name'],
                                                               places[i]['Location'],
                                                               places[i]['Number of reviews'],
                                                               places[i]['Rating'],
                                                               places[i]['Type'],
                                                               places[i]['Working time'],
                                                               places[i]['Manager phone number']))
        else:
            bot.send_message(user, "Название: {}\n"
                                   "Расположение в НУ: {}\n"
                                   "Количество отзывов: {}\n"
                                   "Рейтинг: {}\n"
                                   "Тип: {}\n"
                                   "Рабочее время: {}".format(places[i]['Name'],
                                                              places[i]['Location'],
                                                              places[i]['Number of reviews'],
                                                              places[i]['Rating'],
                                                              places[i]['Type'],
                                                              places[i]['Working time']))
    write_review(user)


@bot.message_handler(regexp="Кафе")
def show_info(message):
    user = message.from_user.id
    places = firebase.get('/nupokushaembot/FoodPlace', '')
    result = []
    
    for i in places:
        if 'Cafe' in places[i]['Type']:
            result.append(i)
    
    bot.send_message(user, "Кафе:")
    
    for i in result:
        if len(places[i]) == 8:
            bot.send_message(user, "Название: {}\n"
                                   "Расположение в НУ: {}\n"
                                   "Количество отзывов: {}\n"
                                   "Рейтинг: {}\n"
                                   "Тип: {}\n"
                                   "Рабочее время: {}\n"
                                   "Номер телефона: {}".format(places[i]['Name'],
                                                               places[i]['Location'],
                                                               places[i]['Number of reviews'],
                                                               places[i]['Rating'],
                                                               places[i]['Type'],
                                                               places[i]['Working time'],
                                                               places[i]['Manager phone number']))
        else:
            bot.send_message(user, "Название: {}\n"
                                   "Расположение в НУ: {}\n"
                                   "Количество отзывов: {}\n"
                                   "Рейтинг: {}\n"
                                   "Тип: {}\n"
                                   "Рабочее время: {}".format(places[i]['Name'],
                                                              places[i]['Location'],
                                                              places[i]['Number of reviews'],
                                                              places[i]['Rating'],
                                                              places[i]['Type'],
                                                              places[i]['Working time']))
    write_review(user)


@bot.message_handler(regexp="Кофе")
def show_info(message):
    user = message.from_user.id
    places = firebase.get('/nupokushaembot/FoodPlace', '')
    result = []

    for i in places:
        if 'Coffee' in places[i]['Food']:
            result.append(i)
            
    bot.send_message(user, "Кофе имеется в следующих местах:")
    
    for i in result:
        if len(places[i]) == 8:
            bot.send_message(user, "Название: {}\n"
                                   "Расположение в НУ: {}\n"
                                   "Количество отзывов: {}\n"
                                   "Рейтинг: {}\n"
                                   "Тип: {}\n"
                                   "Рабочее время: {}\n"
                                   "Номер телефона: {}".format(places[i]['Name'],
                                                              places[i]['Location'],
                                                              places[i]['Number of reviews'],
                                                              places[i]['Rating'],
                                                              places[i]['Type'],
                                                              places[i]['Working time'],
                                                              places[i]['Manager phone number']))
        else:
            bot.send_message(user, "Название: {}\n"
                                   "Расположение в НУ: {}\n"
                                   "Количество отзывов: {}\n"
                                   "Рейтинг: {}\n"
                                   "Тип: {}\n"
                                   "Рабочее время: {}".format(places[i]['Name'],
                                                              places[i]['Location'],
                                                              places[i]['Number of reviews'],
                                                              places[i]['Rating'],
                                                              places[i]['Type'],
                                                              places[i]['Working time']))
    write_review(user)


@bot.message_handler(regexp="Фаст-фуд")
def show_info(message):
    user = message.from_user.id
    places = firebase.get('/nupokushaembot/FoodPlace', '')
    result = []
    
    for i in places:
        if 'Fast Food' in places[i]['Food']:
            result.append(i)
    
    bot.send_message(user, "Фаст-фуд имеется в следующих местах:")
    
    for i in result:
        if len(places[i]) == 8:
            bot.send_message(user, "Название: {}\n"
                                   "Расположение в НУ: {}\n"
                                   "Количество отзывов: {}\n"
                                   "Рейтинг: {}\n"
                                   "Тип: {}\n"
                                   "Рабочее время: {}\n"
                                   "Номер телефона: {}".format(places[i]['Name'],
                                                               places[i]['Location'],
                                                               places[i]['Number of reviews'],
                                                               places[i]['Rating'],
                                                               places[i]['Type'],
                                                               places[i]['Working time'],
                                                               places[i]['Manager phone number']))
        else:
            bot.send_message(user, "Название: {}\n"
                                   "Расположение в НУ: {}\n"
                                   "Количество отзывов: {}\n"
                                   "Рейтинг: {}\n"
                                   "Тип: {}\n"
                                   "Рабочее время: {}".format(places[i]['Name'],
                                                              places[i]['Location'],
                                                              places[i]['Number of reviews'],
                                                              places[i]['Rating'],
                                                              places[i]['Type'],
                                                              places[i]['Working time']))
    write_review(user)


@bot.message_handler(regexp="Завтрак")
def show_info(message):
    user = message.from_user.id
    places = firebase.get('/nupokushaembot/FoodPlace', '')
    result = []
    
    for i in places:
        if 'Breakfast' in places[i]['Food']:
            result.append(i)
    
    bot.send_message(user, "Завтрак имеется в следующих местах:")
    
    for i in result:
        if len(places[i]) == 8:
            bot.send_message(user, "Название: {}\n"
                                   "Расположение в НУ: {}\n"
                                   "Количество отзывов: {}\n"
                                   "Рейтинг: {}\n"
                                   "Тип: {}\n"
                                   "Рабочее время: {}\n"
                                   "Номер телефона: {}".format(places[i]['Name'],
                                                               places[i]['Location'],
                                                               places[i]['Number of reviews'],
                                                               places[i]['Rating'],
                                                               places[i]['Type'],
                                                               places[i]['Working time'],
                                                               places[i]['Manager phone number']))
        else:
            bot.send_message(user, "Название: {}\n"
                                   "Расположение в НУ: {}\n"
                                   "Количество отзывов: {}\n"
                                   "Рейтинг: {}\n"
                                   "Тип: {}\n"
                                   "Рабочее время: {}".format(places[i]['Name'],
                                                              places[i]['Location'],
                                                              places[i]['Number of reviews'],
                                                              places[i]['Rating'],
                                                              places[i]['Type'],
                                                              places[i]['Working time']))
    write_review(user)


@bot.message_handler(regexp="Обед (Ужин)")
def show_info(message):
    user = message.from_user.id
    places = firebase.get('/nupokushaembot/FoodPlace', '')
    result = []
    
    for i in places:
        if 'Lunch' in places[i]['Food']:
            result.append(i)
    
    bot.send_message(user, "Обед и ужин имеется в следующих местах:")
    
    for i in result:
        if len(places[i]) == 8:
            bot.send_message(user, "Название: {}\n"
                                   "Расположение в НУ: {}\n"
                                   "Количество отзывов: {}\n"
                                   "Рейтинг: {}\n"
                                   "Тип: {}\n"
                                   "Рабочее время: {}\n"
                                   "Номер телефона: {}".format(places[i]['Name'],
                                                               places[i]['Location'],
                                                               places[i]['Number of reviews'],
                                                               places[i]['Rating'],
                                                               places[i]['Type'],
                                                               places[i]['Working time'],
                                                               places[i]['Manager phone number']))
        else:
            bot.send_message(user, "Название: {}\n"
                                   "Расположение в НУ: {}\n"
                                   "Количество отзывов: {}\n"
                                   "Рейтинг: {}\n"
                                   "Тип: {}\n"
                                   "Рабочее время: {}".format(places[i]['Name'],
                                                              places[i]['Location'],
                                                              places[i]['Number of reviews'],
                                                              places[i]['Rating'],
                                                              places[i]['Type'],
                                                              places[i]['Working time']))
    write_review(user)


@bot.message_handler(regexp="Дессерт")
def show_info(message):
    user = message.from_user.id
    places = firebase.get('/nupokushaembot/FoodPlace', '')
    result = []
    
    for i in places:
        if 'Dessert' in places[i]['Food']:
            result.append(i)
    
    bot.send_message(user, "Дессерт имеется в следующих местах:")
    
    for i in result:
        if len(places[i]) == 8:
            bot.send_message(user, "Название: {}\n"
                                   "Расположение в НУ: {}\n"
                                   "Количество отзывов: {}\n"
                                   "Рейтинг: {}\n"
                                   "Тип: {}\n"
                                   "Рабочее время: {}\n"
                                   "Номер телефона: {}".format(places[i]['Name'],
                                                               places[i]['Location'],
                                                               places[i]['Number of reviews'],
                                                               places[i]['Rating'],
                                                               places[i]['Type'],
                                                               places[i]['Working time'],
                                                               places[i]['Manager phone number']))
        else:
            bot.send_message(user, "Название: {}\n"
                                   "Расположение в НУ: {}\n"
                                   "Количество отзывов: {}\n"
                                   "Рейтинг: {}\n"
                                   "Тип: {}\n"
                                   "Рабочее время: {}".format(places[i]['Name'],
                                                              places[i]['Location'],
                                                              places[i]['Number of reviews'],
                                                              places[i]['Rating'],
                                                              places[i]['Type'],
                                                              places[i]['Working time']))
    write_review(user)


@bot.message_handler(regexp="Суши")
def show_info(message):
    user = message.from_user.id
    places = firebase.get('/nupokushaembot/FoodPlace', '')
    result = []
    
    for i in places:
        if 'Sushi' in places[i]['Food']:
            result.append(i)
    
    bot.send_message(user, "Суши имеются в следующих местах:")
    
    for i in result:
        if len(places[i]) == 8:
            bot.send_message(user, "Название: {}\n"
                                   "Расположение в НУ: {}\n"
                                   "Количество отзывов: {}\n"
                                   "Рейтинг: {}\n"
                                   "Тип: {}\n"
                                   "Рабочее время: {}\n"
                                   "Номер телефона: {}".format(places[i]['Name'],
                                                               places[i]['Location'],
                                                               places[i]['Number of reviews'],
                                                               places[i]['Rating'],
                                                               places[i]['Type'],
                                                               places[i]['Working time'],
                                                               places[i]['Manager phone number']))
        else:
            bot.send_message(user, "Название: {}\n"
                                   "Расположение в НУ: {}\n"
                                   "Количество отзывов: {}\n"
                                   "Рейтинг: {}\n"
                                   "Тип: {}\n"
                                   "Рабочее время: {}".format(places[i]['Name'],
                                                              places[i]['Location'],
                                                              places[i]['Number of reviews'],
                                                              places[i]['Rating'],
                                                              places[i]['Type'],
                                                              places[i]['Working time']))
    write_review(user)


def food_tags(user_id):
    markup = types.ReplyKeyboardMarkup()
    item_1 = types.KeyboardButton('Кофе')
    item_2 = types.KeyboardButton('Фаст-фуд')
    item_3 = types.KeyboardButton('Завтрак')
    item_4 = types.KeyboardButton('Обед (Ужин)')
    item_5 = types.KeyboardButton('Суши')
    item_6 = types.KeyboardButton('Дессерт')
    markup.row(item_1, item_2, item_3)
    markup.row(item_4, item_5, item_6)
    bot.send_message(user_id, "Выберите желаемую еду", reply_markup=markup)
    
    
def type_tags(user_id):
    markup = types.ReplyKeyboardMarkup()
    item_1 = types.KeyboardButton('Кофейня')
    item_2 = types.KeyboardButton('Столовая')
    item_3 = types.KeyboardButton('Ресторан')
    item_4 = types.KeyboardButton('Кафе')
    markup.row(item_1)
    markup.row(item_2)
    markup.row(item_3)
    markup.row(item_4)
    bot.send_message(user_id, "Выберите желаемое место", reply_markup=markup)


def ratings(user_id):
    places = firebase.get('/nupokushaembot/FoodPlace', '')
    ratings = []
    
    for i in places:
        ratings.append([i, places[i]['Rating']])
    
    ratings = sorted(ratings, key=itemgetter(1))
    ratings.reverse()
    
    for i in ratings:
        if len(places[i]) == 8:
            bot.send_message(user_id, "Название: {}\n"
                                   "Расположение в НУ: {}\n"
                                   "Количество отзывов: {}\n"
                                   "Рейтинг: {}\n"
                                   "Тип: {}\n"
                                   "Рабочее время: {}\n"
                                   "Номер телефона: {}".format(places[i]['Name'],
                                                               places[i]['Location'],
                                                               places[i]['Number of reviews'],
                                                               places[i]['Rating'],
                                                               places[i]['Type'],
                                                               places[i]['Working time'],
                                                               places[i]['Manager phone number']))
        else:
            bot.send_message(user_id, "Название: {}\n"
                                   "Расположение в НУ: {}\n"
                                   "Количество отзывов: {}\n"
                                   "Рейтинг: {}\n"
                                   "Тип: {}\n"
                                   "Рабочее время: {}".format(places[i]['Name'],
                                                              places[i]['Location'],
                                                              places[i]['Number of reviews'],
                                                              places[i]['Rating'],
                                                              places[i]['Type'],
                                                              places[i]['Working time']))
    write_review(user_id)


@bot.message_handler(regexp="Что поесть?")
def handle_email(message):
    user = message.from_user.id
    food_tags(user)


@bot.message_handler(regexp="Где поесть?")
def handle_email(message):
    user = message.from_user.id
    type_tags(user)


@bot.message_handler(regexp="Рейтинг")
def handle_email(message):
    user = message.from_user.id
    ratings(user)


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
    bot.send_message(user, "Пожалуйста, введите email для регистрации.")


# Response to email address
@bot.message_handler(regexp="@")
def handle_email(message):
    user = message.from_user.id
    text = message.text
    
    # check domain
    if re.search("@nu.edu.kz", text):
        # TO-DO handle email
        bot.send_message(user, "Вы успешно зарегистрированы.")
        # go-to options keyboard
        keyboard_first(user)
    elif re.search("@", text):
        bot.send_message(user, "Пожалуйста, введите email с @nu.edu.kz.")


@bot.message_handler(content_types=['voice'])
def get_audio_messages(message):
    user = message.from_user.id
    bot.send_message(user, "Can not process audio")


bot.polling(none_stop=True, interval=0)
