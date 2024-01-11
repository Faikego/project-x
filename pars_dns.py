from datetime import time
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from Css import css_search_dns, css_search_dns_click, css_product_dns, css_price_dns


def parser_dns():
    browser = webdriver.Chrome()
    browser.get('https://www.dns-shop.ru')
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, css_search_dns).send_keys('g 102')
    browser.find_element(By.CSS_SELECTOR, css_search_dns_click).click()
    product = browser.find_elements(By.CSS_SELECTOR, css_product_dns)
    link = None
    for i in product:
        link = i.get_attribute('href')
    price = browser.find_element(By.CSS_SELECTOR, css_price_dns).text

    return link, price


print(parser_dns())
