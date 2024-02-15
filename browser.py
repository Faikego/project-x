from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import undetected_chromedriver as uc


def browser_init(url):
    '''
    Временная функция, инициирует браузер с нужным урлом
    :param url:
    :return:
    '''
    service = Service(executable_path='chromedriver\chromedriver.exe')
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = uc.Chrome(service=service)
    driver.implicitly_wait(50)
    driver.get(url)
    return driver

