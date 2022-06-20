import telebot
import settings
from telebot import types

bot = telebot.TeleBot(settings.TOKEN)


def send_welcome(message):
    bot.reply_to(message, "Привет, новый друг!\nВведи '/go' для начала опроса\nЕсли хочешь узнать о видах удобрений, введи '/fertilizer'\nЕсли хочешь узнать что-то ещё - введи '/questions'\nЕсли не хочешь проходить опрос - нажми '/random', чтобы получить название любого цветка")


def help_f(message):
    bot.reply_to(message, "Команды:\n/go - запуск опроса\n/questions - информация об уходе за цветами\n/fertilizer - узнать больше об удобрениях\n/random - даёт название любого цветка, если не хочешь проходить опрос")


def go_to(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Цветущий')
    btn2 = types.KeyboardButton('Не цветущий')
    markup.add(btn1, btn2)
    bot.reply_to(message, "Выбери вариант ответа!", reply_markup=markup)


def questions(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Полив')
    btn2 = types.KeyboardButton('Посадка')
    btn3 = types.KeyboardButton('Удобрение')
    btn4 = types.KeyboardButton('Освещение')
    btn5 = types.KeyboardButton('Температура')
    markup.add(btn1, btn2, btn3, btn4, btn5)
    bot.reply_to(message, "Что бы вы хотели узнать?", reply_markup=markup)


def fertilizer(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Органические')
    btn2 = types.KeyboardButton('Не органические')
    btn3 = types.KeyboardButton('Бактериальные')
    btn4 = types.KeyboardButton('Стимуляторы роста')
    markup.add(btn1, btn2, btn3, btn4)
    bot.reply_to(message, "О каком виде удобрений вы хотите узнать?", reply_markup=markup)


def random_f(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Рандомный цветок')
    markup.add(btn1)
    bot.reply_to(message, "Нажмите на кнопку", reply_markup=markup)
