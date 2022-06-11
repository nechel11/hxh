import telebot
from telebot import types
import hh_api
import re

def proff_to_dict(message, dict, bot):
	dict['text'] = message.text
	dict['page'] = 0
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	btn_city_moscow = types.KeyboardButton('Москва')
	btn_city_tashkent = types.KeyboardButton('Ташкент')
	btn_city_spb = types.KeyboardButton('СПБ')
	markup.add(btn_city_moscow, btn_city_spb, btn_city_tashkent)
	msg = bot.send_message(message.chat.id, 'Выбери город', reply_markup=markup)	
	bot.register_next_step_handler(msg, city_to_dict, dict, bot)

def city_to_dict(message, dict, bot):
	if message.text=='Москва':
		dict['city'] = 1
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		btn_currency_1 = types.KeyboardButton('RUR')
		btn_currency_2 = types.KeyboardButton('USD')
		markup.add(btn_currency_1,btn_currency_2 )
		msg = bot.send_message(message.chat.id, 'Выбери валюту з\п', reply_markup=markup)
		bot.register_next_step_handler(msg, currency_to_dict, dict, bot)
	elif message.text=='СПБ':
		dict['city'] = 2
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		btn_currency_1 = types.KeyboardButton('RUR')
		btn_currency_2 = types.KeyboardButton('USD')
		markup.add(btn_currency_1,btn_currency_2 )
		msg = bot.send_message(message.chat.id, 'Выбери валюту з\п', reply_markup=markup)
		bot.register_next_step_handler(msg, currency_to_dict, dict, bot)
	elif message.text=='Ташкент':
		dict['city'] = 2759
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		btn_currency_1 = types.KeyboardButton('RUR')
		btn_currency_2 = types.KeyboardButton('USD')
		markup.add(btn_currency_1,btn_currency_2 )
		msg = bot.send_message(message.chat.id, 'Выбери валюту з\п', reply_markup=markup)
		bot.register_next_step_handler(msg, currency_to_dict, dict, bot)
	else:
		msg_error = bot.send_message(message.chat.id, 'Выбери из трех предложенных')
		bot.register_next_step_handler(msg_error, city_to_dict, dict, bot)
	

def currency_to_dict(message, dict, bot):
	if  message.text =='RUR' :
		dict['currency'] = message.text
		markup_3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
		btn_salary_1 = types.KeyboardButton("50'000")
		btn_salary_2 = types.KeyboardButton("100'000")
		btn_salary_3 = types.KeyboardButton("150'000")
		btn_salary_4 = types.KeyboardButton("200'000")
		markup_3.add(btn_salary_1, btn_salary_2, btn_salary_3, btn_salary_4)
		msg = bot.send_message(message.chat.id, 'Выбери з\п или укажи свою', reply_markup=markup_3)
		bot.register_next_step_handler(msg, salary_to_dict, dict, bot)
	elif message.text =='USD' : 
		dict['currency'] = message.text
		markup_4 = types.ReplyKeyboardMarkup(resize_keyboard=True)
		btn_salary_USD_1 = types.KeyboardButton("1'000")
		btn_salary_USD_2 = types.KeyboardButton("1'500")
		btn_salary_USD_3 = types.KeyboardButton("2'000")
		btn_salary_USD_4 = types.KeyboardButton("3'000")
		markup_4.add(btn_salary_USD_1, btn_salary_USD_2, btn_salary_USD_3, btn_salary_USD_4)
		msg = bot.send_message(message.chat.id, 'Выбери з\п или укажи свою', reply_markup=markup_4)
		bot.register_next_step_handler(msg, salary_to_dict, dict, bot)
	else :
		msg_error = bot.send_message(message.chat.id, 'Неверная валюта')
		bot.register_next_step_handler(msg_error, currency_to_dict,dict, bot)	
		

def salary_to_dict(message, dict, bot):
	dict['salary'] = re.sub("[^0-9]", "", message.text)
	markup_5 = types.ReplyKeyboardMarkup(resize_keyboard=True)
	btn_per_page_1 = types.KeyboardButton(5)
	btn_per_page_2 = types.KeyboardButton(10)
	btn_per_page_3 = types.KeyboardButton(15)
	btn_per_page_4 = types.KeyboardButton(20)
	markup_5.add(btn_per_page_1, btn_per_page_2, btn_per_page_3, btn_per_page_4)
	msg = bot.send_message(message.chat.id, 'Выбери кол-во выгружаемых вакансий или укажи свое', reply_markup=markup_5)
	bot.register_next_step_handler(msg, per_page_to_dict, dict, bot)


def per_page_to_dict(message, dict, bot):
	dict['per_page'] = message.text
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	btn_finish = types.KeyboardButton('finish')
	markup.add(btn_finish)
	bot.send_message(message.chat.id, 'Жми <u>финиш</u> для окончания', reply_markup=markup, parse_mode='html')