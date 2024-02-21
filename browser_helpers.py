from selenium import webdriver
from selenium.webdriver.chrome.service import Service
def browser_init (url):
    '''
    Инициирует браузер с нужным урлом, принимает урл возвращает драйвер
    :param url:
    :return:
    '''
    service = Service(executable_path='chromedriver\chromedriver.exe')
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(50)
    driver.get(url)
    return driver
