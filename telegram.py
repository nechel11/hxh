from dataclasses import replace
from xmlrpc.client import boolean
import telebot
from telebot import types
import hh_api
import re
from utils import utils_error

bot = telebot.TeleBot('5432709533:AAF5jAjDJNbZsE2LtsGO7qwd0dwPvuTThKA')
dict = {'page' : 0}
page = 0

@bot.message_handler(commands=['start'])
def start(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	btn_next = types.KeyboardButton('Start')
	markup.add(btn_next)
	bot.send_message(message.chat.id, 
 		f"Привет, <b>{message.from_user.first_name}</b>. Жми старт для начала поиска",
 		reply_markup=markup, parse_mode='html')


@bot.message_handler(content_types=['text'])
def get_user_text(message):
	lst = []
	if message.text == 'Start':
		msg = bot.send_message(message.chat.id, 'Укажи профессию <u>(1-2 слова)</u>', parse_mode='html')
		bot.register_next_step_handler(msg, proff_to_dict)
	elif (message.text == 'finish'):
		if (utils_error.dict_cheq(dict, message, bot)):
			try :
				lst = hh_api.get_package(dict)
			except Exception as e:
				bot.send_message(message.chat.id, f'что-то пошло не так. попробуй еще раз через 10 мин, если не работает, то пиши автору')
			if not lst:
				utils_error.error_handler(message, dict, bot)
			markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
			btn_more = types.KeyboardButton('Ещё')
			markup.add(btn_more)
			for k in lst:
				bot.send_message(message.chat.id, k, parse_mode='html', disable_web_page_preview=True, reply_markup=markup)
			print(dict)
		else : 
			bot.send_message(message.chat.id, 'Попробуй заново <u> /start </u>' , parse_mode='html')
	elif(message.text == 'Ещё'):
		dict['page'] += 1
		if (utils_error.dict_cheq(dict, message, bot)):
			try :
				lst = hh_api.get_package(dict)
			except Exception as e:
				bot.send_message(message.chat.id, 'что-то пошло не так. проверь данные. если все ок, то пиши автору')
			if not lst:
				utils_error.error_handler(message, dict, bot)
			markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
			btn_more = types.KeyboardButton('Ещё')
			for k in lst:
				bot.send_message(message.chat.id, k, parse_mode='html', disable_web_page_preview=True, reply_markup=markup)
		else : 
			bot.send_message(message.chat.id, 'Попробуй заново <u> /start </u>' , parse_mode='html')	
		print(dict)	
	else :
		bot.send_message(message.chat.id, 'пишешь что-то непонятное...')


def proff_to_dict(message):
	dict['text'] = message.text
	dict['page'] = 0
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	btn_city_moscow = types.KeyboardButton('Москва')
	btn_city_tashkent = types.KeyboardButton('Ташкент')
	btn_city_spb = types.KeyboardButton('СПБ')
	markup.add(btn_city_moscow, btn_city_spb, btn_city_tashkent)
	msg = bot.send_message(message.chat.id, 'Выбери город', reply_markup=markup)	
	bot.register_next_step_handler(msg, city_to_dict)


def city_to_dict(message):
	if message.text=='Москва':
		dict['city'] = 1
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		btn_currency_1 = types.KeyboardButton('RUR')
		btn_currency_2 = types.KeyboardButton('USD')
		markup.add(btn_currency_1,btn_currency_2 )
		msg = bot.send_message(message.chat.id, 'Выбери валюту з\п', reply_markup=markup)
		bot.register_next_step_handler(msg, currency_to_dict)
	elif message.text=='СПБ':
		dict['city'] = 2
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		btn_currency_1 = types.KeyboardButton('RUR')
		btn_currency_2 = types.KeyboardButton('USD')
		markup.add(btn_currency_1,btn_currency_2 )
		msg = bot.send_message(message.chat.id, 'Выбери валюту з\п', reply_markup=markup)
		bot.register_next_step_handler(msg, currency_to_dict)
	elif message.text=='Ташкент':
		dict['city'] = 2759
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		btn_currency_1 = types.KeyboardButton('RUR')
		btn_currency_2 = types.KeyboardButton('USD')
		markup.add(btn_currency_1,btn_currency_2 )
		msg = bot.send_message(message.chat.id, 'Выбери валюту з\п', reply_markup=markup)
		bot.register_next_step_handler(msg, currency_to_dict)
	else:
		msg_error = bot.send_message(message.chat.id, 'Выбери из трех предложенных')
		bot.register_next_step_handler(msg_error, city_to_dict)
	

def currency_to_dict(message):
	if  message.text =='RUR' :
		dict['currency'] = message.text
		markup_3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
		btn_salary_1 = types.KeyboardButton("50'000")
		btn_salary_2 = types.KeyboardButton("100'000")
		btn_salary_3 = types.KeyboardButton("150'000")
		btn_salary_4 = types.KeyboardButton("200'000")
		markup_3.add(btn_salary_1, btn_salary_2, btn_salary_3, btn_salary_4)
		msg = bot.send_message(message.chat.id, 'Выбери з\п или укажи свою', reply_markup=markup_3)
		bot.register_next_step_handler(msg, salary_to_dict)
	elif message.text =='USD' : 
		dict['currency'] = message.text
		markup_4 = types.ReplyKeyboardMarkup(resize_keyboard=True)
		btn_salary_USD_1 = types.KeyboardButton("1'000")
		btn_salary_USD_2 = types.KeyboardButton("1'500")
		btn_salary_USD_3 = types.KeyboardButton("2'000")
		btn_salary_USD_4 = types.KeyboardButton("3'000")
		markup_4.add(btn_salary_USD_1, btn_salary_USD_2, btn_salary_USD_3, btn_salary_USD_4)
		msg = bot.send_message(message.chat.id, 'Выбери з\п или укажи свою', reply_markup=markup_4)
		bot.register_next_step_handler(msg, salary_to_dict)
	else :
		msg_error = bot.send_message(message.chat.id, 'Неверная валюта')
		bot.register_next_step_handler(msg_error, currency_to_dict)	
		

def salary_to_dict(message):
	dict['salary'] = re.sub("[^0-9]", "", message.text)
	markup_5 = types.ReplyKeyboardMarkup(resize_keyboard=True)
	btn_per_page_1 = types.KeyboardButton(5)
	btn_per_page_2 = types.KeyboardButton(10)
	btn_per_page_3 = types.KeyboardButton(15)
	btn_per_page_4 = types.KeyboardButton(20)
	markup_5.add(btn_per_page_1, btn_per_page_2, btn_per_page_3, btn_per_page_4)
	msg = bot.send_message(message.chat.id, 'Выбери кол-во выгружаемых вакансий или укажи свое', reply_markup=markup_5)
	bot.register_next_step_handler(msg, per_page_to_dict)


def per_page_to_dict(message):
	dict['per_page'] = message.text
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	btn_finish = types.KeyboardButton('finish')
	markup.add(btn_finish)
	bot.send_message(message.chat.id, 'Жми <u>финиш</u> для окончания', reply_markup=markup, parse_mode='html')


bot.polling(non_stop=True)