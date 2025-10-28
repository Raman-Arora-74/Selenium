from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
import time 
driver = webdriver.Chrome()
nameList = 'YOUR NAME HERE' 
driver.get('https://10fastfingers.com/typing-test/english/')
username = driver.find_element(By.ID,'username')
time.sleep(2)
inputText = driver.find_element(By.ID,'inputfield')
row = driver.find_element(By.ID, "row1")
spans = row.find_elements(By.TAG_NAME, "span")
for span in spans:
    inputText.send_keys(span.text) # Pass the speed do you want if you write 0.1 or something then it got speed like 1000 + which is massive
    inputText.send_keys(Keys.SPACE)
time.sleep(10)
driver.quit()