from datetime import time
import time
from selenium.webdriver.common.by import By
from browser_helpers import browser_init
from selenium.webdriver.common.keys import Keys
from constants import citi_selectors
target='Смартфон iphone 13'

def citi_search_and_select (target):
    '''
    Функция по поиску нужного товара в Ситилинке,
    Принимает запрос с названием товара
    Возвращает название товара и его ценник
    :param target:
    :return:
    '''
    driver = browser_init('https://www.citilink.ru')
    #time.sleep(20)
    element = driver.find_element(By.CSS_SELECTOR,'.css-hyxlzm')
    element.click()
    time.sleep(0.2)
    element.send_keys(target)
    time.sleep(0.2)
    element.send_keys(Keys.ENTER);
    time.sleep(2)
    element=driver.find_element(By.CSS_SELECTOR,citi_selectors[1]).click()
    time.sleep(0.5)
    price=driver.find_element(By.CSS_SELECTOR,citi_selectors[2]).text
    name=driver.find_element(By.CSS_SELECTOR,citi_selectors[3]).text
    return price,name

price,name=citi_search_and_select(target)
print('Название-',name)
print('Цена-',price)