import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://magento.softwaretestingboard.com/")

action = ActionChains(driver)


ele = driver.find_element(by=By.XPATH, value="//a[@id='ui-id-4']//span[contains(text(),'Women')]")
action.move_to_element(ele).perform()
ele = driver.find_element(by=By.XPATH, value="//a[@id='ui-id-9']//span[contains(text(),'Tops')]")
action.move_to_element(ele).perform()
ele = driver.find_element(by=By.XPATH, value="//a[@id='ui-id-11']//span[contains(text(),'Jackets')]")
action.move_to_element(ele).perform()
driver.find_element(by=By.XPATH, value="//a[@id='ui-id-11']//span[contains(text(),'Jackets')]").click()
time.sleep(30)
pass

