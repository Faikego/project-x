from datetime import time
import time
from selenium.webdriver.common.by import By
from browser_helpers import browser_init
from selenium.webdriver.common.keys import Keys
from constants import citi_selectors
target='Смартфон iphone 13'

def parser_citi (target):
    '''
    Функция по поиску нужного товара в Ситилинке,
    Принимает запрос с названием товара
    Возвращает название товара и его ценник
    :param target:
    :return:
    '''
    driver = browser_init('https://www.citilink.ru')
    element = driver.find_element(By.CSS_SELECTOR,citi_selectors[3])
    element.click()
    time.sleep(0.2)
    element.send_keys(target)
    time.sleep(0.2)
    element.send_keys(Keys.ENTER);
    time.sleep(2)
    element=driver.find_element(By.XPATH,citi_selectors[0]).click()
    time.sleep (2)
    price=driver.find_element(By.XPATH,citi_selectors[1]).text
    name=driver.find_element(By.XPATH,citi_selectors[2]).text
    #link=driver.find_element_by_xpath("//a[@href]")
    return price , name
