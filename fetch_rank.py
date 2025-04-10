from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from datetime import datetime
import csv


website = 'https://leetcode.com/u/hassan21kh1996/'
path = r'C:\chromedriver-win64\chromedriver.exe'  # <-- use raw string or double backslashes

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)

driver.get(website)

# Wait until the rank element is visible (instead of using time.sleep)
rank = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[contains(@class, 'ttext-label-1') and contains(@class, 'font-medium')]"))
)

print(rank.text.strip())

# Save to CSV
filename = "rank_history.csv"
today = datetime.now().strftime('%d-%m-%Y')

# Append to CSV file
file_exists = os.path.exists(filename)
with open(filename, 'a', newline='') as f:
    writer = csv.writer(f)
    if not file_exists:
        writer.writerow(["Date", "Rank"])
    writer.writerow([today, rank.text])


# input("Press Enter to close...")  # ttext-label-1 dark:text-dark-label-1 font-medium

driver.quit()
