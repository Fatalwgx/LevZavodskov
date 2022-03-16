from selenium import webdriver
import time
import os

link = 'http://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    element1 = browser.find_element_by_css_selector('input[name=\'firstname\']')
    element1.send_keys('Ivan')
    element2 = browser.find_element_by_css_selector('input[name=\'lastname\']')
    element2.send_keys('Ivanov')
    element3 = browser.find_element_by_css_selector('input[name=\'email\']')
    element3.send_keys('ivan@mail.com')
    element4 = browser.find_element_by_css_selector('input[name=\'file\']')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = os.path.join(current_dir, 'file.txt')
    element4.send_keys(file_name)
    button = browser.find_element_by_class_name('btn.btn-primary')
    button.click()

finally:
    time.sleep(5)
    browser.quit()
