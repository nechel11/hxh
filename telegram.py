import telebot
from telebot import types
import hh_api

bot = telebot.TeleBot('5432709533:AAF5jAjDJNbZsE2LtsGO7qwd0dwPvuTThKA')

dict = {}

@bot.message_handler(commands=['start'])
def start(message):
	mess = hh_api.get_package()
	for k in mess:
		bot.send_message(message.chat.id, k,
			parse_mode='html', disable_web_page_preview=True)



@bot.message_handler(commands=['help'])
def website(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True,
		row_width=3)
	city_moscow = types.KeyboardButton('Москва')
	city_tashkent = types.KeyboardButton('Ташкент')
	city_spb = types.KeyboardButton('СПБ')

	markup.add(city_moscow, city_tashkent, city_spb)
	bot.send_message(message.chat.id, 'Выберете город ',
		reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_user_text(message):
	if message.text=='finish':
		bot.send_message(message.chat.id, ':)', parse_mode='html')

bot.polling(non_stop=True)