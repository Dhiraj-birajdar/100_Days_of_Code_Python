import requests

api_key = "58b82e17bc9f4f8ddd88ca282f7739fe"
lat = 18.427402
lon = 73.808073
# part = daily
end_point = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={api_key}"
end_pointc = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"

response = requests.get(url=end_pointc)

data = response.json()
print(data)