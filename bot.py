import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot(TOKEN)

film_types = {
    'btn1' : 'Боевик',
    'btn2' : 'Фантастика',
    'btn3' : 'Хоррор',
    'btn4' : 'Детектив',
    'btn5' : 'Драма'
}

action_movies = {
    'act_btn1': ('Переводчик (2022)', 'https://www.kinopoisk.ru/film/4771831/'),
    'act_btn2': ('Шерлок Холмс (2009)', 'https://www.kinopoisk.ru/film/420923/'),
    'act_btn3': ('Бесславные ублюдки (2009)', 'https://www.kinopoisk.ru/film/939444/'),
    'act_btn4': ('Джон Уик 4 (2023)', 'https://www.kinopoisk.ru/film/1236063/'),
    'act_btn5': ('Никто (2021)', 'https://www.kinopoisk.ru/film/1346871/')
}

fantasy_movies = {
    'fan_btn1': ('Начало (2010)', 'https://www.kinopoisk.ru/film/447301/'),
    'fan_btn2': ('Интерстеллар (2014)', 'https://www.kinopoisk.ru/film/258687/'),
    'fan_btn3': ('Темный рыцарь (2008)', 'https://www.kinopoisk.ru/film/111543/'),
    'fan_btn4': ('Матрица (1999)', 'https://www.kinopoisk.ru/film/301/'),
    'fan_btn5': ('Мстители: Война бесконечности (2018)', 'https://www.kinopoisk.ru/film/843649/')
}

horror_movies = {
    'hor_btn1': ('Молчание ягнят (1990)', 'https://www.kinopoisk.ru/film/345/'),
    'hor_btn2': ('Репортаж (2007)', 'https://www.kinopoisk.ru/film/278276/'),
    'hor_btn3': ('Хостел (2005)', 'https://www.kinopoisk.ru/film/103369/'),
    'hor_btn4': ('Астрал: Глава 2 (2013)', 'https://www.kinopoisk.ru/film/653716/'),
    'hor_btn5': ('Астрал. Проклятие мёртвых (2024)', 'https://www.kinopoisk.ru/film/5382258/')
}

detective_movies = {
    'det_btn1': ('Шестое чувство (1999)', 'https://www.kinopoisk.ru/film/439/'),
    'det_btn2': ('Порок (2001)', 'https://www.kinopoisk.ru/film/5275/'),
    'det_btn3': ('Остров проклятых (2010)', 'https://www.kinopoisk.ru/film/397667/'),
    'det_btn4': ('Семь (1995)', 'https://www.kinopoisk.ru/film/377/'),
    'det_btn5': ('Девушка с татуировкой дракона (2011)', 'https://www.kinopoisk.ru/film/468466/')
}

drama_movies = {
    'dra_btn1': ('Выживший (2015)', 'https://www.kinopoisk.ru/film/682280/'),
    'dra_btn2': ('Игры разума (2001)', 'https://www.kinopoisk.ru/film/530/'),
    'dra_btn3': ('Старикам тут не место (2007)', 'https://www.kinopoisk.ru/film/195524/'),
    'dra_btn4': ('Побег из Шоушенка (1994)', 'https://www.kinopoisk.ru/film/326/'),
    'dra_btn5': ('Человек на Луне (2018)', 'https://www.kinopoisk.ru/film/1046371/')
}

def get_inline_keyboards():
  markup = InlineKeyboardMarkup()
  markup.add(InlineKeyboardButton('Боевик', callback_data='btn1'))
  markup.add(InlineKeyboardButton('Фантастика', callback_data='btn2'))
  markup.add(InlineKeyboardButton('Хоррор', callback_data='btn3'))
  markup.add(InlineKeyboardButton('Детектив', callback_data='btn4'))
  markup.add(InlineKeyboardButton('Драма', callback_data='btn5'))
  return markup

def get_inline_keyboards_action():
  markup = InlineKeyboardMarkup()
  markup.add(InlineKeyboardButton('Переводчик (2022)', callback_data='act_btn1'))
  markup.add(InlineKeyboardButton('Шерлок Холмс (2009)', callback_data='act_btn2'))
  markup.add(InlineKeyboardButton('Бесславные ублюдки (2009)', callback_data='act_btn3'))
  markup.add(InlineKeyboardButton('Джон Уик 4 (2023)', callback_data='act_btn4'))
  markup.add(InlineKeyboardButton('Никто (2021)', callback_data='act_btn5'))
  return markup

def get_inline_keyboards_fantasy():
  markup = InlineKeyboardMarkup()
  markup.add(InlineKeyboardButton('Начало (2010)', callback_data='fan_btn1'))
  markup.add(InlineKeyboardButton('Интерстеллар (2014)', callback_data='fan_btn2'))
  markup.add(InlineKeyboardButton('Темный рыцарь (2008)', callback_data='fan_btn3'))
  markup.add(InlineKeyboardButton('Матрица (1999)', callback_data='fan_btn4'))
  markup.add(InlineKeyboardButton('Мстители: Война бесконечности (2018)', callback_data='fan_btn5'))
  return markup

def get_inline_keyboards_horror():
  markup = InlineKeyboardMarkup()
  markup.add(InlineKeyboardButton('Молчание ягнят (1990)', callback_data='hor_btn1'))
  markup.add(InlineKeyboardButton('Репортаж (2007)', callback_data='hor_btn2'))
  markup.add(InlineKeyboardButton('Хостел (2005)', callback_data='hor_btn3'))
  markup.add(InlineKeyboardButton('Астрал: Глава 2 (2013)', callback_data='hor_btn4'))
  markup.add(InlineKeyboardButton('Астрал. Проклятие мёртвых (2024)', callback_data='hor_btn5'))
  return markup

def get_inline_keyboards_detective():
  markup = InlineKeyboardMarkup()
  markup.add(InlineKeyboardButton('Шестое чувство (1999)', callback_data='det_btn1'))
  markup.add(InlineKeyboardButton('Порок (2001)', callback_data='det_btn2'))
  return markup

def get_inline_keyboards_drama():
  markup = InlineKeyboardMarkup()
  markup.add(InlineKeyboardButton('Выживший (2015)', callback_data='dra_btn1'))
  markup.add(InlineKeyboardButton('Игры разума (2001)', callback_data='dra_btn2'))
  markup.add(InlineKeyboardButton('Старикам тут не место (2007)', callback_data='dra_btn3'))
  markup.add(InlineKeyboardButton('Побег из Шоушенка (1994)', callback_data='dra_btn4'))
  markup.add(InlineKeyboardButton('Человек на Луне (2018)', callback_data='dra_btn5'))
  return markup


@bot.message_handler(commands = ['start'])
def films(message):
  bot.send_message(message.chat.id, 'Привет Напиши команду /film')

@bot.message_handler(commands=['film'])
def cinema(message):
  bot.send_message(message.chat.id, 'Какой вд фильма хочешь посмотреть ?', reply_markup=get_inline_keyboards())


@bot.callback_query_handler(func=lambda call:call.data in film_types.keys())
def handle_inline_keyboards(call):
  genre = film_types[call.data]
  if genre == 'Боевик':
    bot.send_message(call.message.chat.id, 'Вот Фильмы боевики', reply_markup=get_inline_keyboards_action())
  elif genre == 'Фантастика':
    bot.send_message(call.message.chat.id, 'Вот Фильмы фантастики', reply_markup=get_inline_keyboards_fantasy())
  elif genre == 'Хоррор':
    bot.send_message(call.message.chat.id, 'Вот Фильмы хорроры', reply_markup=get_inline_keyboards_horror())
  elif genre == 'Детектив':
    bot.send_message(call.message.chat.id, 'Вот Фильмы детективы', reply_markup=get_inline_keyboards_detective())
  elif genre == 'Драма':
    bot.send_message(call.message.chat.id, 'Вот Фильмы драмы', reply_markup=get_inline_keyboards_drama())


@bot.callback_query_handler(func=lambda call: call.data in action_movies.keys())
def link_ac(call):
  name, link = action_movies[call.data]
  bot.send_message(call.message.chat.id, f'{name} : {link}')

@bot.callback_query_handler(func=lambda call: call.data in fantasy_movies.keys())
def link_fa(call):
  name, link = fantasy_movies[call.data]
  bot.send_message(call.message.chat.id, f'{name} : {link}')

@bot.callback_query_handler(func=lambda call: call.data in horror_movies.keys())
def link_hor(call):
  name, link = horror_movies[call.data]
  bot.send_message(call.message.chat.id, f'{name} : {link}')

@bot.callback_query_handler(func=lambda call: call.data in detective_movies.keys())
def link_det(call):
  name, link = detective_movies[call.data]
  bot.send_message(call.message.chat.id, f'{name} : {link}')

@bot.callback_query_handler(func=lambda call: call.data in drama_movies.keys())
def link_dra(call):
  name, link = drama_movies[call.data]
  bot.send_message(call.message.chat.id, f'{name} : {link}')

bot.infinity_polling()
