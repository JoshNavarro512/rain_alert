from http.client import responses
from urllib import response


import requests


api_key="ENTER YOUR API KEY HERE"

end_point = "https://api.openweathermap.org/data/2.5/onecall"

parameters = {
    "lat": 30.267153,
    "lon": -97.743057,
    "exclude": "current,minutely,daily",
    "appid": "29f2013083a11e82bc35e6604ce77fc3"
}



response = requests.get(end_point, params=parameters)
response.raise_for_status()

weather_data =response.json()


print(weather_data)
