import sys
from os import path
from time import sleep
from pynput.keyboard import Key, Controller
import configparser


def main(key_Type, repetition, period, waitingTime):

	keyboard = Controller()

	# Waiting period before starting
	waiting = divmod(waitingTime, 5)

	# Every 10 secs 
	for i in range(int(waiting[0])):
		t = i * 5
		print("In waiting mode for: {} sec / {} sec".format(t, waitingTime))
		sleep(waiting[0])
	sleep(waiting[1])

	print("Starting the MRI simulation")

	# Loop
	for i in range(repetition):	
		keyboard.press(key_Type)
		keyboard.release(key_Type)
		sleep(period)
		

if __name__ == '__main__':

	if len(sys.argv) == 1:
		config_file = './config.ini'
	
	elif len(sys.argv) == 2:
		if path.isfile(sys.argv[1]):
			config_file = sys.argv[1]
		else:
			raise IOError("Error: the provided file does not exist")
	else:
		raise IOError("Error: too many input arguments")

	# Load the parameters
	config = configparser.ConfigParser()
	config.read(config_file)

	key_Type = config['params']['key_Type']
	repetition = int(config['params']['repetition'])
	period = int(config['params']['period']) / 1000
	waitingTime = int(config['params']['waitingTime']) / 1000

	main(key_Type, repetition, period, waitingTime)