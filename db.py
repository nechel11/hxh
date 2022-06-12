import psycopg2

# conn = psycopg2.connect(host='127.0.0.1', port=5432, dbname='hxh', user = 'zafar', password='12344321')
# cursor = conn.cursor()
# cursor.execute("INSERT INTO users(telegram_id) VALUES (%s)", ("2000",))
# conn.commit()

class BotDB:
	def __init__(self, db_file) -> None:
		self.conn = psycopg2.connect(host='127.0.0.1', port=5432, dbname='hxh', user = 'zafar', password='12344321')
		self.cursor = self.conn.cursor()

	def user_exists(self, telegram_id):
		self.cursor.execute("SELECT * FROM users WHERE telegram_id =(%s)", (str(telegram_id),))
		return bool(len(self.cursor.fetchall()))

	def get_user_id(self, telegram_id):
		self.cursor.execute("SELECT user_id FROM users WHERE telegram_id=(%s)", (str(telegram_id),))
		return self.cursor.fetchone()[0]

	def add_user(self, telegram_id):
		self.cursor.execute("INSERT INTO users(telegram_id) VALUES (%s)", (str(telegram_id),))
		return self.conn.commit()

	def add_record(self, telegram_id, proff, vacancy):
		self.cursor.execute("INSERT INTO records(telegram_id, proff, vanacy) VALUES (%s, %s, %s)",
		(self.get_user_id(telegram_id), proff, vacancy))
		return self.conn.commit()
	
	def get_records(self, telegram_id):
		self.cursor.execute("SELECT * FROM records WHERE telegram_id (%s)", (telegram_id))
		return self.cursor.fetchall()

	def close(self):
		self.conn.close()