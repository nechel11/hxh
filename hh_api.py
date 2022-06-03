import requests
import json
import time

def add_adress(k) :
	st = ""
	if k['address'] != None:
		if (k['address']['street']) != None:
			st = k['address']['street']
		if k['address']['metro'] != None:
			if k['address']['metro']['station_name'] != None:
				st = st + ". " + k['address']['metro']['station_name']
			if k['address']['metro']['line_name'] != None:
				st = st + ". " + k['address']['metro']['line_name']
	else :
		st ="Адрес не указан"
	return st
	
def add_salary(k):
	salary_start = k['salary']
	if salary_start != None:
		salary_from = salary_start['from']
		salary_to = salary_start['to']
		salary_currency = salary_start['currency']
		st = (f"З\п от  <u>{salary_from}</u> до <u>{salary_to}</u> валюта {salary_currency}")
	else :
		st = ("З\п не указана")
	return st


def add_req(k):
	snip_req = str(f"<b><u>Requirements :</u></b> {k['snippet']['requirement']}")
	snip_res = str(f"<b><u>Responsibility :</u></b> {k['snippet']['responsibility']}\n")
	snip_req = snip_req.replace('<highlighttext>',"")
	snip_req = snip_req.replace('</highlighttext>',"")
	snip_res = snip_res.replace('<highlighttext>',"")
	snip_res = snip_res.replace('</highlighttext>',"")
	res = (snip_res + snip_req)
	res = res + (f"\n<a href='{k['alternate_url']}'> ссылка на вакансию</a>\n_____________________")
	return res


def get_package(dict):
	lst = []
	URL = "https://api.hh.ru/vacancies/"
	params = {
		'text' : dict.get('text'),
		'area' : dict.get('city'),
		'page' : dict.get('page'),
		'per_page' : dict.get('per_page'),
		'salary': dict.get('salary'),
		'currency' : dict.get('currency')
		#'employment' : 'probation' #full
		#'experience' : 'noExperience' #	"between3And6"
	}

	try:
		request = requests.get(URL, params)
		request.raise_for_status()
	except Exception as e:
		print(e)
	data = request.content.decode()
	data = json.loads(data)
	for k in data['items']:
		lst.append(str(f"{k['name']} | {k['employer']['name']} | {k['schedule']['name']}"))
		lst.append(add_adress(k))
		lst.append(add_salary(k))	
		lst.append(add_req(k))
	return lst

# if __name__ == '__main__':
# 	dict = {}
# 	dict['text'] = 'python'
# 	dict['city'] = 1
# 	dict['page'] = 0
# 	dict['pre_page'] = 5
# 	dict['salary'] = 80000
# 	dict['currency'] = 'RUR'
# 	qwe = get_package(dict)
# 	for k in qwe:
# 		print(k)