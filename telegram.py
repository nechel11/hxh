from dataclasses import replace
import telebot
from telebot import types
import hh_api

bot = telebot.TeleBot('5432709533:AAF5jAjDJNbZsE2LtsGO7qwd0dwPvuTThKA')
dict = {}
page = 0

@bot.message_handler(commands=['start'])
def start(message, *args):
	
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	btn_next = types.KeyboardButton('Шаг 1')
	markup.add(btn_next)
	bot.send_message(message.chat.id, 
 		f"Привет, <b>{message.from_user.first_name}</b>. укажи профессию (1-2 слова), отправь сообщение, после нажми кнопку",
 		reply_markup=markup, parse_mode='html')
	dict['text'] = message.text


# @bot.message_handler(commands=['start'])
# def start(message, *args):
# 	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
# 	dict['text'] = message.text
# 	city_moscow = types.KeyboardButton('Москва')
# 	city_tashkent = types.KeyboardButton('Ташкент')
# 	city_spb = types.KeyboardButton('СПБ')
# 	markup.add(city_moscow, city_spb, city_tashkent)
# 	bot.send_message(message.chat.id, 
# 		f"Привет, <b>{message.from_user.first_name}</b>, укажи профессию (1-2 слова), затем выбери город",
# 		reply_markup=markup, parse_mode='html')



@bot.message_handler(content_types=['text'])
def get_user_text(message):
	if message.text=='Шаг 1':
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		btn_city_moscow = types.KeyboardButton('Москва')
		btn_city_tashkent = types.KeyboardButton('Ташкент')
		btn_city_spb = types.KeyboardButton('СПБ')
		markup.add(btn_city_moscow, btn_city_spb, btn_city_tashkent)
		bot.send_message(message.chat.id, "выбери город", reply_markup=markup)
		if message.text=='Москва':
			dict['city'] = 1
		elif message.text=='СПБ':
			dict['city'] = 2
		elif message.text=='Ташкент':
			dict['city'] = 2759
	if (message.text == 'Москва' or message.text == 'СПБ' or message.text == 'Ташкент'):
		markup_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
		btn_currency_1 = types.KeyboardButton('RUR')
		btn_currency_2 = types.KeyboardButton('USD')
		markup_2.add(btn_currency_1,btn_currency_2 )
		bot.send_message(message.chat.id, 'Выбери валюту з\п', reply_markup=markup_2)
		dict['currency'] = message.text
	if (message.text=='RUR'):
		markup_3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
		btn_salary_1 = types.KeyboardButton(50000)
		btn_salary_2 = types.KeyboardButton(100000)
		btn_salary_3 = types.KeyboardButton(150000)
		btn_salary_4 = types.KeyboardButton(200000)
		markup_3.add(btn_salary_1, btn_salary_2, btn_salary_3, btn_salary_4)
		bot.send_message(message.chat.id, 'Выбери з\п', reply_markup=markup_3)
		dict['salary'] = message.text
	if (message.text=='USD'):
		markup_4 = types.ReplyKeyboardMarkup(resize_keyboard=True)
		btn_salary_USD_1 = types.KeyboardButton(1000)
		btn_salary_USD_2 = types.KeyboardButton(1500)
		btn_salary_USD_3 = types.KeyboardButton(2000)
		btn_salary_USD_4 = types.KeyboardButton(3000)
		markup_4.add(btn_salary_USD_1, btn_salary_USD_2, btn_salary_USD_3, btn_salary_USD_4)
		bot.send_message(message.chat.id, 'Выбери з\п', reply_markup=markup_4)
		dict['salary'] = message.text
	if (message.text == '50000' or message.text == '100000' or 
			message.text == '150000' or message.text == '200000'):
		markup_5 = types.ReplyKeyboardMarkup(resize_keyboard=True)
		btn_per_page_1 = types.KeyboardButton(5)
		btn_per_page_2 = types.KeyboardButton(10)
		btn_per_page_3 = types.KeyboardButton(15)
		btn_per_page_4 = types.KeyboardButton(20)
		markup_5.add(btn_per_page_1, btn_per_page_2, btn_per_page_3, btn_per_page_4)
		bot.send_message(message.chat.id, 'Выбери кол-во выгружаемых вакансий', reply_markup=markup_5)
		dict['per_page'] = message.text
	print(dict)



	# if message.text=='finish':
	# 	mess = hh_api.get_package(dict)
	# 	for k in mess:
	# 		bot.send_message(message.chat.id, k, parse_mode='html',
	# 			disable_web_page_preview=True)

bot.polling(non_stop=True)