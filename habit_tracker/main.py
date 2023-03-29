import requests
from datetime import datetime
TOKEN = "abcdefgh1234"
USERNAME = "dhirajbirajdar"
GRAPH_ID = "graph1"

# ------------------ creating user ----------------------
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


# ------------------ creating graph ----------------------
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# ------------------ posting data/pixel ----------------------
post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# today = datetime(year=2023, month=3, day=12)
today = datetime.now()

post_pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "5"
}
# response = requests.post(url=post_pixel_endpoint, json=post_pixel_config, headers=headers)
# print(response.text)

# ------------------ updating data/pixel ----------------------
put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20230313"

update = {
    "quantity": "2"
}

# response = requests.put(url=put_endpoint, headers=headers, json=update)
# print(response.text)

# ------------------ deleting data/pixel ----------------------
delete_endpoint = put_endpoint
response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)