import pytest
from selene import browser
from selenium.webdriver import FirefoxOptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    print("preparing settings for the code executing")
    browser.config.driver_options = FirefoxOptions()
    browser.config.base_url = 'https://demoqa.com'
    browser.config.timeout = 6.0
    browser.config.window_width = 1900
    browser.config.window_height = 950

    # driver_options.add_argument('--headless') #=new

    yield

    browser.quit()
