import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help='Specify language. En by default')

@pytest.fixture(scope='function')
def browser(request):
    language = request.config.getoption('language')
    print('\nstarting browser for tests')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print('\nquitting browser')
    browser.quit()
