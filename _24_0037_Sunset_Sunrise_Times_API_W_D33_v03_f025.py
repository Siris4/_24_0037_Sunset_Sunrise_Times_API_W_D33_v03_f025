import requests
from datetime import datetime

MY_LAT = 25.672939
MY_LNG = -100.309731

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0  # To get the time in 24-hour format
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()

sunrise_time = data['results']["sunrise"]
sunset_time = data['results']['sunset']

print(f"The official sunrise time is: {sunrise_time}")
print(f"The official sunset time is: {sunset_time}")

time_now = datetime.now()
print(f"Current time: {time_now}")
