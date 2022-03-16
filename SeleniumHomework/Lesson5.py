from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'http://suninjuly.github.io/find_xpath_form'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.TAG_NAME, 'input.form-control')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, 'last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, 'form-control.city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, value = 'country')
    input4.send_keys("Russia")
    button = browser.find_element(By.XPATH, '//button[@type=\'submit\']')
    button.click()
except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')
finally:
    time.sleep(5)
    browser.quit()
