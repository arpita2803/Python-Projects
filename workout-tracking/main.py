import requests
from datetime import datetime

APP_ID = "d1d80ba3"
API_KEY = "c631a6811878f7f103ad7880fcfea9a2"
BEARER_TOKEN = "c631a68f7f103ad788fcfea9a2"
GENDER = "female"
WEIGHT_KG = 63
HEIGHT_CM = 162
AGE = 32

exercise_url = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_input = input("Tell me which exercises you did: ")
exercise_header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
exercise_config = {
    "query": exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}
exercise_response = requests.post(url=exercise_url, json=exercise_config, headers=exercise_header)
exercise_data = exercise_response.json()

sheety_url = "https://api.sheety.co/49dcecfe1c0e319bf7cfa3e1b97feadd/myWorkouts/workouts"
sheety_header = {
    "Authorization": f"Bearer {BEARER_TOKEN}"
}
for exercise in exercise_data["exercises"]:
    name = exercise["name"].title()
    duration = exercise["duration_min"]
    calories = exercise["nf_calories"]
    current_datetime = datetime.now()
    date = current_datetime.strftime("%d/%m/%Y")
    time = current_datetime.strftime("%X")
    sheety_config = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": name,
            "duration": duration,
            "calories": calories,
        }
    }

    sheety_response = requests.post(url=sheety_url, json=sheety_config, headers=sheety_header)
    print(sheety_response.text)
