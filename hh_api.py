import requests
import json
import time


def get_package():

	URL = "https://api.hh.ru/vacancies/"
	page = 0
	params = {
		'text' : 'Python',
		'area' : 1,
		'page' : page,
		'per_page' : 2,
		'salary': 80000,
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
	#print(data)
	lst = []
	for k in data['items']:
		#print(k)
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
		salary_from = salary_start['from']
		salary_to = salary_start['to']
		salary_currency = salary_start['currency']
		if salary_start != None:
			lst.append(f"З\п от  <u>{salary_from}</u> до <u>{salary_to}</u> валюта {salary_currency}")
		else :
			lst.append("З\п не указана")
		snip = k['snippet']
		lst.append(f"<b>Requirements</b> : {snip['requirement']}  \n<b>Responsibility</b> : {snip['responsibility']}")
		#lst.append(f"Responsibility  {snip['responsibility']}")
		#lst.append(k['schedule']['name'])
		lst.append(f"<a href='{k['alternate_url']}'> ссылка на хх</a>")
		lst.append("__________________")
	return lst

lst = get_package()
for k in lst:
	print (k)