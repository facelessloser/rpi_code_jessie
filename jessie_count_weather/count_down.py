import RPi.GPIO as GPIO
from subprocess import call
import time, os


GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def buttonStateChanged(pin):

    if not (GPIO.input(pin)):
        os.system("sudo python xmas_count.py")

GPIO.add_event_detect(11, GPIO.BOTH, callback=buttonStateChanged)

while True:
    # sleep to reduce unnecessary CPU usage
    time.sleep(5)
