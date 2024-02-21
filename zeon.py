from datetime import time
import time
from browser_helpers import browser_init
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from constants import *


def parser_zeo(target):
    '''
    Функция по поиску нужного товара в магазине зеон
    Принимает название товара
    Возвращает связку название+цена+ссылка
    :param target:
    :return:
    '''
    browser = browser_init('https://zeon18.ru')
    try:
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR, css_search_zeon).send_keys(target)
        browser.find_element(By.CSS_SELECTOR, css_search_zeon_click).click()
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR, css_sort_zeon).click()
        browser.find_element(By.XPATH, xpath_sort_zeon).click()
        time.sleep(1)
        product = browser.find_elements(By.CSS_SELECTOR, css_product_zeon)
        link = None
        for i in product:
            link = i.get_attribute('href')
        price = browser.find_element(By.CSS_SELECTOR, css_price_zeon).text
        name = browser.find_element(By.CSS_SELECTOR, css_product_zeon).text
        browser.close()
        text = (
                "НАЗВАНИЕ ТОВАРА-" + str(name) +
                "\nЦЕНА-" + str(price) +
                "\nМАГАЗИН-" + str('Зеон') +
                "\nССЫЛКА- " + str(link)
        )
    except NoSuchElementException:
        browser.close()
        text=''
        return text

    return text


if __name__ == '__main__':
    print(parser_zeo('LOGITECH G435'))