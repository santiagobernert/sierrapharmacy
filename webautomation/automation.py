from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import sys

#LINUX
driver_path = '/home/santiago/Descargas/Midas/chromedriver'
binary_path = '/usr/bin/brave-browser'

#WINDOWS
# driver_path = 'E:/Programacion/sierrapharmacy/webautomation/chromedriver.exe'
# binary_path = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe'


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.binary_location = binary_path
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=Service(executable_path=driver_path), options=options)


def open_link_with_retries(url, max_retries=4, timeout=10):
    retries = 0
    while retries < max_retries:
        driver.get(url)
        try:
            WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((By.ID, "text-input-username"))
            )
            return True  # Page loaded successfully
        except Exception as e:
            retries += 1
            print(f"Retry {retries}")
            # Open a new tab with the same link
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[-1])
            driver.get(url)
            # Close the old tab
            driver.switch_to.window(driver.window_handles[0])
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
    driver.close()
    print(Exception("Couldn't load page"))
    return False



def wait_address_verification():
    try:
        WebDriverWait(driver, 1.5).until(
            EC.presence_of_element_located((By.XPATH, '//label[text()="Verified Address"]')
        ))
        driver.find_element(By.XPATH, '//label[text()="Verified Address"]').click()
        driver.find_element(By.XPATH, '//button[text()="Update Address"]').click()
        print("\n\nGoogle Maps verified address\n\n")
        return True
    except:
        try:
            WebDriverWait(driver, 1.5).until(
                EC.presence_of_element_located((By.XPATH, '//p[@class="css-bjux8v" and text()="Review the verification issues"]')
            ))
            driver.find_element(By.XPATH, '//button[text()="Make changes"]').click()
            print("Google maps could not verify the address, it is incorrect")
            return False
        except:
            print("Address is correct")
            return True


def place_order(name, sex, phone, cell, address, apartment, addr2, city, state, zip_code, e_mail, stop_notes, order_reference, delivery_option, time_ready):
    open_link_with_retries("https://portal.e-courier.com/login?tenantId=YZea4lhJozkhTTQuCgB32")
    try:
        #Login
        driver.find_element(By.ID, 'text-input-username').send_keys('SIERRAIE')
        driver.find_element(By.ID, 'text-input-password').send_keys('ALWAYS')
        driver.find_element(By.XPATH, '//span[text()="Log in"]').click()  
        driver.implicitly_wait(3)

        #Place order
        driver.find_element(By.XPATH, '//a[@href="/place-order"]').click()

        #Pick time
        time_ready=time_ready.split(":")
        driver.find_elements(By.CLASS_NAME, 'ant-picker-input')[1].click()
        ac = ActionChains(driver)
        ac.move_to_element(driver.find_element(By.XPATH, f'//div[@class="ant-picker-time-panel-cell-inner" and text()="{time_ready[0]}"]')).move_by_offset(1, 1).click().perform()
        ac.move_to_element(driver.find_element(By.XPATH, f'//div[@class="ant-picker-time-panel-cell-inner" and text()="{time_ready[1]}"]')).move_by_offset(1, 1).click().perform()
        ac.move_to_element(driver.find_element(By.XPATH, f'//div[@class="ant-picker-time-panel-cell-inner" and text()="{time_ready[2]}"]')).move_by_offset(1, 1).click().perform()
        driver.find_element(By.XPATH, '//button[text()="OK"]').click()
        
        #Complete address form
        driver.find_element(By.ID, 'stops.1.Name').send_keys(name)
        driver.find_element(By.ID, 'stops.1.Address').send_keys(address)
        driver.find_element(By.ID, 'stops.1.Building').send_keys(apartment)
        driver.find_element(By.ID, 'stops.1.City').send_keys(city)
        driver.find_element(By.ID, 'stops.1.Zip').send_keys(zip_code)
        driver.find_element(By.ID, 'stops.1.Notes').send_keys(stop_notes)
        driver.find_element(By.ID, 'stops.1.Phone').send_keys(cell if cell else phone)
        driver.find_element(By.ID, 'stops.1.Email').send_keys(e_mail)

        #Verify address
        driver.find_element(By.XPATH, '//label[text()="Delivery Service type"]').click()
        correct_address = wait_address_verification()
        if not correct_address:
            return False
        
        #Finish form
        driver.find_element(By.XPATH, "//div[@class='Select_optionLabel__vVOLn' and text()='NextDay']").click()
        driver.find_element(By.XPATH, f"//div[@class='Select_optionLabel__vVOLn' and text()='{delivery_option}']").click()
        driver.find_element(By.ID, 'input-order-reference-0').send_keys(order_reference)
        return True

    except Exception as e:
        print(e)

#place_order("BRIDGES, JAMES", "M", "(909) 456-7891", "(909) 111-3434", "9338 LOMITA DR c", '', '', 'Rancho Cucamonga', 'CA', '91701', '', 'Stop notes', 'Example order reference', 'NextDayAM')
