from copy import copy
import re
from utils import errors_checks

def make_html(template, settings): #making html view for telegr
	for key, value in settings.items():
		tmp = '{' + key + '}'
		replace = str(value)
		template = re.sub(tmp, replace, template)
	return template


def print_msg(message, BotDB, per_page): # print msg in teleg
	lst = ['id' ,'proff', 'vacancy','salary_from', 'salary_to', 'requir','respons','url', 'company', 'schedule', 'vacancy_id', 'adress', 'currency', 'telegram_id']
	id = BotDB.get_user_id(message.from_user.id)
	html = []
	res = BotDB.get_all_records(str(id), per_page)
	print(res)
	message_to_print= []
	for i in res:
		dct = {}
		dct ={lst[j] : i[j] for j in range(0,len(lst))}
		html.append(dct)
	try :
		with open ('bot_msg.html') as f:
			template = f.read()
	except Exception as e:
		errors_checks.to_loggs(f"User = {message.from_user.id}. Nick = {message.from_user.first_name}")
		errors_checks.to_loggs(e)
	copy_template = copy(template)
	for i in html:
		tmp = make_html(copy_template, i)
		message_to_print.append(tmp)
	return message_to_print