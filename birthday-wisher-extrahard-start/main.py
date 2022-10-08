##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas as pd
import datetime as dt
import random
import smtplib

USERNAME = "arpita2803@yahoo.com"
PASSWORD = "quekqguxdhcdlunc"

birthday_df = pd.read_csv("birthdays.csv")

birthday_dict = birthday_df.to_dict(orient="records")

today = dt.datetime.now()

for item in birthday_dict:
    if item["day"] == today.day and item["month"] == today.month:
        filepath = f"./letter_templates/letter_{random.randint(1,3)}.txt"
        with open(filepath) as file:
            template = "".join(file.readlines())
            message = template.replace("[NAME]", item["name"])

        with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
            connection.starttls()
            connection.login(user=USERNAME, password=PASSWORD)
            connection.sendmail(
                from_addr=USERNAME,
                to_addrs=item["email"],
                msg=f"Subject:Happy Birthday!!\n\n{message}"
            )



