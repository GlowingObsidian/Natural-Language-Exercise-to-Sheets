import os
import requests
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")

natural_lang_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

params = {
    "query": "I ran for 3 Km"
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

data = requests.post(url=natural_lang_endpoint, json=params, headers=headers)
data.raise_for_status()
print(data.json())