from playwright.sync_api import sync_playwright
import time 
import random 

GAME_URL = 'https://10ff.net/login'
USER_NAME = 'None'
LIST_OF_NUMBER = [1,2,3,4]
EMOJY_LIST = ["🫡","💖","🌙","💕","🤣","😪","😒","👍","😁","🚘","🥶","🫵"]
for i in range(50):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(GAME_URL)
        page.fill('input[id="username"]',USER_NAME or " ")
        page.keyboard.press('Enter')
        time.sleep(1)
        choice = random.choice(LIST_OF_NUMBER)
        page.goto('https://10ff.net')
        USER_NAME = page.locator(f'(//span)[{choice}]').text_content()
        print(f'Username ->> {USER_NAME}')
        row = page.locator('.place')
        print('We Found Div 🫡')
        words  = row.locator('span')
        count = words.count()
        print(count)
        input_box = page.locator('input')   # adjust selector if needed
        input_box.wait_for(state="visible")
        i = 1
        while True:
            if page.locator('.overlayer').text_content() != 'false':
                print(f'Time Taken : {i}')
                i += 1
                time.sleep(1)
            else:
                break
        for i in range(count):
            choiceEmojy = random.choice(EMOJY_LIST)
            page.fill('input',words.nth(i).text_content() or '')
            if i > 0 and i < 20:
                time.sleep(0.4)
            if i > 40 and i<60:
                time.sleep(0.1)
            if i > 60:
                time.sleep(0.4)
            page.keyboard.press('Space')
            print(f'{words.nth(i).text_content()} {choiceEmojy}')
        time.sleep(1)
        browser.close()    


