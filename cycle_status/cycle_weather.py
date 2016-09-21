#!/usr/bin/python
#!/usr/bin/env

import urllib2, json, os

#email
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders

class basicWeather(object):

    def __init__(self):
        self.chesterWeather = 'http://api.wunderground.com/api/080b28233d8a1a49/geolookup/conditions/q/UK/%s.json' % 'chester'
        self.broughtonWeather = 'http://api.wunderground.com/api/080b28233d8a1a49/geolookup/conditions/q/UK/%s.json' % 'broughton'

    def run(self):
        print """
                  _                           _   _               
                 | |                         | | | |              
   ___ _   _  ___| | ___  __      _____  __ _| |_| |__   ___ _ __ 
  / __| | | |/ __| |/ _ \ \ \ /\ / / _ \/ _` | __| '_ \ / _ \ '__|
 | (__| |_| | (__| |  __/  \ V  V /  __/ (_| | |_| | | |  __/ |   
  \___|\__, |\___|_|\___|   \_/\_/ \___|\__,_|\__|_| |_|\___|_|   
        __/ |                                                     
       |___/                                                      

 version 0.0.2 beta
       """
        self.mail()
#        self.chesterRead()
#        self.broughtonRead()

    def chesterRead(self):
        chesterList = []

        f = urllib2.urlopen(self.chesterWeather)
        json_string = f.read()
        parsed_json = json.loads(json_string)

        chesterTempC = parsed_json['current_observation']['temp_c']
        chesterList.append(chesterTempC) # 0

        chesterFeels = parsed_json['current_observation']['feelslike_c']
        chesterList.append(chesterFeels) # 1

        chesterWeather = parsed_json['current_observation']['weather']
        chesterList.append(chesterWeather) # 2

        chesterWind = parsed_json['current_observation']['wind_mph']
        chesterList.append(chesterWind) # 3

        chesterWindDir = parsed_json['current_observation']['wind_dir']
        chesterList.append(chesterWindDir) #4

        chesterRain = parsed_json['current_observation']['precip_1hr_metric']
        chesterList.append(chesterRain) #5

        f.close()

        return chesterList


    def chesterHeadsOrTailes(self):
        chesterWind = []

        f = urllib2.urlopen(self.chesterWeather)
        json_string = f.read()
        parsed_json = json.loads(json_string)
        wind_dir = parsed_json['current_observation']['wind_dir']
        f.close()

        if wind_dir == "North":
            chesterWind.append("Head wind, Ferry lane")
            chesterWind.append("Side wind, Saltney stright")
        elif wind_dir == "NE":
            chesterWind.append("Head wind, Ferry lane")
            chesterWind.append("Side/Tail wind, Saltney stright")
        elif wind_dir == "East":
            chesterWind.append("Left sidewine, Ferry lane")
            chesterWind.append("Tail wind, Saltney stright")
        elif wind_dir == "SE":
            chesterWind.append("Left hand sidewind, Ferry lane")
            chesterWind.append("Side/Tail wind, Saltney stright")
        elif wind_dir == "South":
            chesterWind.append("Tail wind, Ferry lane")
            chesterWind.append("Side wind, Saltney stright")
        elif wind_dir == "SW":
            chesterWind.append("Tail wind, Ferry lane")
            chesterWind.append("Side/Head wind, Saltney stright")
        elif wind_dir == "West":
            chesterWind.append("Right hand sidewind, Ferry lane")
            chesterWind.append("Head wind, Saltney stright")
        elif wind_dir == "NW":
            chesterWind.append("Right hand sidewind, Ferry lane")
            chesterWind.append("Side/Head wind, Saltney stright")

        return chesterWind

    def broughtonRead(self):
        broughtonList = []

        f = urllib2.urlopen(self.broughtonWeather)
        json_string = f.read()
        parsed_json = json.loads(json_string)

        broughtonTempC = parsed_json['current_observation']['temp_c']
        broughtonList.append(broughtonTempC) # 0

        broughtonFeels = parsed_json['current_observation']['feelslike_c']
        broughtonList.append(broughtonFeels) # 1

        broughtonWeather = parsed_json['current_observation']['weather']
        broughtonList.append(broughtonWeather) # 2

        broughtonWind = parsed_json['current_observation']['wind_mph']
        broughtonList.append(broughtonWind) # 3

        broughtonWindDir = parsed_json['current_observation']['wind_dir']
        broughtonList.append(broughtonWindDir) # 4

        broughtonRain = parsed_json['current_observation']['precip_1hr_metric']
        broughtonList.append(broughtonRain) # 5

        f.close()

        return broughtonList


    def broughtonHeadsOrTailes(self):

        f = urllib2.urlopen(self.broughtonWeather)
        json_string = f.read()
        parsed_json = json.loads(json_string)
        wind_dir = parsed_json['current_observation']['wind_dir']
        f.close()

        broughtonWind = []

        if wind_dir == "North":
            broughtonWind.append("Side wind, Saltney stright")
            broughtonWind.append("Tail wind, Ferry lane")
        elif wind_dir == "NE":
            broughtonWind.append("Side/Headwind, Saltney stright")
            broughtonWind.append("Tail wind, Ferry lane")
        elif wind_dir == "East":
            broughtonWind.append("Headwind, Saltney stright")
            broughtonWind.append("Right sidewine, Ferry lane")
        elif wind_dir == "SE":
            broughtonWind.append("Right Side/Headwind, Saltney stright")
            broughtonWind.append("Right hand sidewind, Ferry lane")
        elif wind_dir == "South":
            broughtonWind.append("Side wind, Saltney stright")
            broughtonWind.append("Head wind, Ferry lane")
        elif wind_dir == "SW":
            broughtonWind.append("Side/Tail wind, Saltney stright")
            broughtonWind.append("Head wind, Ferry lane")
        elif wind_dir == "West":
            broughtonWind.append("Tail wind way home, Saltney stright")
            broughtonWind.append("Left hand sidewind, Ferry lane")
        elif wind_dir == "NW":
            broughtonWind.append("Side/Tail wind, Saltney stright")
            broughtonWind.append("Left hand sidewind, Ferry lane")

        return broughtonWind

    def mail(self):

        chesterList = self.chesterRead()
        chesterWind = self.chesterHeadsOrTailes()

        broughtonList = self.broughtonRead()
        broughtonWind = self.broughtonHeadsOrTailes()
#        print chesterWind[0]
#        print chesterList[0]
#        self.ip = ip
        print "Sending email"
        gmail_user = "python.mail.lists"
        gmail_pwd = "readingthescrips"
        to = "facelessloser@gmail.com"
        subject = "Cycling weather"
        text = """
        ----------------------------------
        Weather to work
        ----------------------------------
        Current weather - %s
        Temp - %sC
        Feels like - %sC
        rain this hour - %s Cm
        ----------------------------------
        To work wind
        ----------------------------------
        wind - %s Mph
        wind direction - %s
        ----------------------------------
        %s 
        %s
        ----------------------------------
        Weather home from work
        ----------------------------------
        Current weather - %s
        Temp - %sC
        Feels like - %sC
        rain this hour - %s Cm
        ----------------------------------
        From work to home wind
        ----------------------------------
        wind - %s Mph
        wind direction - %s
        ----------------------------------
        %s
        %s
        ----------------------------------
        """% (chesterList[2], chesterList[0], chesterList[1], chesterList[5], chesterList[3], chesterList[4], chesterWind[0], chesterWind[1], broughtonList[2], broughtonList[0], broughtonList[1], broughtonList[5], broughtonList[3], broughtonList[4], broughtonWind[0], broughtonWind[1])
        
        msg = MIMEMultipart()
        msg['From'] = gmail_user
        msg['To'] = to
        msg['Subject'] = subject
        msg.attach(MIMEText(text))
        mailServer = smtplib.SMTP("smtp.gmail.com", 587)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(gmail_user, gmail_pwd)
        mailServer.sendmail(gmail_user, to, msg.as_string())
        mailServer.close()


if __name__ == '__main__':
    start = basicWeather()
    start.run()
