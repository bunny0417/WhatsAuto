from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def read_phone_numbers(file_path):
    with open(file_path, 'r') as file:
        phone_numbers = file.readlines()
    return [number.strip() for number in phone_numbers]


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")  


driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get("https://web.whatsapp.com/")
    
    
    while True:
        is_logged_in = driver.find_elements(By.CSS_SELECTOR, "img[src='https://static.whatsapp.net/rsrc.php/v3/y6/r/wa669aeJeom.png']")
        if is_logged_in:
            print("Login successful")
            break
        print("Waiting for login...")
        time.sleep(10)

    
    element_to_click_1 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "._ajv2 > span:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)")))
    element_to_click_1.click()
    
    element_to_click_2 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div._alzb:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)")))
    element_to_click_2.click()

    
    phone_numbers = read_phone_numbers('phone_numbers.txt')
    
    active_element = driver.switch_to.active_element
    
    for number in phone_numbers:
        active_element.send_keys(number)
        time.sleep(8)
        active_element.send_keys("\n")  

finally:
    print("Script execution completed. Press Enter to close the browser.")
    input()  
    driver.quit()  
