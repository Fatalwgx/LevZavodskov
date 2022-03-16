from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/redirect_accept.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_class_name('trollface.btn.btn-primary')
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    element1 = browser.find_element_by_id('input_value')
    x = calc(element1.text)
    element2 = browser.find_element_by_id('answer')
    element2.send_keys(x)
    button = browser.find_element_by_class_name('btn.btn-primary')
    button.click()
    
finally:
    time.sleep[5]
    browser.quit