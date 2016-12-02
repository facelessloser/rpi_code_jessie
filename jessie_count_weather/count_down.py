#!/usr/bin/python
#!/usr/bin/env

import urllib2, json, os
import RPi.GPIO as GPIO

import datetime
from time import strftime

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def buttonStateChanged(pin):

    if not (GPIO.input(pin)):

        os.system("sudo python xmas_count.py")

GPIO.add_event_detect(17, GPIO.BOTH, callback=buttonStateChanged)
 
while True:
     # sleep to reduce unnecessary CPU usage
    time.sleep(5)
