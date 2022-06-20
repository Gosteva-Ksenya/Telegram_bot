import commands
import text
from commands import bot


@bot.message_handler(commands=['start'])
def send_welcome1(message):
    commands.send_welcome(message)


@bot.message_handler(commands=['go'])
def go_to1(message):
    commands.go_to(message)


@bot.message_handler(commands=['help'])
def go_to1(message):
    commands.help_f(message)


@bot.message_handler(commands=['fertilizer'])
def fertilizer1(message):
    commands.fertilizer(message)


@bot.message_handler(commands=['questions'])
def questions1(message):
    commands.questions(message)


@bot.message_handler(commands=['random'])
def random_f1(message):
    commands.random_f(message)


@bot.message_handler(content_types=['text'])
def mess1(message):
    text.mess(message)


bot.infinity_polling()
