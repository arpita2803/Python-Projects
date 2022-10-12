from pprint import pprint
import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

EMAIL = "XXXXXXX@yahoo.com"
PASSWORD = "XXXXXXXXXXXXXXX"

PRODUCT_URL = "https://www.amazon.in/Fossil-Jacqueline-Analog-Womens-Watch-ES3843/dp/B00WM0CF4A/?_encoding=UTF8&pd_rd_w=gE6Ya&content-id=amzn1.sym.ee853eb9-cee5-4961-910b-2f169311a086&pf_rd_p=ee853eb9-cee5-4961-910b-2f169311a086&pf_rd_r=R0VQVMX2S6BWCCCHN5V1&pd_rd_wg=LBIET&pd_rd_r=62b71aa5-9b48-40ef-b10b-8406ea015016&ref_=pd_gw_ci_mcx_mr_hp_atf_m"
header = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}
amazon_response = requests.get(url=PRODUCT_URL, headers=header)
content = amazon_response.text

soup = BeautifulSoup(content, "lxml")
price = float(soup.find(name="span", class_="a-offscreen").getText()[1:].replace(",", ""))
title = soup.find(name="span", id="productTitle").getText().strip()

if price <= 5000:
    message = f"{title} price is now ₹{price}"
    with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs="ad.iemcal@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}.\nUse this link to purchase {PRODUCT_URL}".encode('utf-8')
        )
