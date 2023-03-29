import datetime as dt
from random import randint
import pandas as pd
import smtplib

ascii_art = """

╦ ╦┌─┐┌─┐┌─┐┬ ┬        
╠═╣├─┤├─┘├─┘└┬┘        
╩ ╩┴ ┴┴  ┴   ┴         
╔╗ ┬┬─┐┌┬┐┬ ┬┌┬┐┌─┐┬ ┬ 
╠╩╗│├┬┘ │ ├─┤ ││├─┤└┬┘ 
╚═╝┴┴└─ ┴ ┴ ┴─┴┘┴ ┴ ┴  
╔═╗┬ ┬┬ ┬┌┐ ┬ ┬┌─┐┌┬┐  
╚═╗├─┤│ │├┴┐├─┤├─┤│││  
╚═╝┴ ┴└─┘└─┘┴ ┴┴ ┴┴ ┴  

"""
# my login details
MY_EMAIL = "asiancollege411041@gmail.com"
PASS = "kthqhuhmktvuxuuc"

# get today's date and get list of birthday's
today = dt.datetime.now()
dobs = pd.read_csv("birthdays.csv")
data = dobs.to_dict(orient="records")

# send email
for dob in data:
    if today.month == dob["month"] and today.day == dob["day"]:
        with open(f"letter_templates/letter_{randint(1,3)}.txt", 'r') as file:
            letter = file.read()
        letter = letter.replace("[NAME]", f"{dob['name']}")
        with smtplib.SMTP("smtp.gmail.com", 587) as google:
            google.starttls()
            google.login(MY_EMAIL, PASS)
            # google.sendmail(from_addr=MY_EMAIL, to_addrs=dob["email"], msg=f"Subject: Happy Birthday\n\n{letter}")
            google.sendmail(from_addr=MY_EMAIL, to_addrs=dob["email"], msg=f"Subject: Happy Birthday\n\n{letter}\n\n("
                                                                           f"Sent using python anywhere cloud service)")

        print("Email sent 🥳")
