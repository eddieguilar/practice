from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

# Adding elements
for _ in range(10):
    add_element = driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Add Element')]")
    add_element.click()

# Deleting elements
for _ in range(10):
    try:
        delete_element = driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Delete')]")
        delete_element.click()

        delete_element = WebDriverWait(driver, 10).until_not(EC.invisibility_of_element_located(delete_element))
        assert not delete_element.is_displayed()
    except (NoSuchElementException, TimeoutException):
        pass
















# deleted_element = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.XPATH,"//button[contains(text(), 'Delete')]")))
#
# deleted_element.click()
#
# assert not deleted_element.is_displayed(), "The deleted element is still displayed."
