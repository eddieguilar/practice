from seleniumwire import webdriver
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


# replace 'user:pass@ip:port' with your information
options = {
	'proxy': {
		'http': 'http://admin:admin@192.168.1.69:5223',
		'https': 'https://admin:admin@192.168.1.69:5223',
		'no_proxy': 'localhost,127.0.0.1'
	}
}

# replace 'your_absolute_path' with your chrome binary's aboslute path
driver = webdriver.Chrome('your_absolute_path', seleniumwire_options=options)

driver.get('https://the-internet.herokuapp.com/basic_auth')

time.sleep(8)

driver.quit()