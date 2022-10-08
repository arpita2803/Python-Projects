from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time

driver_path = "C:/Users/Hello/Chromedriver/chromedriver"
email = "ad.iemcal@gmail.com"
password = "c08/a051"


driver = webdriver.Chrome(driver_path)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3153214094&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom")
time.sleep(5)
driver.maximize_window()

sign_in = driver.find_element(By.XPATH, "(//div[contains(@class,'nav__cta-container')]/a[normalize-space(text())='Sign in'])[1]")
sign_in.click()
time.sleep(5)

email_element = driver.find_element(By.ID, "username")
email_element.send_keys(email)
password_element = driver.find_element(By.NAME, "session_password")
password_element.send_keys(password)
sign_in_button = driver.find_element(By.XPATH, "(//button[normalize-space(text())='Sign in'])[1]")
sign_in_button.click()
time.sleep(5)

easy_apply_button = driver.find_element(By.XPATH, "(//div[@class='mt5']/descendant::span[text()='Easy Apply'])[1]")
easy_apply_button.click()
time.sleep(2)

try:
    submit_application_button = driver.find_element(By.XPATH, "(//button[@aria-label='Submit application'])[1]")
    submit_application_button.click()
except NoSuchElementException:
    dismiss_button = driver.find_element(By.XPATH, "(//button[@aria-label='Dismiss'])[1]")
    dismiss_button.click()
    save_button = driver.find_element(By.XPATH, "(//button[@data-control-name='save_application_btn'])[1]")
    save_button.click()

time.sleep(2)

#driver.quit()
