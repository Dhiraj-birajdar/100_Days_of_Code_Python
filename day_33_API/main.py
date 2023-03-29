import requests
import datetime as dt

MY_LAT = 18.427402
MY_LNG = 73.808073
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
#
# latitude = data["iss_position"]["latitude"]
# longitude = data["iss_position"]["longitude"]
#
# iss_position = (latitude, longitude)
# print(iss_position)






today = dt.datetime.today()
parameter = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

# api_endpoint = f"https://api.sunrise-sunset.org/json?lat={MY_LAT}&lng={MY_LNG}&formatted=0"
# response = requests.get(url=api_endpoint)

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameter)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise, sunset, "\n", dt.datetime.now().hour, "\n", dt.datetime.now())
