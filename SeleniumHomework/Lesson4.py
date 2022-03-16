from selenium import webdriver
import time

link = 'http://suninjuly.github.io/huge_form.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    elements = browser.find_elements_by_tag_name('input')
    for element in elements:
        element.send_keys('Answer')
    button = browser.find_element_by_class_name('btn-default')
    button.click()

except Exception as error:
    print(f'Error occures, traceback: {error}')

finally:
    time.sleep(30)
    browser.quit()