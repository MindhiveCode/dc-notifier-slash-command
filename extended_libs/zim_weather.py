import requests
import json
import urllib.parse

api_key = "8b5c6efb59eeda286b6a1ddfb26a146f"


def weather_check():
    zim_city_name = urllib.parse.quote_plus("Harare Province")
    weather_url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(zim_city_name,api_key)
    request = requests.get(weather_url).text

    weather_data = json.loads(request)

    return weather_data


def kelvin_to_fahrenheit(kelvin):
    temp_F = kelvin * (9 / 5) - 459.67
    temp_F = round(temp_F, 1)
    return temp_F

print(weather_check()['weather'][0]['main'])