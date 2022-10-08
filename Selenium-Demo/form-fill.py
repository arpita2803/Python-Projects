from selenium import webdriver
from selenium.webdriver.common.by import By

driver_path = "C:/Users/Hello/Chromedriver/chromedriver"

driver = webdriver.Chrome(driver_path)
driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Arpita")
last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Das")
email = driver.find_element(By.NAME, "email")
email.send_keys("ad.iemcal@gmail.com")
sign_up = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
sign_up.click()

driver.quit()
