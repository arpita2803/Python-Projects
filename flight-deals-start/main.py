#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import datetime, timedelta
from pprint import pprint

ORIGIN_CITY_CODE = "LON"

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()
sheet_data = data_manager.get_destination_data()

for item in sheet_data:
    city = item["city"]
    iatacode = item["iataCode"]
    if iatacode == "":
        location_code = flight_search.get_destination_code(city)
        item["iataCode"] = location_code

data_manager.destination_data = sheet_data
data_manager.update_destination_codes()

from_time = datetime.now() + timedelta(days=1)
to_time = from_time + timedelta(days=(6 * 30))
for item in sheet_data:
    city_code = item["iataCode"]
    lowest_price = item["lowestPrice"]
    flight = flight_search.find_flights(ORIGIN_CITY_CODE, city_code, from_time, to_time)
    if flight is None:
        continue
    if flight.price < lowest_price:
        message = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        # notification_manager.send_sms(message)
        print(f"Stopovers : {flight.stop_overs}")
        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."

        google_link = f"https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}.{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"

        user_data = data_manager.get_user_data()
        user_details = [(row["firstName"], row["email"]) for row in user_data]
        notification_manager.send_emails(message, user_details, google_link)



