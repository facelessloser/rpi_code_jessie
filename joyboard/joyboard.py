""" rpi-gpio-kbrd.py by Chris Swan 9 Aug 2012
GPIO Keyboard driver for Raspberry Pi for use with 80s 5 switch joysticks
*** This did not work with AdvMAME - failed attempt - may be useful for another project
based on python-uinput/examples/keyboard.py by tuomasjjrasanen
https://github.com/tuomasjjrasanen/python-uinput/blob/master/examples/keyboard.py
requires uinput kernel module (sudo modprobe uinput)
requires python-uinput (git clone https://github.com/tuomasjjrasanen/python-uinput)
requires (from http://pypi.python.org/pypi/RPi.GPIO/0.3.1a)
for detailed usage see http://blog.thestateofme.com/2012/08/10/raspberry-pi-gpio-joystick/
"""
#makes sure that the system uinput module is running
from os import system
from subprocess import call
system("modprobe uinput")

import uinput
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)

events = (uinput.KEY_UP, uinput.KEY_DOWN, uinput.KEY_LEFT, uinput.KEY_RIGHT, uinput.KEY_ENTER, uinput.KEY_BACKSPACE, uinput.KEY_P, uinput.KEY_Y)

device = uinput.Device(events)

fire = False
b = False
x= False
up = False
down = False
left = False
right = False

while True:
  if (not fire) and (not GPIO.input(14)):  # Fire button pressed
    fire = True
#    device.emit(uinput.KEY_LEFTCTRL, 1) # Press Left Ctrl key
    device.emit(uinput.KEY_ENTER, 1) # Press Left Ctrl key

  if fire and GPIO.input(14):  # Fire button released
    fire = False
#    device.emit(uinput.KEY_LEFTCTRL, 0) # Release Left Ctrl key
    device.emit(uinput.KEY_ENTER, 0) # Release Left Ctrl key

  if (not b) and (not GPIO.input(15)):  # Fire button pressed
    b = True
#    device.emit(uinput.KEY_LEFTCTRL, 1) # Press Left Ctrl key
    device.emit(uinput.KEY_BACKSPACE, 1) # Press Left Ctrl key

  if b and GPIO.input(15):  # Fire button released
    b = False
#    device.emit(uinput.KEY_LEFTCTRL, 0) # Release Left Ctrl key
    device.emit(uinput.KEY_BACKSPACE, 0) # Release Left Ctrl key
    
  if (not x) and (not GPIO.input(20)):  # Fire button pressed
    x = True
#    device.emit(uinput.KEY_LEFTCTRL, 1) # Press Left Ctrl key
#    device.emit(uinput.KEY_BACKSPACE, 1) # Press Left Ctrl key
#    call(["cd", "~/", "-h", "now" ])
#    call(["exit"])
#    call(['ls'], shell=False)
#    call(['ls'], shell=True)
#    device.emit(uinput.KEY_P, 1) # Press Left Ctrl key
#    device.emit(uinput.KEY_Y, 1) # Press Left Ctrl key

  if x and GPIO.input(20):  # Fire button released
    b = False
#    device.emit(uinput.KEY_LEFTCTRL, 0) # Release Left Ctrl key
#    device.emit(uinput.KEY_BACKSPACE, 0) # Release Left Ctrl key
#    device.emit(uinput.KEY_P, 0) # Press Left Ctrl key
#    device.emit(uinput.KEY_Y, 0) # Press Left Ctrl key

  if (not up) and (not GPIO.input(16)):  # Up button pressed
    up = True
    device.emit(uinput.KEY_UP, 1) # Press Up key

  if up and GPIO.input(16):  # Up button released
    up = False
    device.emit(uinput.KEY_UP, 0) # Release Up key

  if (not down) and (not GPIO.input(26)):  # Down button pressed
    down = True
    device.emit(uinput.KEY_DOWN, 1) # Press Down key

  if down and GPIO.input(26):  # Down button released
    down = False
    device.emit(uinput.KEY_DOWN, 0) # Release Down key

  if (not left) and (not GPIO.input(4)):  # Left button pressed
    left = True
    device.emit(uinput.KEY_LEFT, 1) # Press Left key

  if left and GPIO.input(4):  # Left button released
    left = False
    device.emit(uinput.KEY_LEFT, 0) # Release Left key

  if (not right) and (not GPIO.input(19)):  # Right button pressed
    right = True
    device.emit(uinput.KEY_RIGHT, 1) # Press Right key

  if right and GPIO.input(19):  # Right button released
    right = False
    device.emit(uinput.KEY_RIGHT, 0) # Release Right key

  time.sleep(.04)
