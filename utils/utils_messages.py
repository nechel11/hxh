from utils import utils_to_dict

def if_start(message, dict, bot):
	msg = bot.send_message(message.chat.id, 'Укажи профессию <u>(1-2 слова)</u>', parse_mode='html')
	bot.register_next_step_handler(msg, utils_to_dict.proff_to_dict, dict, bot)