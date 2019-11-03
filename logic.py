from config import phrase_dict, answer_dict, owm_key, city
from com_port import send_to_port

from datetime import datetime as dt
import random
import pyowm


def answer(cmd):
	for key in phrase_dict:
		if cmd in phrase_dict[key]:
			return eval(key)


def hello():
	return '', random.choice(answer_dict['hello'])


def thank():
	return '', random.choice(answer_dict['you are welcome'])


def date():
	now = dt.now()
	return f"{now.strftime('%A')}, {now.strftime('%d.%m.%Y')}", f"сегодня {now.strftime('%d.%m')}, {now.strftime('%A')}"


def time():
	now = dt.now()
	return f"{now.strftime('%-H:%-M')}", f"сейчас {now.strftime('%-H:%-M')}"


def weather():
	owm = pyowm.OWM(owm_key, language='ru')
	try:
		observation = owm.weather_at_place(city)
		w = observation.get_weather()
		return f"Temperature: {str(w.get_temperature('celsius')['temp'])}ºC\nHumidity: {str(w.get_humidity())}%\nWind: {str(w.get_wind()['speed'])}m/s", f"температура {str(int(w.get_temperature('celsius')['temp']))} градусов цельсия, {str(w.get_detailed_status())}"
	except:
		return '', 'ошибка'


def socket_on():
	try:
		send_to_port('1000')
		return '', random.choice(answer_dict['socket_action_succes'])
	except:
		return '', 'ошибка'


def socket_off():
	try:
		send_to_port('1111')
		return '', random.choice(answer_dict['socket_action_succes'])
	except:
		return '', 'ошибка'
