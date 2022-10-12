import requests


class DataManager:
    def __init__(self):
        self.sheety_api_key = "XXXXXXXXXXXXXXXXXXX"
        self.sheety_url = "https://api.sheety.co/49dcecfe1c0e319bf7cfa3e1b97feadd/flightDeals"
        self.sheety_header = {
            "Authorization": f"Bearer {self.sheety_api_key}"
        }
        self.destination_data = {}
        self.user_data = {}

    def get_destination_data(self):
        response = requests.get(url=f"{self.sheety_url}/prices", headers=self.sheety_header)
        response.raise_for_status()
        self.destination_data = response.json()["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            rec_id = city["id"]
            sheety_config = {
                "price": {
                    "iataCode": city["iataCode"],
                }
            }
            response = requests.put(url=f"{self.sheety_url}/prices/{rec_id}", json=sheety_config, headers=self.sheety_header)
            # print(response.text)

    def get_user_data(self):
        response = requests.get(url=f"{self.sheety_url}/users", headers=self.sheety_header)
        response.raise_for_status()
        self.user_data = response.json()["users"]
        return self.user_data
