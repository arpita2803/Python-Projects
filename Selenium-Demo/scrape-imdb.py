from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

driver_path = "C:/Users/Hello/Chromedriver/chromedriver"

driver = webdriver.Chrome(driver_path)
driver.get("https://www.imdb.com/list/ls070481274/")
driver.maximize_window()

movie_actors = driver.find_elements(By.XPATH, "//div[@class='lister-item-content']/p[@class='text-muted text-small'][2]")
for item in movie_actors:
    print(item.text)

driver.quit()