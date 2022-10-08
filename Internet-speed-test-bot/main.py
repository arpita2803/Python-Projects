from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time

CHROME_DRIVER_PATH = "C:/Users/Hello/Chromedriver/chromedriver"
PROMISED_UP = 150
PROMISED_DOWN = 150


class InternetSpeedTweeterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.driver.maximize_window()
        time.sleep(5)
        go_button = self.driver.find_element(By.CSS_SELECTOR, ".js-start-test")
        go_button.click()
        time.sleep(120)
        # try:
        #     dismiss_button = self.driver.find_element(By.CSS_SELECTOR, ".desktop-app-prompt-modal a")
        #     dismiss_button.click()
        # except NoSuchElementException:
        #     print("Pop up not displayed")
        download_speed = self.driver.find_element(By.CSS_SELECTOR, ".download-speed")
        self.down = float(download_speed.text)
        upload_speed = self.driver.find_element(By.CSS_SELECTOR, ".upload-speed")
        self.up = float(upload_speed.text)

    def tweet_at_provider(self):
        if self.up < PROMISED_UP or self.down < PROMISED_DOWN:
            self.driver.get("https://twitter.com/login")
            tabs = self.driver.window_handles()
            self.driver.switch_to(tabs[1])
            time.sleep(5)
            tweet_button = self.driver.find_element(By.XPATH("(//a[@aria-label='Tweet' and @role='link'])[1]"))
            tweet_button.click()
            choose_audience = self.driver.find_element(By.XPATH, "(//div[@aria-label='Choose audience' and @role='button'])[1]")
            choose_audience.click()
            tweeter_circle = self.driver.find_element(By.XPATH, "(//div[@role='menuitem']/descendant::span[normalize-space(text())='Twitter Circle'])[1]")
            tweeter_circle.click()
            tweet_box = self.driver.find_element(By.XPATH, "(//div[@role='textbox' and @aria-label='Tweet text'])[1]")
            tweet_box.click()
            message = f"Hey ISP, why my internet speed {self.down}down/{self.up} when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up"
            tweet_box.send_keys(message)
            submit_tweet = self.driver.find_element(By.XPATH, "(//div[@role='button' and @data-testid='tweetButton'])[1]")
            submit_tweet.click()


bot = InternetSpeedTweeterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
