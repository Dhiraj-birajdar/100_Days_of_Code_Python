# with open("weather_data.csv") as file:
#     data = file.readlines()

# import csv
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#         print(temperature)

import pandas as pd

# data = pd.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])

# temp_list = data["temp"].to_list()
# avg_temp = sum(temp_list) / len(temp_list)
# print(int(avg_temp))
#
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data[data.day == "Monday"])
#
# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# celsius = int(monday.temp)
# print(celsius)
# fahrenheit = celsius * (9 / 5) + 32
# print(fahrenheit)

# data_dict = {
#     "name": ["Akash", "Dhiraj", "Suraj", "Apurva"],
#     "age": [12, 25, 23, 21]
# }
#
# data = pd.DataFrame(data_dict)
# print(data)
# data.to_csv("data.csv")

squirrel_data = pd.read_csv("Central_Park_Squirrel_Data.csv")
fur_color = squirrel_data["Primary Fur Color"]

# print(fur_color.value_counts())
# print(squirrel_data.count())
gray = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
red = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

print(gray, red, black)

color = {
    "color": ["gray", "cinnamon", "black"],
    "count": [gray, red, black]
}

color_count = pd.DataFrame(color)
color_count.to_csv("squirrel_color_count.csv")
