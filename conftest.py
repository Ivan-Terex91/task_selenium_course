from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language please")


@pytest.fixture(scope='function')
def browser(request):
    language = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    print('\nstart browser...')
    browser = webdriver.Chrome(options=options)
    yield browser
    print('\nquit browser...')
    browser.quit()


