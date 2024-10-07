from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import time
from dotenv import load_dotenv
import os

load_dotenv('.env')

PASSWORD = os.getenv('PASSWORD')

options = Options()
options.add_argument("user-data-dir=C:\\Users\\User\AppData\\Local\\Microsoft\\Edge\\User Data\\Default")
options.add_argument(r"profile-directory=Default")

driver = webdriver.Edge(options=options)

driver.get('https://shopee.com.my/')



# time.sleep(2)

# button = driver.find_element(By.CLASS_NAME, "shopee-button-outline.shopee-button-outline--primary-reverse")
# button.click()

# input_field = driver.find_element(By.NAME, 'loginKey')
# input_field.send_keys('chai.kahchun@hotmail.com')

# password_field = driver.find_element(By.NAME, 'password')
# password_field.send_keys(PASSWORD)

# time.sleep(2)

# button_login = driver.find_element(By.CLASS_NAME, "'vvOL40.iesrPs.AsFRg8.qCI4rz.ZKayWA.AnY7KS'")
# button_login.click()

time.sleep(20)
driver.quit()