import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

api_key = "680cea29a5031289372da166377eb210"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
MY_LAT = "19.150858"
MY_LONG = "73.078261"
account_sid = "AC131eb0386f8aa5ac4e626c240320ada8"
auth_token = "8fe702ee69fea766270bf374820b7745"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}
response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()

weather_data = response.json()
twelve_hours_data = weather_data["hourly"][:12]
# condition code = [item["weather"][0]["id"] for item in twelve_hours_data]

will_rain = False
for item in twelve_hours_data:
    weather_status = item["weather"][0]
    if weather_status["id"] < 700:
        will_rain = True

if will_rain:
    # proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    # client = Client(account_sid, auth_token, http_client=proxy_client)
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today!!Bring an ☔",
        from_='+19705783846',
        to='+919051095101'
    )
    print(message.status)
