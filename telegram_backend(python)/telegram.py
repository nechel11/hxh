import telebot
from telebot import types
from utils import msg_handler, errors_checks
import json

try:
	with open ('../settings') as f:
		template = f.read()
except Exception as e :
	errors_checks.to_loggs('error w/ settings file')
	errors_checks.to_loggs(str(e))
js = json.loads(template)
bot = telebot.TeleBot(js.get('bot'))


@bot.message_handler(commands=['start'])
def start(message):
	
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	btn_next = types.KeyboardButton('Go!')
	markup.add(btn_next)
	bot.send_message(message.chat.id, 
 		f"Welcome, <b>{message.from_user.first_name}</b>.",
 		reply_markup=markup, parse_mode='html')


@bot.message_handler(content_types=['text'])
def get_user_text(message):
	dict = {'page' : 0}
	if message.text == 'Go!':
		msg_handler.if_start(message, dict, bot)
	elif message.text == '/settings' : 
		msg_handler.if_settings(message, dict, bot)
	else :
		bot.send_message(message.chat.id, 'can not understand you...')

bot.polling(non_stop=True)