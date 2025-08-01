
#  erro code 

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
# from webdriver_manager.firefox import GeckoDriverManager


Service = FirefoxService(executable_path="./geckodriver",)
browser= webdriver.Firefox(service=Service)

browser.get('https://www.facebook.com/')
# browser.maximize_window()
# browser.quit()





