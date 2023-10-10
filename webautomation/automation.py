from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#LINUX
#driver_path = '/home/santiago/Descargas/Midas/chromedriver'
#binary_path = '/usr/bin/brave-browser'

#WINDOWS
# driver_path = 'E:/Programacion/sierrapharmacy/webautomation/chromedriver.exe'
binary_path = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe'


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.binary_location = binary_path
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=Service(), options=options)

driver.get("https://portal.e-courier.com/")

def place_order(name, sex, phone, cell, address, apartment, addr2, city, state, zip, e_mail, stop_notes, order_reference, delivery_option):
    try:
        driver.switch_to.new_window('tab')
        driver.get("https://portal.e-courier.com/login?tenantId=YZea4lhJozkhTTQuCgB32")
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "text-input-username")
        ))
        driver.find_element(By.ID, 'text-input-username').send_keys('SIERRAIE')
        driver.find_element(By.ID, 'text-input-password').send_keys('ALWAYS')
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, '//span[text()="Log in"]').click()
        driver.find_element(By.XPATH, '//a[@href="/place-order"]').click()
        driver.find_elements(By.CLASS_NAME, 'ant-picker-input')[1].click()
        actions = Actions(driver);
        actions.moveToElement(driver.find_elements(By.CLASS_NAME, 'ant-picker-time-panel-column')[0].find_elements(By.CLASS_NAME, 'ant-picker-time-panel-cell')[4].find_element(By.CLASS_NAME, 'ant-picker-time-panel-cell-inner')).perform()
        driver.find_elements(By.CLASS_NAME, 'ant-picker-time-panel-column')[1].find_elements(By.CLASS_NAME, 'ant-picker-time-panel-cell')[0].find_element(By.CLASS_NAME, 'ant-picker-time-panel-cell-inner').click()
        driver.find_elements(By.CLASS_NAME, 'ant-picker-time-panel-column')[2].find_elements(By.CLASS_NAME, 'ant-picker-time-panel-cell')[1].find_element(By.CLASS_NAME, 'ant-picker-time-panel-cell-inner').click()
        driver.find_element(By.ID, 'stops.1.Name').send_keys(name)
        driver.find_element(By.ID, 'stops.1.Address').send_keys(address)
        driver.find_element(By.ID, 'stops.1.Building').send_keys(apartment)
        driver.find_element(By.ID, 'stops.1.City').send_keys(city)
        driver.find_element(By.ID, 'stops.1.Zip').send_keys(zip)
        driver.find_element(By.ID, 'stops.1.Notes').send_keys(stop_notes)
        driver.find_element(By.ID, 'stops.1.Phone').send_keys(cell if cell else phone)
        driver.find_element(By.ID, 'stops.1.Email').send_keys(e_mail)
        driver.find_element(By.XPATH, "//div[@class='Select_optionLabel__vVOLn' and text()='NextDay']").click()
        driver.find_element(By.XPATH, f"//div[@class='Select_optionLabel__vVOLn' and text()='{delivery_option}']").click()
        driver.find_element(By.ID, 'input-order-reference-0').send_keys(order_reference)
    except Exception as e:
        print(e)

place_order("PEREZ, FLORA", "F", "(909) 444-3434", "(909) 111-3434", "9338 LOMITA DR", '', '', 'Rancho Cucamonga', 'CA', '91701', '', 'Stop notes', 'order reference', 'NextDayAM')