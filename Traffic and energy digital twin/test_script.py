from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import pandas as pd

driver = webdriver.Chrome()
driver.get("file:///path/to/your/html/file.html")
refresh_button = driver.find_element(By.ID, "refresh-button")
data_display = driver.find_element(By.ID, "data-display")

ActionChains(driver).click(refresh_button).perform()
sleep(2)  
updated_data = data_display.text
is_data_updated = "Traffic:" in updated_data and "Energy:" in updated_data
report_data = [
    {"Test": "Data Refresh", "Expected": "Data updates in 2 seconds", "Actual": updated_data, "Pass": is_data_updated}
]
df = pd.DataFrame(report_data)
df.to_excel("acceptance_criteria_results.xlsx", index=False)
driver.quit()
print("Test completed. Report generated as 'acceptance_criteria_results.xlsx'")
