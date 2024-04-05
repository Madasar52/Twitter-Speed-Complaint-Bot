from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

TWITTER_EMAIL = os.environ.get("email")
TWITTER_PASSWORD = os.environ.get("password")
TWITTER_USERNAME = os.environ.get("username")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://twitter.com")

time.sleep(5)
sign_in = driver.find_element(By.LINK_TEXT, "Sign in").click()


time.sleep(5)
try:
    time.sleep(5)
    username = driver.find_element(By.CSS_SELECTOR, value='input[autocomplete="username"]')
    username.send_keys('latifshahzada4@gmail.com', Keys.ENTER)
    password = driver.find_element(By.CSS_SELECTOR, value='input[autocomplete="current-password"]')
    password.send_keys(TWITTER_PASSWORD, Keys.ENTER)

    time.sleep(5)
except NoSuchElementException:
    time.sleep(5)
    print("exception raised")
    username = driver.find_element(By.CSS_SELECTOR, value='input[data-testid="ocfEnterTextTextInput"]')
    username.send_keys(TWITTER_USERNAME, Keys.ENTER)

    time.sleep(5)
finally:
    time.sleep(5)
    password = driver.find_element(By.CSS_SELECTOR, value='input[autocomplete="current-password"]')
    password.send_keys(TWITTER_PASSWORD,Keys.ENTER)


    time.sleep(10)
    enter_tweet = driver.find_element(By.CSS_SELECTOR, value='br[data-text="true"]')
    enter_tweet.send_keys("Spiderman ps4 was peak super hero game")

    time.sleep(5)
    send_tweet = driver.find_element(By.CSS_SELECTOR, value='div[data-testid="tweetButtonInline"]')
    send_tweet.click()


















