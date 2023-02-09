import requests

with open('config', encoding='UTF-8') as file:
    s = file.read()
    config_data = {j.split('=')[0]: j.split('=')[1] for j in s.split()}

appid = config_data['WEATHER_API']
s_city = 'Moscow'
res = None

try:
    res = requests.get("https://api.openweathermap.org/data/2.5/find",
                       params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})
    if res.status_code == 200:
        print('Got the data, processing...')
    else:
        raise IOError

    data = res.json()
    cities = ["{} ({})".format(d['name'], d['sys']['country'])
              for d in data['list']]
    print("city:", cities)
    city_id = data['list'][0]['id']
    print('city_id=', city_id)
except Exception as e:
    print(f'Got the exception: {e}')

try:
    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                 params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()
    print("conditions:", data['weather'][0]['description'])
    print("temp:", data['main']['temp'])
    print("temp_min:", data['main']['temp_min'])
    print("temp_max:", data['main']['temp_max'])
except Exception as e:
    print("Exception (weather):", e)
    pass

