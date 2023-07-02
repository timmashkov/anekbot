import random

import requests
import telebot
from bs4 import BeautifulSoup as blink

URL = 'https://www.anekdot.ru/last/good'
TELEGRAM_TOKEN = '5804833881:AAF6o7jO11s7sY-d6OSaWjrgjv9yS6e4dzI'


def anekdot_parser(url: str) -> list:
    """Функция-парсер, получает URL строкой, парсит и возвращает список строк"""
    get_request = requests.get(URL)
    soup = blink(get_request.text, 'html.parser')
    anekdots = soup.find_all('div', class_='text')
    return [i.text for i in anekdots]


jokes_list = anekdot_parser(URL)
random.shuffle(jokes_list)

bot = telebot.TeleBot(TELEGRAM_TOKEN)


@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.chat.id, 'Если хочешь анекдот напиши: хочу смеяться 5 минут')


@bot.message_handler(content_types=['text'])
def get_from_user(message):
    if message.text.lower() == 'хочу смеяться 5 минут':
        bot.send_message(message.chat.id, jokes_list[0])
        del jokes_list[0]
    else:
        bot.send_message(message.chat.id, 'Если хочешь анекдот напиши: хочу смеяться 5 минут')


bot.polling()
