# shutdown/reboot(/power on) Raspberry Pi with pushbutton
# Button connected to pin 15
# LED connected to pin 16

import RPi.GPIO as GPIO
from subprocess import call
import time

# ---- ws2812 stuff ----
import time
from neopixel import *

#shutdownPin = 15 

import urllib2, json
import Adafruit_SSD1306
import Image
import ImageDraw
import ImageFont

# LED strip configuration:
LED_COUNT = 8 # Number of LED pixels.
LED_PIN = 12 # GPIO pin connected to the pixels (must support PWM!) 
LED_FREQ_HZ = 800000 # LED signal frequency in hertz (usually 800khz)
LED_DMA = 5 # DMA channel to use for generating signal (try 5)
#LED_BRIGHTNESS = 255 # Set to 0 for darkest and 255 for brightest
LED_BRIGHTNESS = 127 # Set to 0 for darkest and 255 for brightest
LED_INVERT = False # True to invert the signal (when using NPN transistor level shift)

# ---- ws2812 stuff ----

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
#font = ImageFont.load_default()
font = ImageFont.truetype('keep.ttf', 16)

GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.OUT) # Set up pin 16 as an output

def buttonStateChanged(pin):

    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
        # Intialize the library (must be called once before other functions).
    strip.begin()
    ledNumber = 0

    if not (GPIO.input(pin)):
        # Display image.
        draw.text((0, 0),"Shutting down" ,font=font, fill=127)
        disp.image(image)
        disp.display()
        #print"button press"
        GPIO.output(23, True) # Turn on pin 16 (LED)
        while (ledNumber < 8):
            strip.setPixelColorRGB(ledNumber,255,0,0) # Red   
            strip.show()
            ledNumber = ledNumber + 1
            time.sleep(0.2)


        call(['shutdown', '-h', 'now'], shell=False)


GPIO.add_event_detect(22, GPIO.BOTH, callback=buttonStateChanged)

while True:
    # sleep to reduce unnecessary CPU usage
    time.sleep(5)
