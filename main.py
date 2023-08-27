import os
import requests
from dotenv import load_dotenv
import datetime

load_dotenv()

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
AUTHORIZATION = os.getenv("AUTH")

natural_lang_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/651b7aa61c85102e5620785bbfa7026f/workoutSheets/workouts/"

natural_lang_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

sheety_headers = {
    "Authorization": AUTHORIZATION
}

query = input("Tell me which exercises you did: ")

jsonExercise = {
    "query": query
}

exerciseResponse = requests.post(url=natural_lang_endpoint, json=jsonExercise, headers=natural_lang_headers)
exerciseResponse.raise_for_status()

exercises = exerciseResponse.json()['exercises']

current = datetime.datetime.now()

for exercise in exercises:
    jsonSheety = {
        "workout": {
            "date": current.strftime("%d/%m/%Y"),
            "time": current.strftime("%H:%M:%S"),
            "exercise": exercise['name'],
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories']
        }
    }

    response = requests.post(url=sheety_endpoint, json=jsonSheety, headers=sheety_headers)
    response.raise_for_status()

print(response)
