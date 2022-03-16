from tkinter import Button
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/execute_script.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    element2 = browser.find_element_by_id('input_value')
    x = element2.text
    y = calc(x)
    browser.execute_script("return arguments[0].scrollIntoView(true);")
    element3 = browser.find_element_by_id('answer')
    input1 = element3.send_keys(y)
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