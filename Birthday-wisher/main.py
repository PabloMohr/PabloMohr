import smtplib
import datetime as dt
import random
import pandas as pd

my_email = ""
password = ""

now = dt.datetime.now()
today = (now.month, now.day)
data = pd.read_csv("birthdays.csv")
birthdays_dict = {}

birthdays_dict = {(int(row['month']), int(row['day'])): row for row_index, row in data.iterrows()}


if today in birthdays_dict:
    with open(f".\letter_templates\letter_{random.randint(1, 3)}.txt") as txt:
        letter = txt.read()
        today_name = (birthdays_dict[today]["name"])
        letter_with_name = letter.replace("[NAME]", today_name)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject:Happy birthday\n\n{letter_with_name}")






