from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver_path = "C:/Users/Hello/Chromedriver/chromedriver"

driver = webdriver.Chrome(driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")


cookie = driver.find_element(By.ID, "cookie")
cps = driver.find_element(By.ID, "cps")
purchase_timeout = time.time() + 5
game_timeout = time.time() + 60 * 5

while True:
    cookie.click()
    if time.time() >= game_timeout:
        print(cps.text)
        break
    if time.time() >= purchase_timeout:
        items = driver.find_elements(By.XPATH, "//div[@id='store']/div[@class!='grayed']/b")
        item_prices = [float(item.text.split("-")[1].strip().replace(",", "")) for item in items]
        item = items[item_prices.index(max(item_prices))]
        item.click()
        purchase_timeout = time.time() + 5

driver.quit()




