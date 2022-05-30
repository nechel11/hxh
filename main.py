import requests
import json
import time


def get_package(URL, page = 0):

	params = {
		'text' : 'NAME:Python',
		'area' : 1,
		'page' : page,
		'per_page' : 10,
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
	lst = []
	for k in data['items']:
		print(k['name'])
		a = k['employer']
		print(a['name'])
		if k['address'] != None:
			print(k['address']['street'])
			if k['address']['metro'] != None:
				if k['address']['metro']['station_name'] != None:
					print(k['address']['metro']['station_name'])
				if k['address']['metro']['line_name'] != None:
					print(k['address']['metro']['line_name'])
		else :
			print("Адрес не указан")
	
		salary_start = k['salary']
		if salary_start != None:
			print("З\п от : ", salary_start['from'], "до",
				salary_start['to'], "валюта", salary_start['currency'])
		else :
			print("З\п не указана")
		snip = k['snippet']
		print("Requirements :",snip['requirement'])
		print("Responsibility :", snip['responsibility'])
		print(k['schedule']['name'])
		print(k['alternate_url'])
		print("_______________")


if __name__ == "__main__":

	URL = "https://api.hh.ru/vacancies/"
	get_package(URL)
	time.sleep(0.5)