from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/alert_accept.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_class_name('btn.btn-primary')
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    element1 = browser.find_element_by_id('input_value')
    x = calc(element1.text)
    element2 = browser.find_element_by_id('answer')
    element2.send_keys(x)
    button1 = browser.find_element_by_class_name('btn.btn-primary')
    button1.click()

finally:
    time.sleep(5)
    browser.quit()