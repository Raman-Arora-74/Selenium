import os, time, random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
TEST_URL = "https://10fastfingers.com/anticheat/view/1/1"
PROFILE_DIR = r""  # profile to keep session
# --------------- DRIVER ----------------
def build_driver():
    # Remove old Chrome lockfile if needed
    lockfile = os.path.join(PROFILE_DIR, "SingletonLock")
    if os.path.exists(lockfile):
        try:
            os.remove(lockfile)
            print("🗑️ Removed old Chrome lockfile.")
        except Exception as e:
            print("⚠️ Could not remove lockfile:", e)


    opts = Options()
    opts.add_argument("--start-maximized")
    opts.add_argument(f"--user-data-dir={PROFILE_DIR}")
    opts.add_experimental_option("excludeSwitches", ["enable-automation"])
    opts.add_experimental_option("useAutomationExtension", False)
    opts.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": "Object.defineProperty(navigator,'webdriver',{get:()=>undefined});"
    })
    return driver


# ---------------- TYPING TEST LOGIC ----------------
def get_current_row_words(driver):
    strtext = input('Please Enter the Text : ')
    wordList = strtext.split(' ')
    return wordList

def type_like_human(input_field, word, base_delay):
    for ch in word:
        input_field.send_keys(ch)
        time.sleep(random.uniform(base_delay*0.1, base_delay*0.1))
    input_field.send_keys(Keys.SPACE)
    if random.random() < 0.1:  # small pause
        time.sleep(random.uniform(0.1, 0.1))

def do_typing_test(driver):
    driver.get(TEST_URL)
    time.sleep(40)
    strtext = input('Please Enter the Text : ')
    input_field = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "word-input"))
    )
    input_field.click()

    target_wpm = random.randint(120, 135)
    cps = (target_wpm * 5) / 60.0
    base_delay = 0.9 / cps
    print(f"⌨️ Typing at ~{target_wpm} WPM")

    wordList = strtext.split(' ')
    while True:
        for w in wordList:
            type_like_human(input_field, w, base_delay)
        break 

    print("✅ Typing finished.")
if __name__ == "__main__":
    d = build_driver()
    try:
        do_typing_test(d)
        time.sleep(5)
    finally:
        d.quit()