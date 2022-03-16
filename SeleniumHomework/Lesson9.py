from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = 'http://suninjuly.github.io/selects1.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_id('num1')
    input2 = browser.find_element_by_id('num2')
    x = int(input1.text) + int(input2.text)
    print(x)
    select = Select(browser.find_element_by_tag_name('select'))
    select.select_by_visible_text(str(x))
    button = browser.find_element_by_class_name('btn.btn-default')
    button.click()
finally:
    browser.quit
