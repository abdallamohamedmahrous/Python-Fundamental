from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
# Acsess  to chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://support.microsoft.com/en-us/windows/open-the-camera-in-windows-8da044ed-c4a8-2fb4-da51-232362e4126d")
driver.maximize_window()

# Sign in 
sign_in: WebElement = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/header/div/div/div[4]/div[2]/div/a/div/div')
sign_in.click()

# inter to email auto
email_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="i0116"]')))
email_input.send_keys("abdallamahrous1221@gmail.com")


# Acsess to next auto 
next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[4]/div/div/div/div[2]/input')))   
next_button.click()


# Acsess to password
acsse_pass = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div[2]/div[2]/div/form/div[3]/div/div/div/span')))   
acsse_pass.click()

#  inter password auto 
pass_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="i0118"]')))
pass_input.send_keys("Am1221221A")

# Acsess to next auto 
next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div[2]/div[2]/div/form/div[5]/div/div/div/div/button')))   
next_button.click()

#  button to acsess camera
yes_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div[2]/div[2]/div/form/div[3]/div[2]/div/div[2]/button')))   
yes_button.click()

# open camera auto
open_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Open")]')))   
open_button.click()

# driver.get_screenshot_as_file("screen.jpg")

try:
       while True:
        pass     
except KeyboardInterrupt:
    driver.quit()



