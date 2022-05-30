import telebot

bot = telebot.TeleBot('5432709533:AAF5jAjDJNbZsE2LtsGO7qwd0dwPvuTThKA')

@bot.message_handler(commands=['start'])
def start(message):
	mess = f'Привет, <b>{message.from_user.first_name}</b>'
	bot.send_message(message.chat.id, mess, parse_mode='html')
bot.polling(none_stop=True)