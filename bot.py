from telebot import types
from firebase import firebase
from operator import itemgetter

import telebot
import re
import ssl
import smtplib
import numpy

firebase = firebase.FirebaseApplication("https://nupokushaembot.firebaseio.com/", None)

bot = telebot.TeleBot('878935881:AAFtZVhTsrXC4-8vtr5QqTZ6ik8hH8fBxRw')


def send_photo(user_id, title):
    if title == 'Happy Fox Coffee':
        bot.send_photo(user_id, 'https://astana.restolife.kz/upload/information_system_30/1/2/9/item_12936/information_items_property_13381.jpg')
    elif title == 'Kunde Social Cafe':
        bot.send_photo(user_id, 'https://scontent.ftse3-1.fna.fbcdn.net/v/t1.0-9/20604346_263667847464798_3795394876519801540_n.png?_nc_cat=105&_nc_ohc=qsMErKoT3xcAQm7So2rn8mmBOD-XjaNJ2WXWBTmnYkLgxjwz9ohVHaRNQ&_nc_ht=scontent.ftse3-1.fna&oh=262951a42f7a94922a45e671718d5fac&oe=5E7A2D97')
    elif title == 'Midpoint Cafe & Catering':
        bot.send_photo(user_id, 'https://scontent.ftse3-1.fna.fbcdn.net/v/t1.0-9/27752611_1677359642343423_1360998110630683309_n.jpg?_nc_cat=103&_nc_ohc=Xf1lFrsTI0IAQk6W8xYtsnKsKBaYZoqdETszKr2vBpoaqWvjwlw7r3rgw&_nc_ht=scontent.ftse3-1.fna&oh=6fb7032972f91bc2cd023ab29cd2fb04&oe=5E832A2C')
    elif title == 'La Tartine':
        bot.send_photo(user_id, 'https://www.latartine.kz/assets/images/promo.jpg')
    elif title == 'Health Project':
        bot.send_photo(user_id, 'https://slide-share.ru/image/2074452.jpeg')
    elif title == '6\'\'Inch':
        bot.send_photo(user_id, 'https://scontent.ftse3-1.fna.fbcdn.net/v/t1.0-9/60761262_331752720830616_9031096920927371264_n.png?_nc_cat=110&_nc_ohc=5GB2eGVtVDkAQkL6H6EXWCYWONGlsORwbYiv4dZmiXAT-1HlA9OUWg9Pw&_nc_ht=scontent.ftse3-1.fna&oh=32b27ee7cbcefd6c22648faa5255c632&oe=5E746DF6')
    elif title == 'Бодрый День':
        bot.send_photo(user_id, 'https://weproject.media/upload/medialibrary/b42/b4275c1d3f27f3552ea73d406893c14d.jpg')
    # elif title == 'Health Project Cafe':
    # elif title == 'Free Flow':
    elif title == 'Marketplace':
        bot.send_photo(user_id, 'http://nazarbayev-marketplace.ru/static/img/logo.0e6a8f0f2ac1.png')
    elif title == 'Daily Cup':
        bot.send_photo(user_id, 'https://scontent.ftse3-1.fna.fbcdn.net/v/t1.0-9/27654731_1649170721840804_7861585871180708359_n.jpg?_nc_cat=106&_nc_ohc=M24g97CazD0AQne-3-uoom4G-uBF47o2iiAWVDRqQa352ej-7dvzU_z0g&_nc_ht=scontent.ftse3-1.fna&oh=95ab1eaad78c870a15107294e6df3bf0&oe=5E8798B4')


@bot.callback_query_handler(func=lambda c: True)
def inline(c):
    places = firebase.get('/nupokushaembot/FoodPlace', '')
    
    if c.data == 'Happy Fox Coffee, Rating 1':
        
        for i in places:
            if places[i]['Name'] == 'Happy Fox Coffee':
                rating = places[i]['Rating']
                num_reviews = places[i]['Number of reviews']
                break
        
        rating = round(((rating * num_reviews) + 1) / (num_reviews + 1), 2)
        
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Rating', rating)
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Number of reviews', num_reviews + 1)

    elif c.data == 'Happy Fox Coffee, Rating 2':
    
        for i in places:
            if places[i]['Name'] == 'Happy Fox Coffee':
                rating = places[i]['Rating']
                num_reviews = places[i]['Number of reviews']
                break
    
        rating = round(((rating * num_reviews) + 2) / (num_reviews + 1), 2)
    
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Rating', rating)
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Number of reviews', num_reviews + 1)

    elif c.data == 'Happy Fox Coffee, Rating 3':
    
        for i in places:
            if places[i]['Name'] == 'Happy Fox Coffee':
                rating = places[i]['Rating']
                num_reviews = places[i]['Number of reviews']
                break
    
        rating = round(((rating * num_reviews) + 3) / (num_reviews + 1), 2)
    
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Rating', rating)
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Number of reviews', num_reviews + 1)

    elif c.data == 'Happy Fox Coffee, Rating 4':
    
        for i in places:
            if places[i]['Name'] == 'Happy Fox Coffee':
                rating = places[i]['Rating']
                num_reviews = places[i]['Number of reviews']
                break
    
        rating = round(((rating * num_reviews) + 4) / (num_reviews + 1), 2)
    
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Rating', rating)
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Number of reviews', num_reviews + 1)

    elif c.data == 'Happy Fox Coffee, Rating 5':
    
        for i in places:
            if places[i]['Name'] == 'Happy Fox Coffee':
                rating = places[i]['Rating']
                num_reviews = places[i]['Number of reviews']
                break
    
        rating = round(((rating * num_reviews) + 5) / (num_reviews + 1), 2)
    
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Rating', rating)
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Number of reviews', num_reviews + 1)

    elif c.data == 'Kunde Social Cafe, Rating 1':
    
        for i in places:
            if places[i]['Name'] == 'Kunde Social Cafe':
                rating = places[i]['Rating']
                num_reviews = places[i]['Number of reviews']
                break
    
        rating = round(((rating * num_reviews) + 1) / (num_reviews + 1), 2)
    
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Rating', rating)
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Number of reviews', num_reviews + 1)

    elif c.data == 'Kunde Social Cafe, Rating 2':
    
        for i in places:
            if places[i]['Name'] == 'Kunde Social Cafe':
                rating = places[i]['Rating']
                num_reviews = places[i]['Number of reviews']
                break
    
        rating = round(((rating * num_reviews) + 2) / (num_reviews + 1), 2)
    
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Rating', rating)
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Number of reviews', num_reviews + 1)

    elif c.data == 'Kunde Social Cafe, Rating 3':
    
        for i in places:
            if places[i]['Name'] == 'Kunde Social Cafe':
                rating = places[i]['Rating']
                num_reviews = places[i]['Number of reviews']
                break
    
        rating = round(((rating * num_reviews) + 3) / (num_reviews + 1), 2)
    
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Rating', rating)
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Number of reviews', num_reviews + 1)

    elif c.data == 'Kunde Social Cafe, Rating 4':
    
        for i in places:
            if places[i]['Name'] == 'Kunde Social Cafe':
                rating = places[i]['Rating']
                num_reviews = places[i]['Number of reviews']
                break
    
        rating = round(((rating * num_reviews) + 4) / (num_reviews + 1), 2)
    
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Rating', rating)
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Number of reviews', num_reviews + 1)

    elif c.data == 'Kunde Social Cafe, Rating 5':
    
        for i in places:
            if places[i]['Name'] == 'Kunde Social Cafe':
                rating = places[i]['Rating']
                num_reviews = places[i]['Number of reviews']
                break
    
        rating = round(((rating * num_reviews) + 5) / (num_reviews + 1), 2)
    
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Rating', rating)
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Number of reviews', num_reviews + 1)

    elif c.data == 'Midpoint Cafe & Catering, Rating 1':
    
        for i in places:
            if places[i]['Name'] == 'Midpoint Cafe & Catering':
                rating = places[i]['Rating']
                num_reviews = places[i]['Number of reviews']
                break
    
        rating = round(((rating * num_reviews) + 1) / (num_reviews + 1), 2)
    
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Rating', rating)
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Number of reviews', num_reviews + 1)

    elif c.data == 'Midpoint Cafe & Catering, Rating 2':
    
        for i in places:
            if places[i]['Name'] == 'Midpoint Cafe & Catering':
                rating = places[i]['Rating']
                num_reviews = places[i]['Number of reviews']
                break
    
        rating = round(((rating * num_reviews) + 2) / (num_reviews + 1), 2)
    
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Rating', rating)
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Number of reviews', num_reviews + 1)

    elif c.data == 'Midpoint Cafe & Catering, Rating 3':
    
        for i in places:
            if places[i]['Name'] == 'Midpoint Cafe & Catering':
                rating = places[i]['Rating']
                num_reviews = places[i]['Number of reviews']
                break
    
        rating = round(((rating * num_reviews) + 3) / (num_reviews + 1), 2)
    
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Rating', rating)
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Number of reviews', num_reviews + 1)

    elif c.data == 'Midpoint Cafe & Catering, Rating 4':
    
        for i in places:
            if places[i]['Name'] == 'Midpoint Cafe & Catering':
                rating = places[i]['Rating']
                num_reviews = places[i]['Number of reviews']
                break
    
        rating = round(((rating * num_reviews) + 4) / (num_reviews + 1), 2)
    
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Rating', rating)
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Number of reviews', num_reviews + 1)

    elif c.data == 'Midpoint Cafe & Catering, Rating 5':
    
        for i in places:
            if places[i]['Name'] == 'Midpoint Cafe & Catering':
                rating = places[i]['Rating']
                num_reviews = places[i]['Number of reviews']
                break
    
        rating = round(((rating * num_reviews) + 5) / (num_reviews + 1), 2)
    
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Rating', rating)
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Number of reviews', num_reviews + 1)

    elif c.data == 'La Tartine, Rating 1':
    
        for i in places:
            if places[i]['Name'] == 'La Tartine':
                rating = places[i]['Rating']
                num_reviews = places[i]['Number of reviews']
                break
    
        rating = round(((rating * num_reviews) + 1) / (num_reviews + 1), 2)
    
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Rating', rating)
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Number of reviews', num_reviews + 1)

    elif c.data == 'La Tartine, Rating 2':
    
        for i in places:
            if places[i]['Name'] == 'La Tartine':
                rating = places[i]['Rating']
                num_reviews = places[i]['Number of reviews']
                break
    
        rating = round(((rating * num_reviews) + 2) / (num_reviews + 1), 2)
    
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Rating', rating)
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Number of reviews', num_reviews + 1)

    elif c.data == 'La Tartine, Rating 3':
    
        for i in places:
            if places[i]['Name'] == 'La Tartine':
                rating = places[i]['Rating']
                num_reviews = places[i]['Number of reviews']
                break
    
        rating = round(((rating * num_reviews) + 3) / (num_reviews + 1), 2)
    
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Rating', rating)
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Number of reviews', num_reviews + 1)

    elif c.data == 'La Tartine, Rating 4':
    
        for i in places:
            if places[i]['Name'] == 'La Tartine':
                rating = places[i]['Rating']
                num_reviews = places[i]['Number of reviews']
                break
    
        rating = round(((rating * num_reviews) + 4) / (num_reviews + 1), 2)
    
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Rating', rating)
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Number of reviews', num_reviews + 1)

    elif c.data == 'La Tartine, Rating 5':
    
        for i in places:
            if places[i]['Name'] == 'La Tartine':
                rating = places[i]['Rating']
                num_reviews = places[i]['Number of reviews']
                break
    
        rating = round(((rating * num_reviews) + 5) / (num_reviews + 1), 2)
    
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Rating', rating)
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Number of reviews', num_reviews + 1)

    elif c.data == 'Health Project, Rating 1':
    
        for i in places:
            if places[i]['Name'] == 'Health Project':
                rating = places[i]['Rating']
                num_reviews = places[i]['Number of reviews']
                break
    
        rating = round(((rating * num_reviews) + 1) / (num_reviews + 1), 2)
    
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Rating', rating)
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Number of reviews', num_reviews + 1)

    elif c.data == 'Health Project, Rating 2':
    
        for i in places:
            if places[i]['Name'] == 'Health Project':
                rating = places[i]['Rating']
                num_reviews = places[i]['Number of reviews']
                break
    
        rating = round(((rating * num_reviews) + 2) / (num_reviews + 1), 2)
    
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Rating', rating)
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Number of reviews', num_reviews + 1)

    elif c.data == 'Health Project, Rating 3':
    
        for i in places:
            if places[i]['Name'] == 'Health Project':
                rating = places[i]['Rating']
                num_reviews = places[i]['Number of reviews']
                break
    
        rating = round(((rating * num_reviews) + 3) / (num_reviews + 1), 2)
    
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Rating', rating)
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Number of reviews', num_reviews + 1)

    elif c.data == 'Health Project, Rating 4':
    
        for i in places:
            if places[i]['Name'] == 'Health Project':
                rating = places[i]['Rating']
                num_reviews = places[i]['Number of reviews']
                break
    
        rating = round(((rating * num_reviews) + 4) / (num_reviews + 1), 2)
    
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Rating', rating)
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Number of reviews', num_reviews + 1)

    elif c.data == 'Health Project, Rating 5':
    
        for i in places:
            if places[i]['Name'] == 'Health Project':
                rating = places[i]['Rating']
                num_reviews = places[i]['Number of reviews']
                break
    
        rating = round(((rating * num_reviews) + 5) / (num_reviews + 1), 2)
    
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Rating', rating)
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Number of reviews', num_reviews + 1)

    elif c.data == '6\'\'Inch, Rating 1':
    
        for i in places:
            if places[i]['Name'] == '6\'\'Inch':
                rating = places[i]['Rating']
                num_reviews = places[i]['Number of reviews']
                break
    
        rating = round(((rating * num_reviews) + 1) / (num_reviews + 1), 2)
    
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Rating', rating)
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Number of reviews', num_reviews + 1)

    elif c.data == '6\'\'Inch, Rating 2':
    
        for i in places:
            if places[i]['Name'] == '6\'\'Inch':
                rating = places[i]['Rating']
                num_reviews = places[i]['Number of reviews']
                break
    
        rating = round(((rating * num_reviews) + 2) / (num_reviews + 1), 2)
    
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Rating', rating)
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Number of reviews', num_reviews + 1)

    elif c.data == '6\'\'Inch, Rating 3':
    
        for i in places:
            if places[i]['Name'] == '6\'\'Inch':
                rating = places[i]['Rating']
                num_reviews = places[i]['Number of reviews']
                break
    
        rating = round(((rating * num_reviews) + 3) / (num_reviews + 1), 2)
    
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Rating', rating)
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Number of reviews', num_reviews + 1)

    elif c.data == '6\'\'Inch, Rating 4':
    
        for i in places:
            if places[i]['Name'] == '6\'\'Inch':
                rating = places[i]['Rating']
                num_reviews = places[i]['Number of reviews']
                break
    
        rating = round(((rating * num_reviews) + 4) / (num_reviews + 1), 2)
    
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Rating', rating)
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Number of reviews', num_reviews + 1)

    elif c.data == '6\'\'Inch, Rating 5':
    
        for i in places:
            if places[i]['Name'] == '6\'\'Inch':
                rating = places[i]['Rating']
                num_reviews = places[i]['Number of reviews']
                break
    
        rating = round(((rating * num_reviews) + 5) / (num_reviews + 1), 2)
    
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Rating', rating)
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Number of reviews', num_reviews + 1)

    elif c.data == 'Бодрый День, Rating 1':
    
        for i in places:
            if places[i]['Name'] == 'Бодрый День':
                rating = places[i]['Rating']
                num_reviews = places[i]['Number of reviews']
                break
    
        rating = round(((rating * num_reviews) + 1) / (num_reviews + 1), 2)
    
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Rating', rating)
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Number of reviews', num_reviews + 1)

    elif c.data == 'Бодрый День, Rating 2':
    
        for i in places:
            if places[i]['Name'] == 'Бодрый День':
                rating = places[i]['Rating']
                num_reviews = places[i]['Number of reviews']
                break
    
        rating = round(((rating * num_reviews) + 2) / (num_reviews + 1), 2)
    
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Rating', rating)
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Number of reviews', num_reviews + 1)

    elif c.data == 'Бодрый День, Rating 3':
    
        for i in places:
            if places[i]['Name'] == 'Бодрый День':
                rating = places[i]['Rating']
                num_reviews = places[i]['Number of reviews']
                break
    
        rating = round(((rating * num_reviews) + 3) / (num_reviews + 1), 2)
    
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Rating', rating)
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Number of reviews', num_reviews + 1)

    elif c.data == 'Бодрый День, Rating 4':
    
        for i in places:
            if places[i]['Name'] == 'Бодрый День':
                rating = places[i]['Rating']
                num_reviews = places[i]['Number of reviews']
                break
    
        rating = round(((rating * num_reviews) + 4) / (num_reviews + 1), 2)
    
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Rating', rating)
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Number of reviews', num_reviews + 1)

    elif c.data == 'Бодрый День, Rating 5':
    
        for i in places:
            if places[i]['Name'] == 'Бодрый День':
                rating = places[i]['Rating']
                num_reviews = places[i]['Number of reviews']
                break
    
        rating = round(((rating * num_reviews) + 5) / (num_reviews + 1), 2)
    
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Rating', rating)
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Number of reviews', num_reviews + 1)

    elif c.data == 'Health Project Cafe, Rating 1':
    
        for i in places:
            if places[i]['Name'] == 'Health Project Cafe':
                rating = places[i]['Rating']
                num_reviews = places[i]['Number of reviews']
                break
    
        rating = round(((rating * num_reviews) + 1) / (num_reviews + 1), 2)
    
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Rating', rating)
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Number of reviews', num_reviews + 1)

    elif c.data == 'Health Project Cafe, Rating 2':
    
        for i in places:
            if places[i]['Name'] == 'Health Project Cafe':
                rating = places[i]['Rating']
                num_reviews = places[i]['Number of reviews']
                break
    
        rating = round(((rating * num_reviews) + 2) / (num_reviews + 1), 2)
    
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Rating', rating)
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Number of reviews', num_reviews + 1)

    elif c.data == 'Health Project Cafe, Rating 3':
    
        for i in places:
            if places[i]['Name'] == 'Health Project Cafe':
                rating = places[i]['Rating']
                num_reviews = places[i]['Number of reviews']
                break
    
        rating = round(((rating * num_reviews) + 3) / (num_reviews + 1), 2)
    
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Rating', rating)
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Number of reviews', num_reviews + 1)

    elif c.data == 'Health Project Cafe, Rating 4':
    
        for i in places:
            if places[i]['Name'] == 'Health Project Cafe':
                rating = places[i]['Rating']
                num_reviews = places[i]['Number of reviews']
                break
    
        rating = round(((rating * num_reviews) + 4) / (num_reviews + 1), 2)
    
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Rating', rating)
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Number of reviews', num_reviews + 1)

    elif c.data == 'Health Project Cafe, Rating 5':
    
        for i in places:
            if places[i]['Name'] == 'Health Project Cafe':
                rating = places[i]['Rating']
                num_reviews = places[i]['Number of reviews']
                break
    
        rating = round(((rating * num_reviews) + 5) / (num_reviews + 1), 2)
    
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Rating', rating)
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Number of reviews', num_reviews + 1)

    elif c.data == 'Free Flow, Rating 1':
    
        for i in places:
            if places[i]['Name'] == 'Free Flow':
                rating = places[i]['Rating']
                num_reviews = places[i]['Number of reviews']
                break
    
        rating = round(((rating * num_reviews) + 1) / (num_reviews + 1), 2)
    
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Rating', rating)
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Number of reviews', num_reviews + 1)

    elif c.data == 'Free Flow, Rating 2':
    
        for i in places:
            if places[i]['Name'] == 'Free Flow':
                rating = places[i]['Rating']
                num_reviews = places[i]['Number of reviews']
                break
    
        rating = round(((rating * num_reviews) + 2) / (num_reviews + 1), 2)
    
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Rating', rating)
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Number of reviews', num_reviews + 1)

    elif c.data == 'Free Flow, Rating 3':
    
        for i in places:
            if places[i]['Name'] == 'Free Flow':
                rating = places[i]['Rating']
                num_reviews = places[i]['Number of reviews']
                break
    
        rating = round(((rating * num_reviews) + 3) / (num_reviews + 1), 2)
    
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Rating', rating)
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Number of reviews', num_reviews + 1)

    elif c.data == 'Free Flow, Rating 4':
    
        for i in places:
            if places[i]['Name'] == 'Free Flow':
                rating = places[i]['Rating']
                num_reviews = places[i]['Number of reviews']
                break
    
        rating = round(((rating * num_reviews) + 4) / (num_reviews + 1), 2)
    
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Rating', rating)
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Number of reviews', num_reviews + 1)

    elif c.data == 'Free Flow, Rating 5':
    
        for i in places:
            if places[i]['Name'] == 'Free Flow':
                rating = places[i]['Rating']
                num_reviews = places[i]['Number of reviews']
                break
    
        rating = round(((rating * num_reviews) + 5) / (num_reviews + 1), 2)
    
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Rating', rating)
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Number of reviews', num_reviews + 1)

    elif c.data == 'Marketplace, Rating 1':
    
        for i in places:
            if places[i]['Name'] == 'Marketplace':
                rating = places[i]['Rating']
                num_reviews = places[i]['Number of reviews']
                break
    
        rating = round(((rating * num_reviews) + 1) / (num_reviews + 1), 2)
    
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Rating', rating)
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Number of reviews', num_reviews + 1)

    elif c.data == 'Marketplace, Rating 2':
    
        for i in places:
            if places[i]['Name'] == 'Marketplace':
                rating = places[i]['Rating']
                num_reviews = places[i]['Number of reviews']
                break
    
        rating = round(((rating * num_reviews) + 2) / (num_reviews + 1), 2)
    
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Rating', rating)
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Number of reviews', num_reviews + 1)

    elif c.data == 'Marketplace, Rating 3':
    
        for i in places:
            if places[i]['Name'] == 'Marketplace':
                rating = places[i]['Rating']
                num_reviews = places[i]['Number of reviews']
                break
    
        rating = round(((rating * num_reviews) + 3) / (num_reviews + 1), 2)
    
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Rating', rating)
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Number of reviews', num_reviews + 1)

    elif c.data == 'Marketplace, Rating 4':
    
        for i in places:
            if places[i]['Name'] == 'Marketplace':
                rating = places[i]['Rating']
                num_reviews = places[i]['Number of reviews']
                break
    
        rating = round(((rating * num_reviews) + 4) / (num_reviews + 1), 2)
    
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Rating', rating)
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Number of reviews', num_reviews + 1)

    elif c.data == 'Marketplace, Rating 5':
    
        for i in places:
            if places[i]['Name'] == 'Marketplace':
                rating = places[i]['Rating']
                num_reviews = places[i]['Number of reviews']
                break
    
        rating = round(((rating * num_reviews) + 5) / (num_reviews + 1), 2)
    
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Rating', rating)
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Number of reviews', num_reviews + 1)

    elif c.data == 'Daily Cup, Rating 1':
    
        for i in places:
            if places[i]['Name'] == 'Daily Cup':
                rating = places[i]['Rating']
                num_reviews = places[i]['Number of reviews']
                break
    
        rating = round(((rating * num_reviews) + 1) / (num_reviews + 1), 2)
    
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Rating', rating)
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Number of reviews', num_reviews + 1)

    elif c.data == 'Daily Cup, Rating 2':
    
        for i in places:
            if places[i]['Name'] == 'Daily Cup':
                rating = places[i]['Rating']
                num_reviews = places[i]['Number of reviews']
                break
    
        rating = round(((rating * num_reviews) + 2) / (num_reviews + 1), 2)
    
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Rating', rating)
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Number of reviews', num_reviews + 1)

    elif c.data == 'Daily Cup, Rating 3':
    
        for i in places:
            if places[i]['Name'] == 'Daily Cup':
                rating = places[i]['Rating']
                num_reviews = places[i]['Number of reviews']
                break
    
        rating = round(((rating * num_reviews) + 3) / (num_reviews + 1), 2)
    
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Rating', rating)
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Number of reviews', num_reviews + 1)

    elif c.data == 'Daily Cup, Rating 4':
    
        for i in places:
            if places[i]['Name'] == 'Daily Cup':
                rating = places[i]['Rating']
                num_reviews = places[i]['Number of reviews']
                break
    
        rating = round(((rating * num_reviews) + 4) / (num_reviews + 1), 2)
    
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Rating', rating)
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Number of reviews', num_reviews + 1)

    elif c.data == 'Daily Cup, Rating 5':
    
        for i in places:
            if places[i]['Name'] == 'Daily Cup':
                rating = places[i]['Rating']
                num_reviews = places[i]['Number of reviews']
                break
    
        rating = round(((rating * num_reviews) + 5) / (num_reviews + 1), 2)
    
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Rating', rating)
        firebase.put('/nupokushaembot/FoodPlace/{}'.format(i), 'Number of reviews', num_reviews + 1)


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
    
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text='⭐️', callback_data=str(places[i]['Name']) + ", Rating {}".format('1'))
        but_2 = types.InlineKeyboardButton(text='⭐️⭐️', callback_data=str(places[i]['Name']) + ", Rating {}".format('2'))
        but_3 = types.InlineKeyboardButton(text='⭐️⭐️⭐️', callback_data=str(places[i]['Name']) + ", Rating {}".format('3'))
        but_4 = types.InlineKeyboardButton(text='⭐️⭐️⭐️⭐️', callback_data=str(places[i]['Name']) + ", Rating {}".format('4'))
        but_5 = types.InlineKeyboardButton(text='⭐️⭐️⭐️⭐️⭐️', callback_data=str(places[i]['Name']) + ", Rating {}".format('5'))
        key.add(but_1, but_2, but_3, but_4, but_5)
        
        send_photo(user, places[i]['Name'])
        
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
                                                               places[i]['Manager phone number']), reply_markup=key)
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
                                                              places[i]['Working time']), reply_markup=key)
    keyboard_first(user)


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
    
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text='⭐️', callback_data=str(places[i]['Name']) + ", Rating {}".format('1'))
        but_2 = types.InlineKeyboardButton(text='⭐⭐️️', callback_data=str(places[i]['Name']) + ", Rating {}".format('2'))
        but_3 = types.InlineKeyboardButton(text='⭐⭐⭐️️️', callback_data=str(places[i]['Name']) + ", Rating {}".format('3'))
        but_4 = types.InlineKeyboardButton(text='⭐⭐⭐⭐️️️️', callback_data=str(places[i]['Name']) + ", Rating {}".format('4'))
        but_5 = types.InlineKeyboardButton(text='⭐⭐⭐⭐️️️️⭐️', callback_data=str(places[i]['Name']) + ", Rating {}".format('5'))
        key.add(but_1, but_2, but_3, but_4, but_5)

        send_photo(user, places[i]['Name'])
        
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
                                                               places[i]['Manager phone number']), reply_markup=key)
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
                                                              places[i]['Working time']), reply_markup=key)
    keyboard_first(user)


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
    
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text='⭐️', callback_data=str(places[i]['Name']) + ", Rating {}".format('1'))
        but_2 = types.InlineKeyboardButton(text='⭐⭐️️', callback_data=str(places[i]['Name']) + ", Rating {}".format('2'))
        but_3 = types.InlineKeyboardButton(text='⭐⭐⭐️️️', callback_data=str(places[i]['Name']) + ", Rating {}".format('3'))
        but_4 = types.InlineKeyboardButton(text='⭐⭐⭐⭐️️️️', callback_data=str(places[i]['Name']) + ", Rating {}".format('4'))
        but_5 = types.InlineKeyboardButton(text='⭐⭐⭐⭐️️️️⭐️', callback_data=str(places[i]['Name']) + ", Rating {}".format('5'))
        key.add(but_1, but_2, but_3, but_4, but_5)

        send_photo(user, places[i]['Name'])
        
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
                                                               places[i]['Manager phone number']), reply_markup=key)
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
                                                              places[i]['Working time']), reply_markup=key)
    keyboard_first(user)


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
    
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text='⭐️', callback_data=str(places[i]['Name']) + ", Rating {}".format('1'))
        but_2 = types.InlineKeyboardButton(text='⭐⭐️️', callback_data=str(places[i]['Name']) + ", Rating {}".format('2'))
        but_3 = types.InlineKeyboardButton(text='⭐⭐⭐️️️', callback_data=str(places[i]['Name']) + ", Rating {}".format('3'))
        but_4 = types.InlineKeyboardButton(text='⭐⭐⭐⭐️️️️', callback_data=str(places[i]['Name']) + ", Rating {}".format('4'))
        but_5 = types.InlineKeyboardButton(text='⭐⭐⭐⭐️️️️⭐️', callback_data=str(places[i]['Name']) + ", Rating {}".format('5'))
        key.add(but_1, but_2, but_3, but_4, but_5)

        send_photo(user, places[i]['Name'])
        
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
                                                               places[i]['Manager phone number']), reply_markup=key)
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
                                                              places[i]['Working time']), reply_markup=key)
    keyboard_first(user)


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
        
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text='⭐️', callback_data=str(places[i]['Name']) + ", Rating {}".format('1'))
        but_2 = types.InlineKeyboardButton(text='⭐⭐️️', callback_data=str(places[i]['Name']) + ", Rating {}".format('2'))
        but_3 = types.InlineKeyboardButton(text='⭐⭐⭐️️️', callback_data=str(places[i]['Name']) + ", Rating {}".format('3'))
        but_4 = types.InlineKeyboardButton(text='⭐⭐⭐⭐️️️️', callback_data=str(places[i]['Name']) + ", Rating {}".format('4'))
        but_5 = types.InlineKeyboardButton(text='⭐⭐⭐⭐️️️️⭐️', callback_data=str(places[i]['Name']) + ", Rating {}".format('5'))
        key.add(but_1, but_2, but_3, but_4, but_5)

        send_photo(user, places[i]['Name'])
        
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
                                                              places[i]['Manager phone number']), reply_markup=key)
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
                                                              places[i]['Working time']), reply_markup=key)
    keyboard_first(user)


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
    
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text='⭐️', callback_data=str(places[i]['Name']) + ", Rating {}".format('1'))
        but_2 = types.InlineKeyboardButton(text='⭐⭐️️', callback_data=str(places[i]['Name']) + ", Rating {}".format('2'))
        but_3 = types.InlineKeyboardButton(text='⭐⭐⭐️️️', callback_data=str(places[i]['Name']) + ", Rating {}".format('3'))
        but_4 = types.InlineKeyboardButton(text='⭐⭐⭐⭐️️️️', callback_data=str(places[i]['Name']) + ", Rating {}".format('4'))
        but_5 = types.InlineKeyboardButton(text='⭐⭐⭐⭐️️️️⭐️', callback_data=str(places[i]['Name']) + ", Rating {}".format('5'))
        key.add(but_1, but_2, but_3, but_4, but_5)

        send_photo(user, places[i]['Name'])
        
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
                                                               places[i]['Manager phone number']), reply_markup=key)
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
                                                              places[i]['Working time']), reply_markup=key)
    keyboard_first(user)


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
    
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text='⭐️', callback_data=str(places[i]['Name']) + ", Rating {}".format('1'))
        but_2 = types.InlineKeyboardButton(text='⭐⭐️️', callback_data=str(places[i]['Name']) + ", Rating {}".format('2'))
        but_3 = types.InlineKeyboardButton(text='⭐⭐⭐️️️', callback_data=str(places[i]['Name']) + ", Rating {}".format('3'))
        but_4 = types.InlineKeyboardButton(text='⭐⭐⭐⭐️️️️', callback_data=str(places[i]['Name']) + ", Rating {}".format('4'))
        but_5 = types.InlineKeyboardButton(text='⭐⭐⭐⭐️️️️⭐️', callback_data=str(places[i]['Name']) + ", Rating {}".format('5'))
        key.add(but_1, but_2, but_3, but_4, but_5)

        send_photo(user, places[i]['Name'])
        
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
                                                               places[i]['Manager phone number']), reply_markup=key)
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
                                                              places[i]['Working time']), reply_markup=key)
    keyboard_first(user)


@bot.message_handler(regexp="Обед-Ужин")
def show_info(message):
    user = message.from_user.id
    places = firebase.get('/nupokushaembot/FoodPlace', '')
    result = []
    
    for i in places:
        if 'Lunch' in places[i]['Food']:
            result.append(i)
    
    bot.send_message(user, "Обед и ужин имеется в следующих местах:")
    
    for i in result:
    
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text='⭐️', callback_data=str(places[i]['Name']) + ", Rating {}".format('1'))
        but_2 = types.InlineKeyboardButton(text='⭐⭐️️', callback_data=str(places[i]['Name']) + ", Rating {}".format('2'))
        but_3 = types.InlineKeyboardButton(text='⭐⭐⭐️️️', callback_data=str(places[i]['Name']) + ", Rating {}".format('3'))
        but_4 = types.InlineKeyboardButton(text='⭐⭐⭐⭐️️️️', callback_data=str(places[i]['Name']) + ", Rating {}".format('4'))
        but_5 = types.InlineKeyboardButton(text='⭐⭐⭐⭐️️️️⭐️', callback_data=str(places[i]['Name']) + ", Rating {}".format('5'))
        key.add(but_1, but_2, but_3, but_4, but_5)

        send_photo(user, places[i]['Name'])
        
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
                                                               places[i]['Manager phone number']), reply_markup=key)
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
                                                              places[i]['Working time']), reply_markup=key)

    keyboard_first(user)


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
    
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text='⭐️', callback_data=str(places[i]['Name']) + ", Rating {}".format('1'))
        but_2 = types.InlineKeyboardButton(text='⭐⭐️️', callback_data=str(places[i]['Name']) + ", Rating {}".format('2'))
        but_3 = types.InlineKeyboardButton(text='⭐⭐⭐️️️', callback_data=str(places[i]['Name']) + ", Rating {}".format('3'))
        but_4 = types.InlineKeyboardButton(text='⭐⭐⭐⭐️️️️', callback_data=str(places[i]['Name']) + ", Rating {}".format('4'))
        but_5 = types.InlineKeyboardButton(text='⭐⭐⭐⭐️️️️⭐️', callback_data=str(places[i]['Name']) + ", Rating {}".format('5'))
        key.add(but_1, but_2, but_3, but_4, but_5)

        send_photo(user, places[i]['Name'])
        
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
                                                               places[i]['Manager phone number']), reply_markup=key)
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
                                                              places[i]['Working time']), reply_markup=key)

    keyboard_first(user)


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
    
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text='⭐️', callback_data=str(places[i]['Name']) + ", Rating {}".format('1'))
        but_2 = types.InlineKeyboardButton(text='⭐⭐️️', callback_data=str(places[i]['Name']) + ", Rating {}".format('2'))
        but_3 = types.InlineKeyboardButton(text='⭐⭐⭐️️️', callback_data=str(places[i]['Name']) + ", Rating {}".format('3'))
        but_4 = types.InlineKeyboardButton(text='⭐⭐⭐⭐️️️️', callback_data=str(places[i]['Name']) + ", Rating {}".format('4'))
        but_5 = types.InlineKeyboardButton(text='⭐⭐⭐⭐️️️️⭐️', callback_data=str(places[i]['Name']) + ", Rating {}".format('5'))
        key.add(but_1, but_2, but_3, but_4, but_5)

        send_photo(user, places[i]['Name'])
        
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
                                                               places[i]['Manager phone number']), reply_markup=key)
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
                                                              places[i]['Working time']), reply_markup=key)

    keyboard_first(user)


def food_tags(user_id):
    markup = types.ReplyKeyboardMarkup()
    item_1 = types.KeyboardButton('Кофе')
    item_2 = types.KeyboardButton('Фаст-фуд')
    item_3 = types.KeyboardButton('Завтрак')
    item_4 = types.KeyboardButton('Обед-Ужин')
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
    ids = []
    
    for i in places:
        ratings.append([i, places[i]['Rating']])
    
    ratings = sorted(ratings, key=itemgetter(1))
    ratings.reverse()
    
    for i in ratings:
        ids.append(i[0])
    
    for i in ids:
    
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text='⭐️', callback_data=str(places[i]['Name']) + ", Rating {}".format('1'))
        but_2 = types.InlineKeyboardButton(text='⭐⭐️️', callback_data=str(places[i]['Name']) + ", Rating {}".format('2'))
        but_3 = types.InlineKeyboardButton(text='⭐⭐⭐️️️', callback_data=str(places[i]['Name']) + ", Rating {}".format('3'))
        but_4 = types.InlineKeyboardButton(text='⭐⭐⭐⭐️️️️', callback_data=str(places[i]['Name']) + ", Rating {}".format('4'))
        but_5 = types.InlineKeyboardButton(text='⭐⭐⭐⭐️️️️⭐️', callback_data=str(places[i]['Name']) + ", Rating {}".format('5'))
        key.add(but_1, but_2, but_3, but_4, but_5)

        send_photo(user_id, places[i]['Name'])
        
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
                                                                  places[i]['Manager phone number']), reply_markup=key)
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
                                                                 places[i]['Working time']), reply_markup=key)
            
    keyboard_first(user_id)


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
    
    
def random_generator():
    code = numpy.random.randint(low=1000,high=9999)
    print(code)
    return code


def verify_user(user_id, user_email):
    bot.send_message(user_id, "Please enter the message reply")
    port = 465
    sender = "saadatsunnysmile@gmail.com"
    send_psw = "GGGg5555"

    code = random_generator()

    message = """\
    NU pokushaem! Verification Code

    """ + str(code) + """

    Please, send this code to bot.
    """
    context = ssl.create_default_context()
    print("Sending message")

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender, send_psw)
        server.sendmail(sender, user_email, message)

    print("Message sent")

    @bot.message_handler(regexp="[0-9]{4}")
    def code_verification(message):
        user_id = message.from_user.id
        local_code = message.text
        if str(local_code) == str(code):
            # go-to options keyboard
            keyboard_first(user_id)


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


@bot.message_handler(regexp="@")
def handle_email(message):
    user = message.from_user.id
    email = message.text
    # check domain
    if re.search("@nu.edu.kz", email):
        # TO-DO handle email
        print("verify_user")
        bot.send_message(user, "You recieve a message")
        verify_user(user, email)
    
    
    elif (re.search("@", email)):
        bot.send_message(user, "Пожалуйста, введите email с @nu.edu.kz.")


@bot.message_handler(content_types=['voice'])
def get_audio_messages(message):
    user = message.from_user.id
    bot.send_message(user, "Can not process audio")


bot.polling(none_stop=True, interval=0)
