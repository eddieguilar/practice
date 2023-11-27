import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# Click for JS Alert
driver.find_element(by=By.XPATH, value="//button[contains(text(),'Click for JS Alert')]").click()
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
alert.accept()  # clicks "positive" Ok
# alert.dismiss() clicks on "negative" ie Cancel

# Click for JS Confirm
driver.find_element(by=By.XPATH, value="//button[contains(text(),'Click for JS Confirm')]").click()
alert = driver.switch_to.alert
alert.dismiss()
time.sleep(5)

# Click for JS Prompt

driver.find_element(by=By.XPATH, value="//button[contains(text(),'Click for JS Prompt')]").click()
prompt = driver.switch_to.alert
prompt_text = prompt.text
name = "Eddie A"
prompt.send_keys(name)
prompt.accept()
print(name)
text_displayed = driver.find_element(by=By.XPATH, value="//p[contains(text(), 'Eddie')]").text[-7:] #learn about slicing
assert name == text_displayed
pass
