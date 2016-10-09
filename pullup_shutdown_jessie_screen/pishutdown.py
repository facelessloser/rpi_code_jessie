#!/usr/bin/python
#!/usr/bin/env

import time, os
import RPi.GPIO as GPIO
from subprocess import call

# ---- Screen stuff ----
import urllib2, json
import Adafruit_SSD1306
import Image
import ImageDraw
import ImageFont

# ---- Screen stuff ----
GPIO.setmode(GPIO.BCM)
# Raspberry Pi pin configuration:
RST = 24

# 128x64 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()
  
# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
 
# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)
#font = ImageFont.load_default() # Default font
font = ImageFont.truetype('Minecraftia-Regular.ttf', 14) # Custom font
# ---- Screen stuff ----

prev_input = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.OUT) # Set up pin 23 as an output

while True:
    input = GPIO.input(22)
    if ((not prev_input) and input):

        GPIO.output(23, True) # Turn on pin 23 (LED)
        draw.text((0, 0),"Shutting", font=font, fill=127)
        draw.text((0, 20),"Down", font=font, fill=127)
        disp.image(image)
        disp.display()
        call(['shutdown', '-h', 'now'], shell=False)

    prev_input = input
    time.sleep(0.05)

