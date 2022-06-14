import re

def make_html(template, settings):
	for key, value in settings.items():
		tmp = '{' + key + '}'
		replace = str(value)
		template = re.sub(tmp, replace, template)
	return template

def print_msg(message, BotDB):
	dct = {}
	dct['telegram_id'] = BotDB.get_user_id(message.from_user.id)
	dct['proff'] = BotDB.get_one_record(str(dct.get('telegram_id')), 'proff')
	dct['vacancy'] = BotDB.get_one_record(str(dct.get('telegram_id')), 'vacancy')
	dct['company'] = BotDB.get_one_record(str(dct.get('telegram_id')), 'company')
	dct['schedule'] = BotDB.get_one_record(str(dct.get('telegram_id')), 'schedule')
	dct['adress'] = BotDB.get_one_record(str(dct.get('telegram_id')), 'adress')
	dct['salary_from'] = BotDB.get_one_record(str(dct.get('telegram_id')), 'salary_from')
	dct['salary_to'] = BotDB.get_one_record(str(dct.get('telegram_id')), 'salary_to')
	dct['currency'] = BotDB.get_one_record(str(dct.get('telegram_id')), 'currency')
	dct['respons'] = BotDB.get_one_record(str(dct.get('telegram_id')), 'respons')
	dct['requir'] = BotDB.get_one_record(str(dct.get('telegram_id')), 'requir')
	dct['url'] = BotDB.get_one_record(str(dct.get('telegram_id')), 'url')
	

	with open ('bot_msg.html') as f:
		template = f.read()
	html = make_html(template, dct)
	return html