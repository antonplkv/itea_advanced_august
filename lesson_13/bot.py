from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = TeleBot('1334641500:AAH79AO7m0iyr7LX509qL4cZPI3MBRgJy8E')


@bot.message_handler(commands=['start'])
def start(message):
    kb = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton(text='Привет',
                                   callback_data='hi')
    button2 = InlineKeyboardButton(text='Пока', callback_data='bye',
                                   url='https://google.com/')
    kb.add(button1, button2)
    bot.send_message(
        message.chat.id,
        'Здравствуйте',
        reply_markup=kb
    )


@bot.callback_query_handler(func=lambda call: call.data == 'hi')
def handle_callback_hi(call):
    bot.send_message(
        call.message.chat.id,
        'Ещё раз привет'
    )


@bot.callback_query_handler(func=lambda call: call.data == 'bye')
def handle_callback_bye(call):
    bot.send_message(
        call.message.chat.id,
        'Пока :('
    )


print()
bot.polling()