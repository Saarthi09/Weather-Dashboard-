import json, requests

url = "https://api.openweathermap.org/data/2.5/weather?q=Delhi&appid=12f1e1829c6ef03b9fa9c2c43aa212b8&units=metric"
res = requests.get(url)
js = res.json()
print(json.dumps(js, indent=4))