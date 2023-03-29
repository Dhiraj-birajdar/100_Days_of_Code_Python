import smtplib
import datetime as dt
from random import choice

my_gmail = "asiancollege411041@gmail.com"
password = "kthqhuhmktvuxuuc"
to_mail = "rawemi5496@orgria.com"

# if dt.datetime.now().weekday() == 5:
#     with open("quotes.txt", "r") as file:
#         quotes = file.readlines()
#     q = choice(quotes)
#     quote = f"Subject: Motivational Quote\n\n{q.split('-')[0]}\n    -{q.split('-')[1]}"
#
#     with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#         connection.starttls()
#         connection.login(user=my_gmail, password=password)
#         connection.sendmail(
#             from_addr=my_gmail,
#             to_addrs=to_mail,
#             msg=quote
#         )
#         print("Email sent 👍😊")
# else:
#     print("Today is not Monday")


for i in range(51):
    with open("quotes.txt", "r") as file:
        quotes = file.readlines()
    q = choice(quotes)
    quote = f"Subject: Motivational Quote {i}\n\n{q.split('-')[0]}\n    -{q.split('-')[1]}"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_gmail, password=password)
        connection.sendmail(
            from_addr=my_gmail,
            to_addrs=to_mail,
            msg=quote
        )
    print(i)
