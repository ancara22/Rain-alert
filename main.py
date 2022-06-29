import requests
from twilio.rest import Client

LAT = 51.577710
LONG = 0.102185
API = "3ebc7562731f35c08ce9b75a302767db"
URL = f"https://api.openweathermap.org/data/2.5/onecall"
account_sid = 'ACcd5a423a900e6a83147fffd9dbcc4237'
auth_token = '369673874bc95d0e2bf484a80a0c5f81'

param = {
    "lat": 51.577710,
    "lon": 0.102185,
    "appid": API,
    "exclude": "current,minutely,daily"
}


request = requests.get(url=URL, params=param)
request.raise_for_status()
request_data = request.json()
weather_slice = request_data["hourly"][:12]

will_rain = False

for hour in weather_slice:
    condition_code = hour["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages\
        .create(
             body=f"Rain Alert\n\n",
             from_='+19894991090',
             to='**********'
        )