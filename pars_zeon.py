from datetime import time
import time

from browser import browser_init
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from Css import *


def parser_zeo(target):
    browser = browser_init('https://zeon18.ru')
    try:
        time.sleep(2)
        browser.find_element(By.CSS_SELECTOR, css_city).click()
        browser.find_element(By.CSS_SELECTOR, css_my_city).click()
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
        text = (f'Название товара: {name}\n'
                f'Ссылка на товар: {link}\n'
                f'Цена товара: {price}')
        browser.close()

    except NoSuchElementException:
        browser.close()
        return 'товар не найден'

    return text


if __name__ == '__main__':
    print(parser_zeo('LOGITECH G435'))
