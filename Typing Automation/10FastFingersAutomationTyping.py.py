from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
import time 
driver = webdriver.Chrome()
nameList = 'YOUR NAME HERE' 
for i in range(10):
    
    driver.get('https://10ff.net/login')
    username = driver.find_element(By.ID,'username')
    username.send_keys(':)')
    time.sleep(1)
    username.send_keys(Keys.ENTER)
    time.sleep(13)
    inputText = driver.find_element(By.TAG_NAME,'input')
    words  = driver.find_elements(By.TAG_NAME,'span')
    nameList = words[0].text
    for word in words:
        inputText.send_keys(word.text)
        time.sleep(0.4)
        inputText.send_keys(Keys.SPACE)
    time.sleep(10)
driver.quit()