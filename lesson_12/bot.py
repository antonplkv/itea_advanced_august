from telebot import TeleBot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import random
TOKEN = '1334641500:AAH79AO7m0iyr7LX509qL4cZPI3MBRgJy8E'

NICE_MOOD = 'Хорошее :)'
BAD_MOOD = 'Плохое :('

bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def handle_start(message):
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    nice = KeyboardButton(text=NICE_MOOD)
    bad = KeyboardButton(text=BAD_MOOD)
    kb.add(nice, bad)
    bot.send_message(
        message.chat.id,
        'Как Ваше настроение?',
        reply_markup=kb
    )


@bot.message_handler(content_types=['contact'])
def handle_contact(message):
    print(message.contact)
    print(message.contact.phone_number)
    print(message.contact.first_name)


@bot.message_handler(func=lambda m: m.text in (BAD_MOOD, NICE_MOOD))
def handle_bad_mood(message):

    if message.text == BAD_MOOD:
        text = 'Не грусти'
    else:
        text = 'Так держать!'
    bot.send_message(
        message.chat.id,
        text
    )


@bot.message_handler(commands=['random'])
def handle_random(message):
    random_number = random.randint(0, 1000)
    bot.send_message(
        message.chat.id,
        f'Ваше случайное число - {random_number}!'
    )


# def hello(message):
#     return message.text == 'Привет'


# @bot.message_handler(func=hello)
@bot.message_handler(func=lambda m: m.text == 'Привет')
def handle_hello(message):
    list_of_greetings = ['Hi', 'Hello', 'My greetings!', 'Salut']
    bot.send_message(
        message.chat.id,
        random.choice(list_of_greetings)
    )


# @bot.message_handler(content_types=['text'])
# def handle_text(message):
#     bot.send_message(message.chat.id, 'Спасибо за сообщение!')


@bot.message_handler(content_types=['text'])
def handle_text(message):
    print(message)
    bot.send_message(
        message.chat.id,
        message.text[::-1]
    )


bot.polling()