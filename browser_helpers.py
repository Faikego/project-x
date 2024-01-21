from selenium import webdriver
from selenium.webdriver.chrome.service import Service
def browser_init (url):
    '''
    Временная функция, инициирует браузер с нужным урлом
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
def list_normalizer(list):
    '''
    Функция по переработке сырого листа в лист с тектовыми значениями
     :param list:
    :return:
    '''
    new_list=[]
    co=0
    for i in list:
        print(i.text)
        new_list.append(i.text)
        co+=1
    print(co)
    return new_list