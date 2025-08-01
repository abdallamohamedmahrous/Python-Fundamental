from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.youtube.com/")
driver.maximize_window()
try:  
#       auto sign in
   sign_in: WebElement = driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[3]/div[2]/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div/div[2]')
   sign_in.click()
#       auto email
   email_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="identifierId"]'))
    )
   email_input.send_keys("test01154775040@gmail.com")

#       auto next
   next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="identifierNext"]/div/button/span'))
    )   
   next_button.click()
#       auto password
   password_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))
    )
   password_input.send_keys("Am1234567")
#       auto next
   next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="passwordNext"]/div/button/span'))
    )
   next_button.click()

   script="alert('Abdalla Mohamed')"
   driver.execute_async_script(script)
   while True:
        pass     
except KeyboardInterrupt:
    driver.quit()

