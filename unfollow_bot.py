import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
reload(sys)
sys.setdefaultencoding('utf-8')

# Initializing the headless chrome
driver = webdriver.Chrome()
driver.get("https://github.com/login")
wait = WebDriverWait(driver, 10)

# Locating username and password field
username = wait.until(EC.presence_of_element_located((By.ID, "login_field")))
password = wait.until(EC.presence_of_element_located((By.ID, "password")))

# password and username need to go into these values
username.send_keys("Username")
password.send_keys("Password")

# Clicking the sign in button
login_form = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@value='Sign in']")))
login_form.click()

prepend = ["your_username"]


for user in prepend:
    for i in range(0, 200):
        for t in range(1, 100):
            string = "https://github.com/{}/following?page={}".format(user, t)
            driver.get(string)
            time.sleep(1)

            follow_button = driver.find_elements_by_xpath("//button[@aria-label='Unfollow this person']")

            # time.sleep(1)
            # print len(follow_button)
            try:
                for i in follow_button:
                    i.submit()
            except:
                pass
            time.sleep(1)



driver.close()

time.sleep(3)

time.sleep(3)

driver.close()