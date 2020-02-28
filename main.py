from time import sleep
from pynput.keyboard import Key, Controller
import configparser


def main(key_Type, repetition, period, waitingTime):

	keyboard = Controller()
	
	# Waiting period before starting
	waiting = divmod(waitingTime, 5)

	# Every 10 secs 
	for i in range(waiting[0]):
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

	# Load the parameters
	config = configparser.ConfigParser()
	config.read('config.ini')

	key_Type = config['params']['key_Type']
	repetition = int(config['params']['repetition'])
	period = int(config['params']['period'])
	waitingTime = int(config['params']['waitingTime'])

	main(key_Type, repetition, period, waitingTime)