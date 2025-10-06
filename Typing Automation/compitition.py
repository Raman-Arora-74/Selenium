import os, time, random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

TEST_URL = "https://10fastfingers.com/typing-test/english"# Enter the Link You want If it is advance english simple or any compition if not so this code won't work 
PROFILE_DIR = r""  # persistent profile folder

# ---------------- DRIVER ----------------
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
    opts.add_argument(f"--user-data-dir={PROFILE_DIR}")  # persistent login

    # Anti-detection
    opts.add_experimental_option("excludeSwitches", ["enable-automation"])
    opts.add_experimental_option("useAutomationExtension", False)
    opts.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": "Object.defineProperty(navigator,'webdriver',{get:()=>undefined});"
    })
    return driver

# ---------------- WORDS ----------------
def get_current_row_words(driver):
    row = driver.find_element(By.ID, "row1")
    spans = row.find_elements(By.TAG_NAME, "span")
    return [(s.get_attribute("textContent") or "").strip() for s in spans if (s.get_attribute("textContent") or "").strip()]

# ---------------- HUMAN-LIKE TYPING ----------------
def type_like_human(input_field, word, base_delay):
    for ch in word:
        input_field.send_keys(ch)
        time.sleep(random.uniform(base_delay * 0.4, base_delay * 0.6))

    if random.random() < 0.02:  # small typo + correction
        input_field.send_keys("x")
        input_field.send_keys(Keys.BACKSPACE)

    input_field.send_keys(Keys.SPACE)

    if random.random() < 0.1:  # micro pause
        time.sleep(random.uniform(0.6,0.7))

# ---------------- TYPING TEST ----------------
def do_typing_test(driver):


        driver.get(TEST_URL)

        input_field = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "inputfield"))
        )
        input_field.click()

    # Pick random speed between 120–135
        target_wpm = random.randint(120, 135)

        cps = (target_wpm * 5) / 60.0
        base_delay = 1.0 / cps
        print(f"⌨️ Typing at ~{target_wpm} WPM (delay {base_delay:.3f}s/char)")

        end = time.time() + 70
        while time.time() < end:
            for w in get_current_row_words(driver):
                type_like_human(input_field, w, base_delay)
                if time.time() > end:
                    break

        print("✅ Typing finished.")

# ---------------- MAIN ----------------
if __name__ == "__main__":
    d = build_driver()
    try:
        do_typing_test(d)
        time.sleep(5)
    finally:
        d.quit()
