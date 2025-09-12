import urllib.request, urllib.parse 
import json
from dotenv import load_dotenv
import os

load_dotenv()

APIKEY = os.getenv("OPENWEATHER_API_KEY")

serviceurl = 'https://api.openweathermap.org/data/2.5/weather?'

while True:
    city = input("Enter city: ")
    if len(city)<1:
        break
    
    city = city.strip()
    parms = dict()
    parms['q'] = city
    parms['appid'] = APIKEY
    parms['units'] = 'metric'

    url = serviceurl + urllib.parse.urlencode(parms)
    print("Retrieving", url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print("Retrieved", len(data), "characters")

    try:
        js = json.loads(data)
    except:
        js = None
    
    if not js or 'main' not in js:
        print("====DOWNLOAD ERROR====")
        print(data)
        continue