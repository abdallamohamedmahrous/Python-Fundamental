from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.youtube.com/feed/channels")
driver.maximize_window()

email_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div[1]/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input')))
email_input.send_keys("test01154775040@gmail.com")

next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="identifierNext"]/div/button/span')))   
next_button.click()

pass_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')))
pass_input.send_keys("Am1234567")

next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="passwordNext"]/div/button/span')))   
next_button.click()

channel_name_elements = WebDriverWait(driver, 200).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "yt-formatted-string#text.style-scope.ytd-channel-name"))
)
for channel_name in channel_name_elements:
    print(channel_name.text)
    
# try:   
#     while True:
#         pass     
# except KeyboardInterrupt:
#     driver.quit()


