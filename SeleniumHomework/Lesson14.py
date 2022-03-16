from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    element = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'),'$100'))
    button = browser.find_element_by_class_name('btn.btn-primary')
    button.click()
    element1 = browser.find_element_by_id('input_value')
    x = calc(element1.text)
    element2 = browser.find_element_by_id('answer')
    element2.send_keys(x)
    button1 = browser.find_element_by_id('solve')
    button1.click()

finally:
    time.sleep(12)
    browser.quit()