def get_value_from_colour(hue, origin):
    
    #most of the notes need to be supplemented
    
    vfc = "0"
    
    if origin == "CAD":
        if 171 <= hue <= 211:
            vfc = "5"
        elif 310 <= hue <= 350:
            vfc = "10"
        elif 79 <= hue <= 119:
            vfc = "20"
        elif 0 <= hue <= 24:
            vfc = "50"
        else:
            vfc = "100"
        return vfc
    
    elif origin == "GBP":
        if 77 <= hue <= 117:
            vfc = "1"
        elif 179 <= hue <= 219:
            vfc = "5"
        elif 27 <= hue <= 67:
            vfc = "10"
        elif 265 <= hue <= 305:
            vfc = "20"
        else:
            vfc = "50"
        return vfc
    
    elif origin == "AUD":
        if 187 <= hue <= 227:
            vfc = "100"
        elif 42 <= hue <= 77:
            vfc = "50"
        elif 5 <= hue <= 30:
            vfc = "20"
        elif 78 <= hue <= 113:
            vfc = "10"
        elif 337 <= hue <= 360:
            vfc = "5"
        #Pass 2
        elif 31 <= hue <= 56:
            vfc = "1"
        else:
            vfc = "2"
        return vfc
    
    elif origin == "CHF":
        if 24 <= hue <= 60:
            vfc = "10"
        elif  hue >= 340 or hue <= 23:
            vfc = "20"
        elif 61 <= hue <= 94:
            vfc = "50"
        elif 195 <= hue <= 235:
            vfc = "100"
        #Pass 200
        elif 249 <= hue <= 289:
            vfc = "1000"
        else:
            vfc = "200"
        return vfc
    
    elif origin == "EUR":
        if 137 <= hue <= 177:
            vfc = "5"
        elif  hue >= 349 or hue <= 21:
            vfc = "10"
        elif 184 <= hue <= 224:
            vfc = "20"
        elif 22 <= hue <= 54:
            vfc = "50"
        elif 60 <= hue <= 100:
            vfc = "100"
        #Pass 200
        elif 306 <= hue <= 346:
            vfc = "500"
        else:
            vfc = "200"
        return vfc
    
    elif origin == "HKD":
        if 256 <= hue <= 296:
            vfc = "10"
        elif  179 <= hue <= 219: 
            vfc = "20"
        elif 42 <= hue <= 82:
            vfc = "50"
        elif hue >= 354 or hue <= 21:
            vfc = "100"
        elif 22 <= hue <= 41:
            vfc = "500"
        else:
            vfc = "1000"
        return vfc
    
    elif origin == "INR":
        #Needs extra support
        if 27 <= hue <= 41:
            vfc = "10"
        elif  42 <= hue <= 57: 
            vfc = "20"
        elif 157 <= hue <= 197:
            vfc = "50"
        elif 229 <= hue <= 269:
            vfc = "100"
        elif 6 <= hue <= 26:
            vfc = "200"
        elif 58 <= hue <= 78:
            vfc = "500"
        else:
            vfc = "2000"
        return vfc
    
    elif origin == "MXN":
        if 186 <= hue <= 236:
            vfc = "20"
        elif  345 <= hue or hue <= 2: 
            vfc = "50"
        elif 3 <= hue <= 23:
            vfc = "100"
        elif 50 <= hue <= 90:
            vfc = "200"
        elif 24 <= hue <= 42:
            vfc = "500"
        else:
            vfc = "1000"
        return vfc
    
    elif origin == "NOK":
        if 81 <= hue <= 121:
            vfc = "50"
        elif  354 <= hue or hue <= 28: 
            vfc = "100"
        elif 180 <= hue <= 200:
            vfc = "200"
        elif 29 <= hue <= 63:
            vfc = "500"
        else:
            vfc = "1000"
        return vfc
    
    elif origin == "NZD":
        if 16 <= hue <= 43:
            vfc = "5"
        elif 176 <= hue <= 209:
            vfc = "10"
        elif 99 <= hue <= 139:
            vfc = "20"
        elif 210 <= hue <= 245:
            vfc = "50"
        else:
            vfc = "100"
        return vfc
    
    elif origin == "SEK":
        if 235 <= hue <= 267:
            vfc = "20"
        elif 15 <= hue <= 49:
            vfc = "50"
        elif 202 <= hue <= 234:
            vfc = "100"
        elif 75 <= hue <= 115:
            vfc = "200"
        elif 345 <= hue or hue <= 15:
            vfc = "500"
        #1000 sek is basically indiscernable from the 500
        else:
            vfc = "1000"
        return vfc
    
    elif origin == "SGP":
        if 18 <= hue <= 56:
            vfc = "2"
        elif 60 <= hue <= 100:
            vfc = "5"
        elif 341 <= hue or hue <= 17:
            vfc = "10"
        elif 182 <= hue <= 222:
            vfc = "50"
        #one hundred needs work
        else:
            vfc = "100"
        return vfc
    
    elif origin == "USD":
        #This should not be relied on for USD
        if 66 <= hue <= 76:
            vfc = "1"
        elif 39 <= hue <= 49:
            vfc = "5"
        elif 33 <= hue <= 38:
            vfc = "10"
        elif 79 <= hue <= 89:
            vfc = "20"
        elif 22 <= hue <= 32:
            vfc ="50"
        else:
            vfc = "100"
        return vfc
    
    else:
        vfc = "0"
        return vfc