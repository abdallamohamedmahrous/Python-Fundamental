from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as Ec

driver: WebDriver = webdriver.Firefox()
driver.get("https://www.youtube.com/")
sign_in: WebElement = driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[3]/div[2]/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div/div[2]')
sign_in.click()

email_input: WebElement = driver.find_element(By.XPATH, '//*[@id="identifierId"]')
email_input.send_keys('test01154775040')

next_Bottun: WebElement = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button/span')
next_Bottun.click()

password:WebElement =driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
password.send_keys('Am01154775040')

next_Bottun: WebElement = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button/span')
next_Bottun.click()


try:
       while True:
        pass     
except KeyboardInterrupt:
    driver.quit()

