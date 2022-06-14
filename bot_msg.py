import re

def make_html(template, settings):
	for key, value in settings.items():
		tmp = '{' + key + '}'
		replace = str(value)
		template = re.sub(tmp, replace, template)
	return template

def print_msg(message, BotDB):
	lst = ['proff', 'vacancy','company', 'schedule', 'adress', 'salary_from', 'salary_to', 'currency','respons','requir','url']
	id = BotDB.get_user_id(message.from_user.id)
	dct = {}
	for k in lst:
		dct[k] = BotDB.get_one_record(str(id), k)
	with open ('bot_msg.html') as f:
		template = f.read()
	html = make_html(template, dct)
	return html