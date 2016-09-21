temp_c = 13 
ledNumber = 0

#form = (number / 8) * 1.25
#print form

#def translate(value,temp_min,temp_max):
#    span = temp_max - temp_min
#    scaled = float(value - temp_min) / float(span)
##    return temp_min+(scaled * span)
#    return scaled

if temp_c < 0:
#    strip.setPixelColorRGB(0,0,0,255) # Blue    
#    strip.show()
    print "below"
    pass

elif 0.1 <= temp_c <= 10:

#    mappedTemp = (temp_c / 8) * 1.25 
    mappedTemp = temp_c / 1.25 
#    mappedTemp = 0 + (7 - 0) * ((temp_c - 0) / (10 - 0));
    print "Number of led's int %d " % int(mappedTemp)
    print "Number of led's %d " % mappedTemp
    
    while (ledNumber <= int(mappedTemp)):
        print ledNumber
        print "Aqua"
#        strip.setPixelColorRGB(ledNumber,127,0,127) # Aqua    
        ledNumber = ledNumber + 1
#        strip.show()

elif 10.1 <= temp_c <= 20:
    convert_temp_c = temp_c - 10
#
#    mappedTemp = 0 + (7 - 0) * ((convert_temp_c - 0) / (10 - 0));
#    mappedTemp = (temp_c / 8) * 2.5 
    mappedTemp = convert_temp_c / 1.25 
#    mappedTemp = translate(temp_c,0,7)
    print "Number of led's int %d " % int(mappedTemp)
    print "Number of led's %d " % mappedTemp
    
    while (ledNumber < int(mappedTemp)):
        print ledNumber
        print "yellow"
#        strip.setPixelColorRGB(ledNumber,127,127,0) # Yellow   
        ledNumber = ledNumber + 1
#        strip.show()

elif 20.1 <= temp_c <= 30:

    mappedTemp = 0 + (7 - 0) * ((temp_c - 0) / (30 - 20));
    print "Number of led's int %d " % int(mappedTemp)
    print "Number of led's %d " % mappedTemp
    
    while (ledNumber < int(mappedTemp)):
        print ledNumber
        print "orange"
#        strip.setPixelColorRGB(ledNumber,255,127,0) # orange   
        ledNumber = ledNumber + 1
#        strip.show()

elif 30.1 <= temp_c <= 40:

    mappedTemp = 0 + (7 - 0) * ((temp_c - 0) / (40 - 30));
    print "Number of led's int %d " % int(mappedTemp)
    print "Number of led's %d " % mappedTemp
    
    while (ledNumber < int(mappedTemp)):
        print ledNumber
        print "red"
#        strip.setPixelColorRGB(ledNumber,255,0,0) # red    
        ledNumber = ledNumber + 1
#        strip.show()
