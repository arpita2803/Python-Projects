import smtplib
import datetime as dt
import random

EMAIL = "XXXXXXXXXXXX@yahoo.com"
PASSWORD = "XXXXXXXXXXXXXXX"

now = dt.datetime.now()
# print(now.weekday()) #count starts from 0-Monday
weekday = now.weekday()

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
if weekday == 2:
    with open("quotes.txt") as file:
        quotes_list = file.readlines()

    todays_quote = random.choice(quotes_list).strip()

    # SMTP server of your email domain
    with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs="ad.iemcal@gmail.com",
            msg=f"Subject:{days[2]} Motivation\n\n{todays_quote}"
        )
