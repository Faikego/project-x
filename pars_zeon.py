from datetime import time
import time

from browser import browser_init
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from Css import *


def parser_zeo():
    browser = browser_init('https://zeon18.ru')
    try:
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR, css_city).click()
        browser.find_element(By.CSS_SELECTOR, css_my_city).click()
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR, css_search_zeon).send_keys('LOGITECH G435')
        browser.find_element(By.CSS_SELECTOR, css_search_zeon_click).click()
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR, 'body > div.site-wrapper > div > div.site-content > div > div.laypart-main > div > div > div.catalog-browser-header > div.catalog-browser-controls.if-size-pc > div:nth-child(1) > div > div.catalog-combobox-current.logic-dropdown-current').click()
        browser.find_element(By.XPATH, '/html/body/div[2]/div/div[4]/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div[2]/div/div[2]/div').click()

        time.sleep(1)
        product = browser.find_elements(By.CSS_SELECTOR, css_product_zeon)
        link = None
        for i in product:
            link = i.get_attribute('href')
        price = browser.find_element(By.CSS_SELECTOR, css_price_zeon).text
        name = browser.find_element(By.CSS_SELECTOR, css_product_zeon).text
        browser.close()

    except NoSuchElementException:
        browser.close()
        return 'товар не найден'

    return name, link, price


if __name__ == '__main__':
    print(parser_zeo())
