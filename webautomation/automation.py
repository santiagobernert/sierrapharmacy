from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#LINUX
#driver_path = '/home/santiago/Descargas/Midas/chromedriver'
#binary_path = '/usr/bin/brave-browser'

#WINDOWS
driver_path = '/home/santiago/Descargas/Midas/chromedriver'
binary_path = '/usr/bin/brave-browser'

options = webdriver.ChromeOptions()
options.binary_location = binary_path
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=Service(executable_path=driver_path), options=options)

driver.get("https://portal.e-courier.com/login?tenantId=YZea4lhJozkhTTQuCgB32")


driver.find_element(By.ID, 'text-input-username').send_keys('SIERRAIE')
driver.find_element(By.ID, 'text-input-password').send_keys('123456')
driver.find_element(By.CLASS_NAME, 'bp4-button-text').click()

