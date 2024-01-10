from datetime import time
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from Css import (css_search_zeon, css_search_zeon_click, css_product_zeon,
                 css_price_zeon, css_sity, css_mysity)


def parser():
    browser = webdriver.Chrome()
    browser.get('https://zeon18.ru')
    time.sleep(1)

    browser.find_element(By.CSS_SELECTOR, css_sity).click()
    browser.find_element(By.CSS_SELECTOR, css_mysity).click()

    browser.find_element(By.CSS_SELECTOR, css_search_zeon).send_keys('g 102')
    browser.find_element(By.CSS_SELECTOR, css_search_zeon_click).click()

    product = browser.find_elements(By.CSS_SELECTOR, css_product_zeon)

    link = None

    for i in product:
        link = i.get_attribute('href')

    price = browser.find_element(By.CSS_SELECTOR, css_price_zeon).text

    return link, price


print(parser())
