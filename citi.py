from datetime import time
import time
from selenium.webdriver.common.by import By
from browser_helpers import browser_init
from selenium.webdriver.common.keys import Keys
from constants import *
from selenium.common.exceptions import NoSuchElementException

def parser_citi (target):
    '''
    Функция по поиску нужного товара в Ситилинке,
    Принимает запрос с названием товара
    Возвращает название товара и его ценник
    :param target:
    :return:
    '''
    try:
        driver = browser_init('https://www.citilink.ru')
        element = driver.find_element(By.CSS_SELECTOR,css_search_citi)
        element.click()
        time.sleep(0.2)
        element.send_keys(target)
        time.sleep(0.2)
        element.send_keys(Keys.ENTER);
        time.sleep(2)
        element=driver.find_element(By.XPATH,xpath_sort_button_citi).click()
        time.sleep (2)
        price=driver.find_element(By.XPATH,xpath_price_citi).text
        name=driver.find_element(By.XPATH,xpath_name_citi).text
        unsorted_links=driver.find_elements(By.XPATH,xpath_links_citi)
        for i in unsorted_links:
            link = i.get_attribute('href')
        text = (
                "НАЗВАНИЕ ТОВАРА-" + str(name) +
                "\nЦЕНА-" + str(price) +
                "\nМАГАЗИН-" + str('Ситилинк') +
                "\nССЫЛКА- " + str(link)
        )
    except NoSuchElementException:
        driver.close()
        text=''
        return text
    return text
