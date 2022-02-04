import telebot

import json
import requests

from datetime import date

today = date.today()

alldata = 0

holiday = []

bot = telebot.TeleBot("5235847357:AAEbI9316MuosID0sapxEJ1_fE05MX3PcuA")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)
	# dates and time
	import datetime

	now = datetime.datetime.now()
	year = '{:02d}'.format(now.year)
	month = '{:02d}'.format(now.month)
	day = '{:02d}'.format(now.day)
	day_month_year_start = '{}-{}-{}'.format(year, month, day)

	beginning_date=(day_month_year_start)
	print (beginning_date)


	headers = {
		'Authorization': 'Bearer 53b42f0b-8ff2-4183-9f04-d407211c8620',
	}

	timeresponse = f'https://app.timetastic.co.uk/api/holidays?Start={beginning_date}&End={beginning_date}'

	print(timeresponse)

	response= requests.get(timeresponse, headers=headers)
	json_data = json.loads(response.text)


	usernames = []
	for person in json_data['holidays']:
		usernames.append(person["userName"])

	print(f'{usernames} has a holiday today')






#data_new = json_data['holidays'][0]["userName"]
	#print(data_new)


	bot.reply_to(message,f'{usernames} has a holiday today')


bot.infinity_polling()