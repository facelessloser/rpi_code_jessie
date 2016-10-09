#!/usr/bin/python
#!/usr/bin/env

import time, os
import RPi.GPIO as GPIO
import socket
import fcntl
import struct
# ---- ws2812 stuff ----
import time
from neopixel import *

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

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
# Intialize the library (must be called once before other functions).
strip.begin()
# ---- ws2812 stuff ----

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
#font = ImageFont.load_default()
font = ImageFont.truetype('Minecraftia-Regular.ttf', 14)
# ---- Screen stuff ----

hostname = "google.com" #example
#hostname = "secure.ubi.com/login/" #example

response = os.system("ping -c 1 " + hostname)

prev_input = 1

ledNumber = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(22,GPIO.IN, GPIO.PUD_UP)
GPIO.setup(23, GPIO.OUT) # Set up pin 16 as an output

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
        )[20:24])


print get_ip_address('wlan0')
ip_address =  get_ip_address('wlan0')
# Display image.
draw.text((0, 0),"%s" % ip_address ,font=font, fill=127)

#and then check the response...
if response == 0:
    print hostname, 'is up!'
    draw.text((0, 20),"Online", font=font, fill=127)
    while (ledNumber < 8):
        strip.setPixelColorRGB(ledNumber,0,255,0) # Green   
        strip.show()
        ledNumber = ledNumber + 1
else:
    print hostname, 'is down!'
    draw.text((0, 20),"Offline", font=font, fill=127)
    while (ledNumber < 8):
        strip.setPixelColorRGB(ledNumber,255,0,0) # Red
        strip.show()
        ledNumber = ledNumber + 1

disp.image(image)
disp.display()
