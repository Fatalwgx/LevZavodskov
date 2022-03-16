from ast import In
from cmath import sin
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/execute_script.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    element1 = browser.find_element(By.ID, 'input_value')
    x = calc(int(element1.text))
    footer = browser.find_element(By.TAG_NAME, 'footer')
    browser.execute_script('arguments[0].style.visibility = \'hidden\'', footer)
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(x)
    input2 = browser.find_element(By.ID, 'robotCheckbox')
    input2.click()
    input3 = browser.find_element(By.ID, 'robotsRule')
    input3.click()
    button = browser.find_element(By.CLASS_NAME, 'btn.btn-primary')
    button.click()

finally:
    time.sleep(5)
    browser.quit()

