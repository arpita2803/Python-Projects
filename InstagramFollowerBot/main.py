import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = "C:/Users/Hello/Chromedriver/chromedriver"
USERNAME = "arpita.das.2803"
PASSWORD = "081040110021"
SIMILAR_ACCOUNT = "nasa"
URL = "https://www.instagram.com/"

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)

    def login(self):
        self.driver.get(url=URL)
        time.sleep(5)
        self.driver.maximize_window()
        username = self.driver.find_element(By.NAME, "username")
        username.send_keys(USERNAME)
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(PASSWORD)
        login_button = self.driver.find_element(By.XPATH, "(//button[@type='submit'])[1]")
        login_button.click()
        time.sleep(5)
        not_now_button = self.driver.find_element(By.XPATH, "(//button[normalize-space(text())='Not Now'])[1]")
        not_now_button.click()

    def find_following(self):
        self.driver.get(url="https://www.instagram.com/bigbangtheory/")
        time.sleep(5)
        following_list = self.driver.find_element(By.XPATH, "(//a[contains(@href,'following')])[1]")
        following_list.click()
        time.sleep(5)
        scrollable_popup = self.driver.find_element(By.XPATH, "(//div[@class='_aano'])[1]")
        while True:
            try:
                follow = self.driver.find_element(By.XPATH, "(//a[contains(@href,'starwars')])[1]")
                break
            except NoSuchElementException:
                self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_popup)
                time.sleep(2)

    def follow(self):
        follow_button = self.driver.find_element(By.XPATH, "(//a[contains(@href,'starwars')]/ancestor::div[@aria-labelledby]/descendant::button)[1]")
        follow_button.click()


instafollower = InstaFollower()
instafollower.login()
instafollower.find_following()
instafollower.follow()
instafollower.driver.quit()
