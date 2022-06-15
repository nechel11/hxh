import telebot
from telebot import types
import hh_api
from utils import utils_error, utils_to_dict, utils_messages
from db import BotDB
import db

bot = telebot.TeleBot('5432709533:AAF5jAjDJNbZsE2LtsGO7qwd0dwPvuTThKA')



@bot.message_handler(commands=['start'])
def start(message):
	
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	btn_next = types.KeyboardButton('Поехали!')
	markup.add(btn_next)
	bot.send_message(message.chat.id, 
 		f"Привет, <b>{message.from_user.first_name}</b>.",
 		reply_markup=markup, parse_mode='html')


@bot.message_handler(content_types=['text'])
def get_user_text(message):
	dict = {'page' : 0}
	if message.text == 'Поехали!':
		utils_messages.if_start(message, dict, bot)
	else :
		bot.send_message(message.chat.id, 'пишешь что-то непонятное...')


bot.polling(non_stop=True)