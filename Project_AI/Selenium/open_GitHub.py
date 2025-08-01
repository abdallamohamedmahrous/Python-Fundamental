from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Acsess  to chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://github.com/")
driver.maximize_window()

# Sign in 
sign_in: WebElement = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/header/div/div[2]/div/div/div')
sign_in.click()

# inter to email auto
email_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="login_field"]')))
email_input.send_keys("abdallamahrous1221@gmail.com")


#  inter password auto 
pass_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]')))
pass_input.send_keys("Am1221221A")

# Acsess to next auto 
next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/main/div/div[4]/form/div/input[13]')))   
next_button.click()

 
# my all feature
your_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/header/div/div[2]/div[3]/deferred-side-panel/include-fragment/react-partial-anchor/button/span/span/img')))   
your_button.click()


# click to your profile 
your_profile = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, ' /html/body/div[4]/div/div/div/div[2]/div/ul/li[3]/a/div/span')))   
your_profile.click()


# create repo
create_repo = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a/span[1]')))   
create_repo.click()


# new repo
new_repo = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[5]/main/div/div/div[2]/turbo-frame/div/div[1]/div/div/a')))   
new_repo.click()



# input name repo 
repo_name_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[5]/main/react-app/div/form/div[3]/div[1]/div[1]/div[1]/fieldset/div/div[2]/div/span/input'))
)
repo_name_element.click()


# Wait for the repository name input field to be visible, then enter the name
repo_name_input = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[5]/main/react-app/div/form/div[3]/div[1]/div[1]/div[1]/fieldset/div/div[2]/div/span/input'))
)
repo_name_input.send_keys(input("Enter repository name: "))
time.sleep(1)


# Wait for the README file button to be clickable, then click it
README_file_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id=":rm:"]'))
)
README_file_element.click()



# Wait for the submit button to be clickable, then click it
submit_repo_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[5]/main/react-app/div/form/div[5]/button/span/span'))
)
submit_repo_element.click()


try:
       while True:
        pass     
except KeyboardInterrupt:
    driver.quit()


