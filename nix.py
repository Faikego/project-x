from datetime import time
import time
from selenium.webdriver.common.by import By
from browser_helpers import browser_init,list_normalizer



def nix_search_and_select(target):
    '''
    Функция по поиску искомого в никсе, парсит все достижимые для него ценники в словарь (Название+ценник) и выбирает наименьшую сумму
    Возвращает пару сумма+имя
    :param target:
    :return:
    '''
    driver = browser_init('https://www.nix.ru')
    element = driver.find_element(By.CSS_SELECTOR, '#textfield')
    element.send_keys(target)
    element = driver.find_element(By.CSS_SELECTOR, '#search_button').click()
    time.sleep(2)
    element = driver.find_element(By.CSS_SELECTOR,'.cell-price-top').click()
    time.sleep(0.3)
    price_list = driver.find_elements(By.CSS_SELECTOR,'.cell-half-price')
    price=price_list[3].text
    name = driver.find_element(By.CSS_SELECTOR,'.cell-name').text

    return price,name

target="Коммутатор"
min_price,min_name=nix_search_and_select(target)
print('Название-',min_name)
print('Цена-', min_price)