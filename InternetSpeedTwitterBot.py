from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
import os

PROMISED_DOWN = 40
PROMISED_UP = 10
CHROME_DRIVER_PATH = '/Users/angela/Development/chromedriver'
TWITTER_EMAIL = os.environ.get("email")
TWITTER_PASSWORD = os.environ.get("password")
TWITTER_USERNAME = os.environ.get("username")

class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.up = 0
        self.down = 0


    def get_internet_speed(self):
        self.driver.get('https://fast.com')
        print("timer for speed test started")
        time.sleep(50)
        self.down = self.driver.find_element(By.ID, "speed-value").text
        print(self.down)

        more_info = self.driver.find_element(By.CSS_SELECTOR, ".more-info-container a")
        more_info.click()

        time.sleep(3)
        self.up = self.driver.find_element(By.ID, "upload-value").text
        print(self.up)



    def tweet_at_provider(self):
        self.driver.get("https://twitter.com")

        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, "Sign in").click()

        time.sleep(5)
        try:
            time.sleep(5)
            username = self.driver.find_element(By.CSS_SELECTOR, value='input[autocomplete="username"]')
            username.send_keys('latifshahzada4@gmail.com', Keys.ENTER)
            password = self.driver.find_element(By.CSS_SELECTOR, value='input[autocomplete="current-password"]')
            password.send_keys(TWITTER_PASSWORD, Keys.ENTER)

            time.sleep(5)
        except NoSuchElementException:
            time.sleep(5)
            print("exception raised")
            username = self.driver.find_element(By.CSS_SELECTOR, value='input[data-testid="ocfEnterTextTextInput"]')
            username.send_keys(TWITTER_USERNAME, Keys.ENTER)

            time.sleep(5)
        finally:
            time.sleep(5)
            password = self.driver.find_element(By.CSS_SELECTOR, value='input[autocomplete="current-password"]')
            password.send_keys(TWITTER_PASSWORD, Keys.ENTER)

            time.sleep(10)
            enter_tweet = self.driver.find_element(By.CSS_SELECTOR, value='br[data-text="true"]')
            enter_tweet.send_keys(f"internet speed test download speed={self.down} mbps and upload speed={self.up}mbps.")
            print("tweet done")

            time.sleep(5)
            send_tweet = self.driver.find_element(By.CSS_SELECTOR, value='div[data-testid="tweetButtonInline"]')
            send_tweet.click()

            time.sleep(10)
            self.driver.quit()






































