import requests
import os
from datetime import datetime as dt


end_point = "https://trackapi.nutritionix.com/v2/natural/exercise"
query = input("What did you do today? (Exercise) : ")
parameter = {
        "query": query,
        # "gender": "female",
        # "weight_kg": 72.5,
        # "height_cm": 167.64,
        # "age": 30
}

headers = {
        "x-app-id": os.environ["APP_ID"],
        "x-app-key": os.environ["API_KEY"],
        "x-remote-user-id": "0"
}

response = requests.post(url=end_point, json=parameter, headers=headers)
response.raise_for_status()
data = response.json()

today = dt.now()

sheet_get = "https://api.sheety.co/12610ac30f6fe182edfff1ace732bfe8/workoutTracking/workouts"
sheet_post = "https://api.sheety.co/12610ac30f6fe182edfff1ace732bfe8/workoutTracking/workouts"
# row = requests.get(url=sheet_get)
# print(row.json())

row_insert = {
  "workout":  {
    "date": today.strftime("%d/%m/%Y"),
    "time": today.strftime("%H:%M:%S"),
    "exercise": data["exercises"][0]["user_input"],
    "duration": data["exercises"][0]["duration_min"],
    "calories": data["exercises"][0]["nf_calories"]
  }
}
#
sheet_auth = {
    "Authorization": os.environ["AUTH_TOKEN"]
}
post = requests.post(url=sheet_post, json=row_insert, headers=sheet_auth)
print(post.json())
