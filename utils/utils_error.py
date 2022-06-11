
def error_handler(message, dict, bot):
	bot.send_message(message.chat.id, f'что-то пошло не так. проверь данные. \n\
			Профессия -  {dict.get("text")} \n\
			Город - {dict.get("city")} \n\
			Валюта - {dict.get("currency")} \n\
			З\п - {dict.get("currency")} \n\
			per_page - {dict.get("per_page")} \n\
			page - {dict.get("page")} \n\
			если все ок, то пиши @nechel1233 ')

def dict_cheq(dct, message, bot) : # check if dict is filled 
	if ('text' in dct and 'city' in dct and 
		'currency' in dct and 'salary' in dct and
		 'per_page' in dct):
		return True
	else:
		error_handler(message, dct, bot)
		return False
