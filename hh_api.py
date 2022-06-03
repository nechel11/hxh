import requests
import json
import time


def get_package(dict):

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
	lst = []
	for k in data['items']:
		lst.append(str(f"{k['name']} | {k['employer']['name']} | {k['schedule']['name']}"))
		if k['address'] != None:
			if (k['address']['street']) != None:
				lst.append(k['address']['street'])
			if k['address']['metro'] != None:
				if k['address']['metro']['station_name'] != None:
					lst.append(k['address']['metro']['station_name'])
				if k['address']['metro']['line_name'] != None:
					lst.append(k['address']['metro']['line_name'])
		else :
			lst.append("Адрес не указан")
		salary_start = k['salary']
		if salary_start != None:
			salary_from = salary_start['from']
			salary_to = salary_start['to']
			salary_currency = salary_start['currency']
			lst.append(f"З\п от  <u>{salary_from}</u> до <u>{salary_to}</u> валюта {salary_currency}")
		else :
			lst.append("З\п не указана")
		snip_req = str(f"<b>Requirements :</b> {k['snippet']['requirement']}\n")
		snip_res = str(f"<b>Responsibility :</b> {k['snippet']['responsibility']}")
		snip_req = snip_req.replace('<highlighttext>',"")
		snip_req = snip_req.replace('</highlighttext>',"")
		snip_res = snip_res.replace('<highlighttext>',"")
		snip_res = snip_res.replace('</highlighttext>',"")

		lst.append(snip_res + snip_req)
		lst.append(f"<a href='{k['alternate_url']}'> ссылка на хх</a>")
		lst.append("__________________")
		
	return lst