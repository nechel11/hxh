from utils import utils_to_dict, utils_error
import telebot
from telebot import types
import hh_api
from db import BotDB
import db

def if_start(message, dict, bot):
	
	msg = bot.send_message(message.chat.id, 'Укажи профессию <u>(1-2 слова)</u>', parse_mode='html')
	bot.register_next_step_handler(msg, utils_to_dict.proff_to_dict, dict, bot)


def if_finish(message, dict, bot):
	lst =[]
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


def if_more(message, dict, bot):
	dict['page'] += 1
	if (utils_error.dict_cheq(dict, message, bot)):
		try :
			lst = hh_api.get_package(dict)
		except Exception as e:
			bot.send_message(message.chat.id, 'что-то пошло не так. проверь данные. если все ок, то пиши автору')
		if not lst:
			utils_error.error_handler(message, dict, bot)
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		for k in lst:
			bot.send_message(message.chat.id, k, parse_mode='html', disable_web_page_preview=True, reply_markup=markup)
	else : 
		bot.send_message(message.chat.id, 'Попробуй заново <u> /start </u>' , parse_mode='html')	
	print(dict)	