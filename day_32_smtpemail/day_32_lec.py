import smtplib
import datetime as dt
from random import choice

my_gmail = "asiancollege411041@gmail.com"
password = "kthqhuhmktvuxuuc"

to_mail = "rawemi5496@orgria.com"

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_gmail, password=password)
    connection.sendmail(
        from_addr=my_gmail,
        to_addrs=to_mail,
        msg="Subject: hello again\n\nThis is body of my email."
    )


now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
# print(day_of_week)

# DOB = dt.datetime(day=15, month=12, year=2000)
# print(DOB)
