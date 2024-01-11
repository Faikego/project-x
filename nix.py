from datetime import time
import time
from selenium.webdriver.common.by import By
from browser_helpers import browser_init


# def browser_init ():
#     '''
#     Временная функция, удалить после "Слияния"
#     :return:
#     '''
#
#     service = Service(executable_path='chromedriver\chromedriver.exe')
#     options = webdriver.ChromeOptions()
#     options.add_argument('--headless')
#     driver = webdriver.Chrome(service=service)
#     driver.implicitly_wait(50)
#     driver.get('https://www.nix.ru')
#     return driver

def nix_search_and_select(target):
    '''
    Функция по поиску искомого в никсе, парсит все достижимые для него ценники в словарь (Название+ценник) и выбирает наименьшую сумму
    Возвращает пару сумма+имя
    :param target:
    :return:
    '''
    driver = browser_init('https://www.nix.ru')
    counter = 0
    price_lib=[]
    element = driver.find_element(By.CSS_SELECTOR, '#textfield')
    element.send_keys(target)
    element = driver.find_element(By.CSS_SELECTOR, '#search_button').click()
    time.sleep(2)
    element_library = driver.find_elements (By.CSS_SELECTOR,'#search_results')
    for i in element_library:
        counter=counter+1
        #print(i.find_element(By.CSS_SELECTOR,'#search_results > tbody > tr:nth-child(5)').text)
        #price_lib.append(i.find_element(By.CSS_SELECTOR,'#search_results > tbody > tr:nth-child('+str(counter)+') > td:nth-child(6)').text)
        print(counter)
        print(i.text)
    return False

target='infinix'
nix_search_and_select(driver,target)