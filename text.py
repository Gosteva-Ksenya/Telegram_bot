from telebot import types
import qestions
from commands import bot
import flowers
import fertilizers
import random


def mess(message):
    get_message_bot = message.text.strip().lower()

    if get_message_bot == 'цветущий':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Однолетний')
        btn2 = types.KeyboardButton('Многолетний')
        markup.add(btn1, btn2)
        final_text = 'Сколько будет жить ваш цветок?'

    elif get_message_bot == 'не цветущий':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Высокий')
        btn2 = types.KeyboardButton('Низкий')
        markup.add(btn1, btn2)
        final_text = 'Какой высоты будет ваше растение?'

    elif get_message_bot == 'однолетний':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=False)
        final_text = flowers.Petunia
        photo = open("photo/петуния.jpg", "rb")
        bot.send_photo(message.chat.id, photo)

    elif get_message_bot == 'многолетний':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=False)
        final_text = flowers.Gwozdika
        photo = open("photo/гвоздика.jpg", "rb")
        bot.send_photo(message.chat.id, photo)

    elif get_message_bot == 'высокий':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=False)
        final_text = flowers.Ficus
        photo = open("photo/фикус.jpg", "rb")
        bot.send_photo(message.chat.id, photo)

    elif get_message_bot == 'низкий':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=False)
        final_text = flowers.Kaktus
        photo = open("photo/кактус.jpg", "rb")
        bot.send_photo(message.chat.id, photo)

    elif get_message_bot == 'органические':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=False)
        final_text = fertilizers.Organicheskie

    elif get_message_bot == 'не органические':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=False)
        final_text = fertilizers.Neorganicheskie

    elif get_message_bot == 'бактериальные':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=False)
        final_text = fertilizers.Bacterii

    elif get_message_bot == 'стимуляторы роста':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=False)
        final_text = fertilizers.Rost

    elif get_message_bot == 'полив':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=False)
        final_text = qestions.Poliv

    elif get_message_bot == 'посадка':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=False)
        final_text = qestions.Posadka

    elif get_message_bot == 'удобрение':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=False)
        final_text = qestions.Udobrenie

    elif get_message_bot == 'освещение':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=False)
        final_text = qestions.Swet

    elif get_message_bot == 'температура':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=False)
        final_text = qestions.Temperatura

    elif get_message_bot == 'рандомный цветок':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=False)
        final_text = random.choice(flowers.Random_flower)

    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=False)
        final_text = "Я не понимаю, нажмите /help для выбора команды"

    bot.reply_to(message, final_text, reply_markup=markup)
