# shutdown/reboot(/power on) Raspberry Pi with pushbutton
# Button connected to pin 15
# LED connected to pin 16

import RPi.GPIO as GPIO
from subprocess import call
import time

#shutdownPin = 15 


GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def buttonStateChanged(pin):

    if not (GPIO.input(pin)):
        call(['shutdown', '-h', 'now'], shell=False)

GPIO.add_event_detect(40, GPIO.BOTH, callback=buttonStateChanged)

while True:
    # sleep to reduce unnecessary CPU usage
    time.sleep(5)
