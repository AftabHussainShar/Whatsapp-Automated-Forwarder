from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-geolocation")
chrome_options.add_argument("--disable-features=Geolocation")
service = Service()
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
from time import time, sleep

driver.get("https://web.whatsapp.com")


id_file = "ids.txt"
group2 = "TEST2" # Group 1
group1 = "TEST" # Group 2

def repeat():
    sourceGroupSelector = driver.find_elements(By.CSS_SELECTOR, '//div[@class="_amje _aotl"]')
    if len(sourceGroupSelector) > 0:
        sourceGroupSelector[0].click()

    if len(sourceGroupSelector) > 0:
        sleep(5)
        all_rows = driver.find_elements(By.XPATH, '//div[@class="_amjv _aotl"]')
        with open(id_file, "a+") as file:
            file.seek(0)
            existing_ids = set(file.read().splitlines())  
            for i, item in enumerate(all_rows, start=1):
                if id not in existing_ids:
                    try:
                        download_button = item.find_element(By.CSS_SELECTOR, '//div[@class="_amjv we"]')
                        download_button.click()
                    except:
                        print("No download button found")
                    sleep(5)        
                    try:
                        forward_button = item.find_element(By.CSS_SELECTOR, '//div[@class="_amjv ho"]')
                        forward_button.click()
                        time.sleep(3)
                    except:
                        print("No forward button found")
                    sleep(3)
                    try:
                        targetGroupSelector = driver.find_elements(By.CSS_SELECTOR,'//div[@class=" ta"]')
                        targetGroupSelector[0].click()
                    except:
                        print("No group button found")
                    sleep(3)        
                    try:
                        send_button = driver.find_element(By.CSS_SELECTOR, 'span[data-icon="send"]')
                        send_button.click()
                        print('Forwarded')
                    except:
                        print("No download button found")
                        
                    file.write(id + "\n")
                    # repeat()
                    
while True:
    repeat()
