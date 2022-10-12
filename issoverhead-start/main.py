import requests
from datetime import datetime
import smtplib
import time

EMAIL = "XXXXXXXXX@yahoo.com"
PASSWORD = "XXXXXXXXXXXXX"

MY_LAT = 19.150866
MY_LONG = 73.078243


# Your position is within +5 or -5 degrees of the ISS position.
def is_iss_overhead():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_data = iss_response.json()
    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])
    print((iss_latitude, iss_longitude))
    abs_lat = abs(iss_latitude - MY_LAT)
    abs_long = abs(iss_longitude - MY_LONG)
    return abs_lat <= 5 and abs_long <= 5


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}


def is_night():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    time_now = datetime.now()
    utc_offset = time_now - datetime.utcnow()
    sunrise = datetime.strptime(data["results"]["sunrise"].split("+")[0], '%Y-%m-%dT%H:%M:%S') + utc_offset
    sunset = datetime.strptime(data["results"]["sunset"].split("+")[0], '%Y-%m-%dT%H:%M:%S') + utc_offset
    return not sunrise < time_now < sunset


# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

while True:
    #time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.mail.yahoo.com")
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg="Subject:Spot the ISS in the sky!!\n\nISS is above you in the sky!"
        )






