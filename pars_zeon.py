from datetime import time
import time

from browser import browser_init
from selenium.webdriver.common.by import By
from Css import *


def parser():
    browser = browser_init('https://zeon18.ru')
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, css_sity).click()
    browser.find_element(By.CSS_SELECTOR, css_mysity).click()
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, css_search_zeon).send_keys('LOGITECH G435')
    browser.find_element(By.CSS_SELECTOR, css_search_zeon_click).click()
    time.sleep(1)
    elem_hover = browser.find_element(By.CSS_SELECTOR, 'body > div.site-wrapper > div > div.site-content > div > div.laypart-main > div > div > div.catalog-browser-header.type-multisearch > div.catalog-browser-controls.if-size-pc > div:nth-child(1) > div > div.catalog-combobox-current.logic-dropdown-current')
    elem_click = browser.find_element(By.CSS_SELECTOR, 'body > div.site-wrapper > div > div.site-content > div > div.laypart-main > div > div > div.catalog-browser-header.type-multisearch > div.catalog-browser-controls.if-size-pc > div:nth-child(1) > div > div.catalog-combobox-dropdown.logic-dropdown-menu > div > div:nth-child(2) > div')

    browser.move_to_element(elem_hover)
    browser.click(elem_click)
    browser.perform()
    product = browser.find_elements(By.CSS_SELECTOR, css_product_zeon)
    link = None
    for i in product:
        link = i.get_attribute('href')
    price = browser.find_element(By.CSS_SELECTOR, css_price_zeon).text

    return link, price


print(parser())
