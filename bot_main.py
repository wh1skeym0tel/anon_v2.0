import telebot
import random

access_token = "377231647:AAGdE6s4jc4QZtzmungq5KLdAvyPKSNWerU"
bot = telebot.TeleBot(access_token)

@bot.message_handler(content_types=['text'])
def anon(message):
	resp = ''
	if message.text[-2:] == 'да' or message.text[-2:] == 'Да' or message.text[-2:] == 'ДА' or message.text[-2:] == 'дА':
		resp = 'пакет говна'
		bot.reply_to(message, resp, parse_mode = 'HTML')
	elif message.text[-3:] == 'дыа' or message.text[-3:] == 'Дыа':
		resp = 'пакет говныа'
		bot.reply_to(message, resp, parse_mode = 'HTML')
	elif message.text[-3:] == 'нет' :
		resp = 'говна пакет'
		bot.reply_to(message, resp, parse_mode = 'HTML')
	elif message.text[-3:] == 'нетик' :
		resp = 'говна пакетик'
		bot.reply_to(message, resp, parse_mode = 'HTML')
	elif message.text[-3:] == 'нит':
		resp = 'гавна пакит'
		bot.reply_to(message, resp, parse_mode = 'HTML')
	elif message.text[-2:] == 'da':
		resp = 'paket govna'
		bot.reply_to(message, resp, parse_mode = 'HTML')
	elif message.text[-4:] == 'niet' :
		resp = 'govna pakiet'
		bot.reply_to(message, resp, parse_mode = 'HTML')
	elif message.text[-4:] == 'nyet':
		resp = 'govna pakyet'
		bot.reply_to(message, resp, parse_mode = 'HTML')
	elif message.text[-3:] == 'net' :
		resp = 'govna paket'
		bot.reply_to(message, resp, parse_mode = 'HTML')
	elif message.text == 'с новым годом' :
		resp = 'и тебя, пидор'
		bot.reply_to(message, resp, parse_mode = 'HTML')
	elif message.text == 'пидора ответ' :
		resp = '(сладкого)'
		bot.reply_to(message, resp, parse_mode = 'HTML')
	elif message.text == 'приветики' :
		resp = 'пукни в пакетики'
		bot.reply_to(message, resp, parse_mode = 'HTML')
	elif message.text[:2] == 'да' and not message.text == 'да':
		resp = message.text
		resp = resp.replace('да','пакет говна')
		bot.reply_to(message, resp, parse_mode = 'HTML')
	elif message.text[:2] == 'Да' and not message.text == 'Да':
		resp = message.text
		resp = resp.replace('Да','пакет говна')
		bot.reply_to(message, resp, parse_mode = 'HTML')
	elif message.text == 'пидор' or message.text == 'Пидор':
		resp = 'сладкий'
		bot.reply_to(message, resp, parse_mode = 'HTML')
	elif message.text[:3] == 'нет' and not message.text == 'нет':
		resp = message.text
		resp = resp.replace('нет','говна пакет')
		bot.reply_to(message, resp, parse_mode = 'HTML')
	elif message.text[:3] == 'Нет' and not message.text == 'Нет':
		resp = message.text
		resp = resp.replace('Нет','Говна пакет')
		bot.reply_to(message, resp, parse_mode = 'HTML')

if __name__ == '__main__':
    bot.polling(none_stop=True)