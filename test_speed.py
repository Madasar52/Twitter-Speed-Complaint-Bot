from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://fast.com")

# start_speed_test = driver.find_element(By.CSS_SELECTOR, ".start-button a")
# start_speed_test.click()
print("timer started")
time.sleep(50)
download_speed = driver.find_element(By.ID, "speed-value").text
print(download_speed)


more_info = driver.find_element(By.CSS_SELECTOR, ".more-info-container a")
more_info.click()


time.sleep(3)
upload_speed = driver.find_element(By.ID, "upload-value").text
print(upload_speed)















