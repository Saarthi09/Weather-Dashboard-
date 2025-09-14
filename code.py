import urllib.request, urllib.parse #For making HTTP requests and encoding URL parameters
import json                         #For parsing JSON responses
from dotenv import load_dotenv      #For loading environment variables from .env file
import os                           #For accessing environment variables 

#First we will add the API key to access the OpenWeatherMap API
load_dotenv()

APIKEY = os.getenv("OPENWEATHER_API_KEY")

serviceurl = 'https://api.openweathermap.org/data/2.5/weather?' #This is the base url to use the API

while True:
    city = input("Enter city: ") #Taking input for city
    if len(city)<1:
        break
    
    city = city.strip()
    parms = dict()              #Creating a dictionary for parameters
    parms['q'] = city           #Creating the query parameter 
    parms['appid'] = APIKEY     #Adding API key to dictionary (required to access the API)
    parms['units'] = 'metric'   #Choosing units

    url = serviceurl + urllib.parse.urlencode(parms)    #Creating the final URL that will give the city's weather information
    print("Retrieving", url)
    uh = urllib.request.urlopen(url)                    #Opening the created URL
    data = uh.read().decode()                           #Reading and decoding the opened URL
    print("Retrieved", len(data), "characters")

    try:
        js = json.loads(data) #Parse JSON  
    except:
        js = None
    
    if not js or 'main' not in js:  #If parsing fails or main is missing, show error
        print("====DOWNLOAD ERROR====")
        print(data)
        continue

#Extracting useful information
    temp = js['main']['temp']
    feels = js['main']['feels_like']
    weather = js['weather'][0]['description']
    wind = js['wind']['speed']
    mintemp = js['main']['temp_min']
    maxtemp = js['main']['temp_max']
#Printing extracted information 
    print(f"City: {js['name']}, {js['sys']['country']}")
    print(f"Temperature: {temp}°C (feels like {feels}°C)")
    print(f"Condition: {weather}")
    print(f"Wind speed: {wind}")
    print(f"Max temp: {maxtemp}")
    print(f"Min temp: {mintemp}")