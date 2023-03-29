import smtplib
import requests
from datetime import datetime

MY_LAT = 18.427402 # Your latitude
MY_LONG = 73.808073 # Your longitude


def check_pos():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    return (MY_LAT - 5) <= iss_latitude <= (MY_LAT + 5) and (MY_LONG - 5) <= iss_longitude <= (MY_LONG - 5)


def check_time():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    return sunset <= time_now.hour <= sunrise
    # return MY_LAT < iss_latitude < MY_LAT
    # return 1<4<2
#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.


my_gmail = "asiancollege411041@gmail.com"
password = "kthqhuhmktvuxuuc"
to_mail = "rawemi5496@orgria.com"

if check_pos() and check_time():
    with smtplib.SMTP("smtp.gmail.com", 587) as google:
        google.starttls()
        google.login(user=my_gmail, password=password)
        google.sendmail(from_addr=my_gmail, to_addrs=to_mail, msg="Subject: iss tracker\n\niss is over your head look up.")
