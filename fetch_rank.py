import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from datetime import datetime
import csv

# Automatically install ChromeDriver if needed
chromedriver_autoinstaller.install()

# Use the default ChromeDriver path from chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

website = 'https://leetcode.com/u/username/'

options = webdriver.ChromeOptions()
options.add_argument("--window-position=-2400,-2400")

# chromedriver_autoinstaller will handle  the path.
service = Service()

driver = webdriver.Chrome(service=service, options=options)

driver.get(website)

# Wait until the rank element is visible (instead of using time.sleep)
rank = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[contains(@class, 'ttext-label-1') and contains(@class, 'font-medium')]"))
)

# with open("log.txt", "a") as log:
#     log.write(f"{datetime.now()} , RANK = {rank.text.strip()}: Ran successfully\n")

# Save to CSV
filename = "rank_history.csv"
today = datetime.now().strftime('%d-%m-%Y')
today_general = datetime.now()   # to test exactly time ...

# Append to CSV file
file_exists = os.path.exists(filename)
with open(filename, 'a', newline='') as f:
    writer = csv.writer(f)
    if not file_exists:
        writer.writerow(["Date", "Rank"])
    writer.writerow([today, rank.text])
    writer.writerow([today_general, rank.text]) # to test exactly time ...

driver.quit()
