import telebot
import random

access_token = "377231647:AAGdE6s4jc4QZtzmungq5KLdAvyPKSNWerU"
bot = telebot.TeleBot(access_token)

@bot.message_handler(content_types=['text'])
def anon(message):
	resp = ''
	if message.text[-2:] == 'да' or message.text[-2:] == 'Да' or message.text[-2:] == 'ДА' or message.text[-2:] == 'дА':
		resp = 'пакет говна'
	elif message.text[-3:] == 'дыа' or message.text[-3:] == 'Дыа':
		resp = 'пакет говныа'
	elif message.text[-3:] == 'нет' :
		resp = 'говна пакет'
	elif message.text[-3:] == 'нетик' :
		resp = 'говна пакетик'
	elif message.text[-3:] == 'нит':
		resp = 'гавна пакит'
	elif message.text[-2:] == 'da':
		resp = 'paket govna'
	elif message.text[-4:] == 'niet' :
		resp = 'govna pakiet'
	elif message.text[-4:] == 'nyet':
		resp = 'govna pakyet'
	elif message.text[-3:] == 'net' :
		resp = 'govna paket'
	elif message.text == 'с новым годом' :
		resp = 'и тебя, пидор'
	elif message.text == 'пидора ответ' :
		resp = '(сладкого)'
	elif message.text == 'приветики' :
		resp = 'пукни в пакетики'
	elif message.text[:2] == 'да' and not message.text == 'да':
		resp = message.text
		resp = resp.replace('да','пакет говна')
	elif message.text[:2] == 'Да' and not message.text == 'Да':
		resp = message.text
		resp = resp.replace('Да','пакет говна')
	elif message.text == 'пидор' or message.text == 'Пидор':
		resp = 'сладкий' 
	bot.reply_to(message, resp, parse_mode = 'HTML')

if __name__ == '__main__':
    bot.polling(none_stop=True)