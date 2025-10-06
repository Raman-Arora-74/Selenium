from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
driver = webdriver.Chrome()
driver.get('https://canary.discord.com/login')
try:
    email = WebDriverWait(driver,10).until(
        EC.visibility_of_element_located((By.ID,"uid_32"))
    )
    password = WebDriverWait(driver,10).until(
        EC.visibility_of_element_located((By.NAME,"password"))
    )
    # paste your email 

    email.send_keys("squidxactionwithreaction@gmail.com")
    #paste your 
    password.send_keys("465213eF")
    button = WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.XPATH,'//button[@class="marginBottom8_fd297e button__921c5 button__201d5 lookFilled__201d5 colorBrand__201d5 sizeLarge__201d5 fullWidth__201d5 grow__201d5"]'))
    )
    button.click()
    # add time to quit 
    time.sleep(5)
except Exception:
    print("No tag found")
time.sleep(100)
driver.quit()