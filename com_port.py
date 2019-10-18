from serial import Serial
from subprocess import Popen
from time import sleep

port = None


def open_serial():
	global port

	'''
	#work with bluetooth com port
	Popen(['sudo', 'rfcomm', 'connect', 'hci0', '00:18:E4:35:45:73', '1'])
	sleep(5)
	port = Serial(port='/dev/rfcomm0', baudrate=9600)
	'''

	#simple com port
	port = Serial(port='/dev/ttyUSB0', baudrate=9600)
	
	port.isOpen()


def close_serial():
	global port
	port.close()


def send_to_port(item):
	global port
	port.write(bytes(item, 'utf-8'))
