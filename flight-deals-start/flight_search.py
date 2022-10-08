import requests
from flight_data import FlightData
from pprint import pprint

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "0GJTt6Ivo4cjvD49u7XXxxMhZhBr2C9F"


class FlightSearch:
    def __init__(self):
        self.header = {
            "apikey": TEQUILA_API_KEY
        }

    def get_destination_code(self, city):
        location_params = {
            "term": city,
            "location_types": "city",
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", params=location_params, headers=self.header)
        response.raise_for_status()
        code = response.json()["locations"][0]["code"]
        return code

    def find_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        search_params = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "curr": "GBP",
            "max_stopovers": 0,
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", params=search_params, headers=self.header)
        try:
            search_results = response.json()["data"][0]
        except IndexError:
            search_params["max_stopovers"] = 1
            response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", params=search_params, headers=self.header)
            try:
                search_results = response.json()["data"][0]
            except IndexError:
                print(f"No flight found for {destination_city_code}")
                return None
            else:
                print("1 Stop")
                print(search_results)
                flight_data = FlightData(
                    price=search_results["price"],
                    origin_city=search_results["route"][0]["cityFrom"],
                    origin_airport=search_results["route"][0]["flyFrom"],
                    destination_city=search_results["route"][1]["cityTo"],
                    destination_airport=search_results["route"][1]["flyTo"],
                    out_date=search_results["route"][0]["local_departure"].split("T")[0],
                    return_date=search_results["route"][2]["local_departure"].split("T")[0],
                    stop_overs=1,
                    via_city=search_results["route"][0]["cityTo"]
                )
                print(f"{flight_data.destination_city}: £{flight_data.price}")
                return flight_data
        else:
            print("Non Stop")
            flight_data = FlightData(
                price=search_results["price"],
                origin_city=search_results["route"][0]["cityFrom"],
                origin_airport=search_results["route"][0]["flyFrom"],
                destination_city=search_results["route"][0]["cityTo"],
                destination_airport=search_results["route"][0]["flyTo"],
                out_date=search_results["route"][0]["local_departure"].split("T")[0],
                return_date=search_results["route"][1]["local_departure"].split("T")[0],
            )
            print(f"{flight_data.destination_city}: £{flight_data.price}")
            return flight_data
