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
		if k['address']['raw'] != None:
			st = st + ". " + k['address']['raw']
	else :
		st ="Адрес не указан"
	return st
	
def add_salary(k):
	dct={}
	salary_start = k['salary']
	if salary_start != None:
		if salary_start['from'] == None:
			dct['salary_from'] = '0'
		else:	
			dct['salary_from'] = str(salary_start['from'])
		if salary_start['to'] == None:
			dct['salary_to'] = '0'
		else:	
			dct['salary_to'] = str(salary_start['to'])
		dct['currency'] = salary_start['currency']
		return dct
	return None
	

def add_req(k):
	dct = {}
	snip_req = str(f"{k['snippet']['requirement']}")
	snip_res = str(f"{k['snippet']['responsibility']}	")
	snip_req = snip_req.replace('<highlighttext>',"")
	snip_req = snip_req.replace('</highlighttext>',"")
	snip_res = snip_res.replace('<highlighttext>',"")
	snip_res = snip_res.replace('</highlighttext>',"")
	dct['requir'] = snip_req
	dct['respons'] = snip_res
	dct['URL'] = k['alternate_url']
	return dct


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
		dct = {}
		dct['proff'] = dict.get('text')
		dct['vacancy'] = k['name']
		dct['vacancy_id'] = k['id']
		dct['company'] = k['employer']['name']
		dct['schedule'] = k['schedule']['name']
		dct['adress'] = add_adress(k)
		sal = add_salary(k)
		if sal != None:
			dct['salary_from'] = sal.get('salary_from')
			dct['salary_to'] = sal.get('salary_to')
			dct['currency'] = sal.get('currency')
		else:
			dct['salary_from'] = None
			dct['salary_to'] = None
			dct['currency'] = None
		inf = add_req(k)
		dct['requir'] = inf.get('requir')
		dct['respons'] = inf.get('respons')
		dct['URL'] = inf.get('URL')
		lst.append(dct)
	return lst

# if __name__ == '__main__':
# 	dict = {}
# 	dict['text'] = 'python'
# 	dict['city'] = 1
# 	dict['page'] = 0
# 	dict['per_page'] = 2
# 	dict['salary'] = 80000
# 	dict['currency'] = 'RUR'
# 	qwe = get_package(dict)
# 	for k in qwe:
# 		print (k)