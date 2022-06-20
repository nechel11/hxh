import telebot
from telebot import types
import re
from utils  import msg_handler

def proff_to_dict(message, dict, bot):
	dict['text'] = message.text
	dict['page'] = 0
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	btn_city_moscow = types.KeyboardButton('Moscow')
	btn_city_tashkent = types.KeyboardButton('Tashkent')
	btn_city_spb = types.KeyboardButton('SPB')
	markup.add(btn_city_moscow, btn_city_spb, btn_city_tashkent)
	msg = bot.send_message(message.chat.id, 'Choose city', reply_markup=markup)	
	bot.register_next_step_handler(msg, city_to_dict, dict, bot)
	return dict

def city_to_dict(message, dict, bot):
	if message.text=='Moscow':
		dict['city'] = 1
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		btn_currency_1 = types.KeyboardButton('RUR')
		btn_currency_2 = types.KeyboardButton('USD')
		markup.add(btn_currency_1,btn_currency_2 )
		msg = bot.send_message(message.chat.id, 'Choose salary currency', reply_markup=markup)
		bot.register_next_step_handler(msg, currency_to_dict, dict, bot)
	elif message.text=='SPB':
		dict['city'] = 2
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		btn_currency_1 = types.KeyboardButton('RUR')
		btn_currency_2 = types.KeyboardButton('USD')
		markup.add(btn_currency_1,btn_currency_2 )
		msg = bot.send_message(message.chat.id, 'Choose salary currency', reply_markup=markup)
		bot.register_next_step_handler(msg, currency_to_dict, dict, bot)
	elif message.text=='Tashkent':
		dict['city'] = 2759
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		btn_currency_1 = types.KeyboardButton('RUR')
		btn_currency_2 = types.KeyboardButton('USD')
		markup.add(btn_currency_1,btn_currency_2 )
		msg = bot.send_message(message.chat.id, 'Choose salary currency', reply_markup=markup)
		bot.register_next_step_handler(msg, currency_to_dict, dict, bot)
	else:
		msg_error = bot.send_message(message.chat.id, 'Choose Moscow or SPB or Tash')
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
		msg = bot.send_message(message.chat.id, 'Choose salary or enter yours', reply_markup=markup_3)
		bot.register_next_step_handler(msg, salary_to_dict, dict, bot)
	elif message.text =='USD' : 
		dict['currency'] = message.text
		markup_4 = types.ReplyKeyboardMarkup(resize_keyboard=True)
		btn_salary_USD_1 = types.KeyboardButton("1'000")
		btn_salary_USD_2 = types.KeyboardButton("1'500")
		btn_salary_USD_3 = types.KeyboardButton("2'000")
		btn_salary_USD_4 = types.KeyboardButton("3'000")
		markup_4.add(btn_salary_USD_1, btn_salary_USD_2, btn_salary_USD_3, btn_salary_USD_4)
		msg = bot.send_message(message.chat.id, 'Choose salary or enter yours', reply_markup=markup_4)
		bot.register_next_step_handler(msg, salary_to_dict, dict, bot)
	else :
		msg_error = bot.send_message(message.chat.id, 'Invalid currency')
		bot.register_next_step_handler(msg_error, currency_to_dict,dict, bot)	
		

def salary_to_dict(message, dict, bot):
	dict['salary'] = re.sub("[^0-9]", "", message.text)
	markup_5 = types.ReplyKeyboardMarkup(resize_keyboard=True)
	btn_per_page_1 = types.KeyboardButton(5)
	btn_per_page_2 = types.KeyboardButton(10)
	btn_per_page_3 = types.KeyboardButton(15)
	btn_per_page_4 = types.KeyboardButton(20)
	markup_5.add(btn_per_page_1, btn_per_page_2, btn_per_page_3, btn_per_page_4)
	msg = bot.send_message(message.chat.id, 'Choose ammount of vacancies or enter yours', reply_markup=markup_5)
	bot.register_next_step_handler(msg, per_page_to_dict, dict, bot)

def per_page_to_dict(message, dict, bot):
	dict['per_page'] = message.text
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	btn_finish = types.KeyboardButton('finish')
	markup.add(btn_finish)
	msg = bot.send_message(message.chat.id, '<u>finish</u> to end', reply_markup=markup, parse_mode='html')
	bot.register_next_step_handler(msg, msg_handler.if_finish, dict, bot)
