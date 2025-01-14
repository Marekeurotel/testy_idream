from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")

service = Service('/usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=service)
##driver = webdriver.Chrome(options=options)

driver.get("https://idream.pl")
driver.maximize_window()

search_box = WebDriverWait(driver, 1).until(
    EC.visibility_of_element_located((By.NAME, "q"))
)
search_box.send_keys("słuchawki")
search_box.send_keys(Keys.RETURN)

time.sleep(3)

driver.quit()

