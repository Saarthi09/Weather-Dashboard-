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

    temp = js['main']['temp']
    feels = js['main']['feels_like']
    weather = js['weather'][0]['description']
    wind = js['wind']['speed']
    mintemp = js['main']['temp_min']
    maxtemp = js['main']['temp_max']

    print(f"City: {js['name']}, {js['sys']['country']}")
    print(f"Temperature: {temp}°C (feels like {feels}°C)")
    print(f"Condition: {weather}")
    print(f"Wind speed: {wind}")
    print(f"Max temp: {maxtemp}")
    print(f"Min temp: {mintemp}")