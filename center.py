import time
from browser_helpers import browser_init
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from constants import *


def parser_center(target):
    '''
    Парсит магазин "Центр"
    Принимает название товара
    Возвращает связку название+цена+ссылка
    :param target:
    :return:
    '''
    link = None
    browser = browser_init('https://kcentr.ru')
    try:
        browser.find_element(By.CSS_SELECTOR, css_city_kc).click()
        time.sleep(0.5)
        browser.find_element(By.CSS_SELECTOR, css_search_kc).send_keys(target)
        time.sleep(0.5)
        browser.find_element(By.CSS_SELECTOR, css_search_kc_click).click()
        time.sleep(1)
        browser.execute_script("window.scrollBy(0,500)", "")
        time.sleep(3)
        browser.find_element(By.XPATH, xpath_price_min_kc).click()
        time.sleep(1)
        browser.find_element(By.XPATH, xpath_price_min_kc_click).click()
        time.sleep(1)
        product = browser.find_elements(By.CSS_SELECTOR, css_kc_link)
        for i in product:
            link = i.get_attribute('href')
        time.sleep(1)
        price = browser.find_element(By.CSS_SELECTOR, css_price_kc).text
        name = browser.find_element(By.CSS_SELECTOR, css_name_kc).text
        browser.close()
        text = (
                    "НАЗВАНИЕ ТОВАРА-" + str(name) +
                    "\nЦЕНА-" + str(price) +
                    "\nМАГАЗИН-" + str('Никс') +
                    "\nССЫЛКА- " + str(link)
            )
    except NoSuchElementException:
        browser.close()
        text=''
        return text

    return text,price


if __name__ == '__main__':
    print(parser_center('LOGITECH G435'))