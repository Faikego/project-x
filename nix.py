from datetime import time
import time
from selenium.webdriver.common.by import By
from browser_helpers import browser_init
from constants import nix_selectors


def parser_nix(target):
    '''
    Функция по поиску искомого в никсе, парсит все достижимые для него ценники в словарь (Название+ценник) и выбирает наименьшую сумму
    Принимает название товара
    Возвращает пару сумма+имя
    :param target:
    :return:
    '''
    driver = browser_init('https://www.nix.ru')
    element = driver.find_element(By.CSS_SELECTOR, nix_selectors[0])
    element.send_keys(target)
    element = driver.find_element(By.CSS_SELECTOR, nix_selectors[1]).click()
    time.sleep(5)
    element = driver.find_element(By.CSS_SELECTOR,nix_selectors[2]).click()
    time.sleep(0.3)
    price_list = driver.find_elements(By.CSS_SELECTOR,nix_selectors[3])
    price=price_list[3].text
    name = driver.find_element(By.CSS_SELECTOR,nix_selectors[4]).text
    return price , name
