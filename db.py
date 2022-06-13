import psycopg2


class BotDB:
	def __init__(self) -> None:
		self.conn = psycopg2.connect(host='127.0.0.1', port=5432, dbname='hxh', user = 'zafar', password='12344321')
		self.cursor = self.conn.cursor()

	def user_exists(self, telegram_id):
		self.cursor.execute("SELECT * FROM users WHERE telegram_id =(%s)", (str(telegram_id),))
		return bool(len(self.cursor.fetchall()))

	def get_user_id(self, telegram_id):
		self.cursor.execute("SELECT fk_telegram_id FROM records WHERE fk_telegram_id=(%s)", (str(telegram_id),))
		return self.cursor.fetchone()[0]

	def add_user(self, telegram_id):
		self.cursor.execute("INSERT INTO users(telegram_id) VALUES (%s)", (str(telegram_id),))
		return self.conn.commit()

	def add_record(self, telegram_id, proff, vacancy, salary_from, salary_to, requir, respons, url, company, schedule, vacancy_id, adress):
		self.cursor.execute("INSERT INTO records(fk_telegram_id, proff, vacancy,\
		salary_from, salary_to, requir, respons, url, company, schedule, \
		vacancy_id, adress)  VALUES \
		(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
		(str(telegram_id), proff, vacancy, salary_from, salary_to, requir, 
		respons, url, company, schedule, vacancy_id, adress,))
		return self.conn.commit()
	
	def get_records(self, telegram_id):
		self.cursor.execute("SELECT * FROM records WHERE fk_telegram_id (%s)", (telegram_id))
		return self.cursor.fetchall()

	def close(self):
		self.conn.close()