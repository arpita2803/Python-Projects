from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import re
import time

CHROME_DRIVER_PATH = "C:/Users/Hello/Chromedriver/chromedriver"
FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLScr52FQSSunWURcOG3g3NE5oG5m5BpDtBst6x1jDLJvod94PA/viewform?usp=sf_link"
ZILLOW_URL = "https://www.zillow.com/princeton-nj/rentals/?searchQueryState=%7B%22mapBounds%22%3A%7B%22north%22%3A40.51049006252678%2C%22east%22%3A-74.45285318359375%2C%22south%22%3A40.23742775976171%2C%22west%22%3A-74.87582681640625%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A3000%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A395489%2C%22regionType%22%3A6%7D%5D%2C%22pagination%22%3A%7B%7D%7D"
header = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

response = requests.get(url=ZILLOW_URL, headers=header)
website_data = response.text

soup = BeautifulSoup(website_data, "html.parser")
listing_links = [link.get("href").replace("/b/", "https://www.zillow.com/b/") for link in soup.select(selector="article div div a")]
address_lists = [address.getText()for address in soup.select(selector="article div div a address")]
price_list = [re.split('\+|/', price.getText())[0] for price in soup.select(selector="article div div div span") if price.get("data-test") == "property-card-price"]

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.get(FORM_URL)
time.sleep(5)
driver.maximize_window()

for index in range(len(address_lists)):
    address_input = driver.find_element(By.XPATH, "(//input[@type='text'])[1]")
    price_input = driver.find_element(By.XPATH, "(//input[@type='text'])[2]")
    link_input = driver.find_element(By.XPATH, "(//input[@type='text'])[3]")
    submit_button = driver.find_element(By.XPATH, "(//div[@role='button']/descendant::span[text()='Submit'])[1]")
    address_input.send_keys(address_lists[index])
    price_input.send_keys(price_list[index])
    link_input.send_keys(listing_links[index])
    submit_button.click()
    time.sleep(2)
    submit_another_link = driver.find_element(By.LINK_TEXT, "Submit another response")
    submit_another_link.click()
    #driver.refresh()
    time.sleep(5)

