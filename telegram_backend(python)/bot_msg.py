from copy import copy
import re

def make_html(template, settings):
	for key, value in settings.items():
		tmp = '{' + key + '}'
		replace = str(value)
		template = re.sub(tmp, replace, template)
	return template


def print_msg(message, BotDB, per_page):
	lst = ['id' ,'proff', 'vacancy','salary_from', 'salary_to', 'requir','respons','url', 'company', 'schedule', 'vacancy_id', 'adress', 'currency', 'telegram_id']
	id = BotDB.get_user_id(message.from_user.id)
	html = []
	res = BotDB.get_all_records(str(id), per_page)
	message_to_print= []
	for i in res:
		dct = {}
		dct ={lst[j] : i[j] for j in range(0,len(lst))}
		html.append(dct)
	#print(html)	
	with open ('bot_msg.html') as f:
		template = f.read()
	copy_template = copy(template)
	for i in html:
		tmp = make_html(copy_template, i)
		message_to_print.append(tmp)
	return message_to_print