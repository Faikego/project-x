
import time

from browser import browser_init
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from Css import *


def parser_rbt():
    browser = browser_init(https_rbt)
    browser.find_element(By.CSS_SELECTOR, css_search_rbt).send_keys('Клавиатура проводная Logitech K120 for Business (920-002522)')
    browser.find_element(By.CSS_SELECTOR, css_search_rbt_click).click()
    time.sleep(1)
    try:
        browser.find_element(By.CSS_SELECTOR, css_lower_price).click()
        browser.find_element(By.CSS_SELECTOR, css_lower_price_click).click()
        product = browser.find_elements(By.CSS_SELECTOR, css_product_zeon)
        link = None
        for i in product:
            link = i.get_attribute('href')
        price = browser.find_element(By.CSS_SELECTOR, css_price_rbt).text
        return link, price
    except NoSuchElementException:
        return "Товар не найден"


if __name__ == '__main__':
    print(parser_rbt())
