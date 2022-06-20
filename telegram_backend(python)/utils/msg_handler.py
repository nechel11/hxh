from utils import dict_compose, hash_func, errors_checks
import telebot
from telebot import types
import hh_api
from db import BotDB
import bot_msg
from utils import hash_func

BotDB = BotDB()

def if_start(message, dict, bot):
	keyboard = types.ReplyKeyboardRemove()
	msg = bot.send_message(message.chat.id, 'Enter password <u>up to 32 symb</u>', 
		parse_mode='html', reply_markup = keyboard)
	bot.register_next_step_handler(msg, account_set_up, dict, bot)

def account_set_up(message, dict, bot):
	if(not BotDB.user_exists(message.from_user.id)):
		BotDB.add_user(message.from_user.id,message.from_user.username, hash_func.hash_func(message.text))
	msg = bot.send_message(message.chat.id, 'Enter profession <u>(1-2 words)</u>', parse_mode='html')
	bot.register_next_step_handler(msg, dict_compose.proff_to_dict, dict, bot)

def add_to_db(message, lst):
	for k in lst:
		BotDB.add_record(message.from_user.id, k['proff'], k['vacancy'], k['salary_from'], 
		k['salary_to'], k['requir'], k['respons'], k['URL'], k['company'], k['schedule'], 
		k['vacancy_id'], k['adress'], k['currency'])
		

def if_finish(message, dict, bot):
	if (errors_checks.dict_cheq(dict, message, bot)):
			try :
				lst = hh_api.get_package(dict)
			except Exception as e:
				bot.send_message(message.chat.id, f'Smth went wrong... Try again in 10 mis. Then contact author')
				errors_checks.to_loggs(f"Command = finish. Error w/ teleg + api connect. User = {message.from_user.id}. Nick = {message.from_user.username}")
				errors_checks.to_loggs(e)
			if not lst:
				errors_checks.error_handler(message, dict, bot)
			markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
			btn_more = types.KeyboardButton('More')
			markup.add(btn_more)
			add_to_db(message, lst)
			errors_checks.to_loggs(f"Comand = finish. User = {message.from_user.id}. Nick = {message.from_user.username}")
			errors_checks.to_loggs(str(dict))
			html = bot_msg.print_msg(message, BotDB, dict.get('per_page'))
			for k in html[::-1]:
				bot.send_message(message.chat.id, k , parse_mode='html', disable_web_page_preview=True, reply_markup=markup)
			msg = bot.send_message(message.chat.id, '<u>More</u> for new vacancies', reply_markup=markup, parse_mode='html')
			bot.register_next_step_handler(msg, if_more, dict, bot)
	else : 
		bot.send_message(message.chat.id, 'Try again <u> /start </u>' , parse_mode='html')


def if_more(message, dict, bot):
	dict['page'] += 1
	if (errors_checks.dict_cheq(dict, message, bot)):
		try :
			lst = hh_api.get_package(dict)
		except Exception as e:
			bot.send_message(message.chat.id, 'Smth went wrong. If your input is right contact author')
			errors_checks.to_loggs(f"Command = more. Error w/ teleg + api connect. User = {message.from_user.id}. Nick = {message.from_user.username}")
			errors_checks.to_loggs(e)
		if not lst:
			errors_checks.error_handler(message, dict, bot)
		add_to_db(message, lst)
		errors_checks.to_loggs(f"Comand = more. User = {message.from_user.id}. Nick = {message.from_user.username}")
		errors_checks.to_loggs(str(dict))
		html = bot_msg.print_msg(message, BotDB, dict.get('per_page'))
		for k in html[::-1]:
			bot.send_message(message.chat.id, k , parse_mode='html', disable_web_page_preview=True)
		msg = bot.send_message(message.chat.id, ' <u>More</u> for new vacancies', parse_mode='html')
		bot.register_next_step_handler(msg, if_more, dict, bot)	
	else : 
		bot.send_message(message.chat.id, 'Try again <u> /start </u>' , parse_mode='html')	
	