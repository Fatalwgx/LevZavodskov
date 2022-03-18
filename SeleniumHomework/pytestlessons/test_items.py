from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_cart_button_is_present(browser):
    browser.get(link)
    assert EC.presence_of_element_located((By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')), 'No such element'
