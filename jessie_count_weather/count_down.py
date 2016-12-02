# shutdown/reboot(/power on) Raspberry Pi with pushbutton
# Button connected to pin 15
# LED connected to pin 16

import RPi.GPIO as GPIO
from subprocess import call
import time, os

#shutdownPin = 15 


GPIO.setmode(GPIO.BOARD)
#GPIO.setup(shutdownPin, GPIO.IN)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def buttonStateChanged(pin):

    if not (GPIO.input(pin)):
        #print"button press"
        #GPIO.output(16, True) # Turn on pin 16 (LED)
        #print"Shutdown"
        os.system("sudo python xmas_count.py")

GPIO.add_event_detect(17, GPIO.BOTH, callback=buttonStateChanged)

while True:
    # sleep to reduce unnecessary CPU usage
    time.sleep(5)
