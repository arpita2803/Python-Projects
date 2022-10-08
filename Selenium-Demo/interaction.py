from selenium import webdriver
from selenium.webdriver.common.by import By

wiki_url = "https://en.wikipedia.org/wiki/Main_Page"
driver_path = "C:/Users/Hello/Chromedriver/chromedriver"

driver = webdriver.Chrome(driver_path)
driver.get(wiki_url)

article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
print(article_count.text)

driver.quit()
