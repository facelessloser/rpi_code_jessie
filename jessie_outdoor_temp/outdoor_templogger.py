#!/usr/bin/python
#!/usr/bin/env

import time, os, urllib, urllib2, json

#thinkKey = 'AddKeyHere' # ---- Add your api key here ----
thinkKey = 'YHML8DFQZ1TBXO5A'
thinkUrl = 'https://api.thingspeak.com/update'

class logging(object):

    def __init__(self):
        self.chesterWeather = 'http://api.wunderground.com/api/080b28233d8a1a49/geolookup/conditions/q/UK/%s.json' % 'chester'

    def weatherPull(self):
        f = urllib2.urlopen(self.chesterWeather)
        json_string = f.read()
        parsed_json = json.loads(json_string)
        temp_c = parsed_json['current_observation']['temp_c']
        f.close()
        return temp_c

#    def sendData(url,key,field1,temp):
    def sendData(self,url,key):
        temp = self.weatherPull()
        values = {'key' : key,'field2' : temp}

        postdata = urllib.urlencode(values)
        req = urllib2.Request(url, postdata)

        log = time.strftime("%d-%m-%Y\n%H:%M:%S\n")
        log = log + "{:.1f}C\n".format(temp)

        try:
            # Send data to Thingspeak
            response = urllib2.urlopen(req, None, 5)
            html_string = response.read()
            response.close()
            log = log + 'Update ' + html_string

        except urllib2.HTTPError, e:
            log = log + 'Server could not fulfill the request. Error code: ' + e.code
        except urllib2.URLError, e:
            log = log + 'Failed to reach server. Reason: ' + e.reason
        except:
            log = log + 'Unknown error'

        print log

if __name__=="__main__":
#    temperature = sensor.read_temperature()
    start = logging()
#    start.sendData(thinkUrl,thinkKey,'field1',temperature)
    start.sendData(thinkUrl,thinkKey)
#    print "Inside temp - %0.1fC" % sensor.read_temperature()
