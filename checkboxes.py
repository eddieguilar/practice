from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://the-internet.herokuapp.com/checkboxes")


for i in range(1, 3):
    checkbox_xpath = f"//input[@type='checkbox'][{i}]"
    driver.find_element(by=By.XPATH, value=checkbox_xpath).click()
    is_selected = driver.find_element(by=By.XPATH,value=checkbox_xpath).is_selected()

print(len("checkbox_xpath"))

driver.find_element(by=By.XPATH, value="//input[@type='checkbox']").click()
driver.find_element(by=By.XPATH, value="//input[@type='checkbox']").click()




