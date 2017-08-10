import telebot
import random

access_token = "377231647:AAGdE6s4jc4QZtzmungq5KLdAvyPKSNWerU"
bot = telebot.TeleBot(access_token)

@bot.message_handler(content_types=['text'])
def anon(message):
	resp = ''
	if message.text[-2:] == 'да' or message.text[-2:] == 'da' or message.text[-2:] == 'Да':
		resp = answer_yes(random.randint(1,3))
	elif message.text[-3:] == 'нет' or message.text[-3:] == 'Нет' or message.text[-3:] == 'net' or message.text[-4:] == 'niet':
		resp = answer_no(random.randint(1,3))
	elif message.text[-3:] == 'нит':
		resp = 'говна пакит'
	elif message.text[:2] == 'да' and not message.text == 'да':
		resp = message.text
		resp = resp.replace('да','пакет говна')
	elif message.text[:2] == 'Да' and not message.text == 'Да':
		resp = message.text
		resp = resp.replace('Да','пакет говна')
	elif message.text == 'пидор' or message.text == 'Пидор':
		resp = 'сладкий' 
	bot.send_message(message.chat.id, resp, parse_mode = 'HTML')

def answer_yes(varik):
	if varik == 1:
		return 'пизда'
	elif varik == 2:
		return 'пидора слова'
	elif varik == 3:
		return 'манда'

def answer_no(varik):
	if varik == 1:
		return 'пидора ответ'
	elif varik == 2:
		return 'говна пакет'
	elif varik == 3:
		return 'сделай минет'

if __name__ == '__main__':
    bot.polling(none_stop=True)