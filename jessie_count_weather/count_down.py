#!/usr/bin/python
#!/usr/bin/env

import urllib2, json, os
import RPi.GPIO as GPIO

import datetime
from time import strftime


# ---- ws2812 stuff ----
import time
from neopixel import *

# LED strip configuration:
LED_COUNT = 8 # Number of LED pixels.
LED_PIN = 12 # GPIO pin connected to the pixels (must support PWM!) 
LED_FREQ_HZ = 800000 # LED signal frequency in hertz (usually 800khz)
LED_DMA = 5 # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 127 # Set to 0 for darkest and 255 for brightest
#LED_BRIGHTNESS = 255 # Set to 0 for darkest and 255 for brightest
LED_INVERT = False # True to invert the signal (when using NPN transistor level shift)

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
# Intialize the library (must be called once before other functions).
strip.begin()
# ---- ws2812 stuff ----


# ---- Screen stuff ----

import Adafruit_SSD1306
import Image
import ImageDraw
import ImageFont

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
#font = ImageFont.load_default()
#font = ImageFont.truetype('Minecraftia-Regular.ttf', 12)
font = ImageFont.truetype('keep.ttf', 14)
# ---- Screen stuff ----

#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(shutdownPin, GPIO.IN)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def buttonStateChanged(pin):

    if not (GPIO.input(pin)):

        xmas = datetime.datetime(2016,12,25)
        now = datetime.datetime.now()
        take = xmas - now
        day = take.days * 86400
        print "%r" % take.days
       
        draw.text((0, 0), "Days till xmas" ,font=font, fill=255)
        draw.text((0, 15), "%r"  % take.days,font=font, fill=255)
#        draw.text((0, 15), "%sC" % temp_c, font=font, fill=255)
#        draw.text((0, 30), "Feels like" ,font=font, fill=255)
#        draw.text((0, 45), "%sC" % feels, font=font, fill=255)

        # Display image.
        disp.image(image)
        disp.display()

        strip.setPixelColorRGB(0,255,0,0) # Red    
        strip.show()
        strip.setPixelColorRGB(1,0,255,0) # Green    
        strip.show()
        strip.setPixelColorRGB(2,255,0,0) # Red    
        strip.show()
        strip.setPixelColorRGB(3,0,255,0) # Green    
        strip.show()
        strip.setPixelColorRGB(4,255,0,0) # Red    
        strip.show()
        strip.setPixelColorRGB(5,0,255,0) # Green    
        strip.show()
        strip.setPixelColorRGB(6,255,0,0) # Red    
        strip.show()
        strip.setPixelColorRGB(7,0,255,0) # Green    
        strip.show()

        time.sleep(10) # delays for 5 seconds
 
        os.system("sudo python jessie_weather_screen.py")

GPIO.add_event_detect(17, GPIO.BOTH, callback=buttonStateChanged)
 
while True:
     # sleep to reduce unnecessary CPU usage
    time.sleep(5)
                                 
