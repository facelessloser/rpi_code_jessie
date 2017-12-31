# joyboard
quick and dirty way of mapping key presses to GPIO buttons on raspberry pi

To install you will first need to install PIP then install uinput
1. sudo apt-get install python-pip python-dev build-essential 
2. pip install python-uinput

Next you will need to make it start at boot. First you will need to move the .service file
1. sudo cp joyboard.service /etc/systemd/system/

Next make joyboard.py executable with
1. sudo chmod +x joyboard.py

To make it start at boot run these 2 commands below
1. sudo systemctl start joyboard.service
2. sudo systemctl enable joyboard.service
