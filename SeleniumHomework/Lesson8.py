from tkinter import Button
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/get_attribute.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    element1 = browser.find_element_by_css_selector('.form-group img[valuex]')
    valuex = element1.get_attribute('valuex')
    x = valuex
    y = calc(x)
    print(x)
    element3 = browser.find_element_by_id('answer')
    element3.send_keys(y)
    element4 = browser.find_element_by_id('robotCheckbox')
    element4.click()
    element5 = browser.find_element_by_id('robotsRule')
    element5.click()
    time.sleep(1)
    button = browser.find_element_by_class_name('btn-default')
    button.click()

finally:
    time.sleep(5)
    browser.quit()