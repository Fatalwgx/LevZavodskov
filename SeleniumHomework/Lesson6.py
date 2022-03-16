from selenium import webdriver
import time

# файл хромдрайвера находится в директории вместе с уроками, либо укажите свой путь до него

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_css_selector('.first_block .form-control.first')
    input1.send_keys('Ivan')
    # На этом месте код ловит ошибку, из-за отсутствующего блока
    input2 = browser.find_element_by_css_selector('.first_block .form-control.second')
    input2.send_keys('Ivanov')
    input3 = browser.find_element_by_css_selector('.first_block .form-control.third')
    input3.send_keys('Ivan@mail.com')


    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()