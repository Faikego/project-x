import time

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from Css import (css_search_dns, css_sity_dns_click, css_sity_search, css_sity_search_click, css_search_dns_click,
                 css_product_dns, css_price_dns)


def parser_dns():
    browser = uc.Chrome()
    browser.get('https://www.dns-shop.ru')
    time.sleep(0.3)
    browser.find_element(By.CSS_SELECTOR, css_sity_dns_click).click()
    time.sleep(0.3)
    browser.find_element(By.CSS_SELECTOR, css_sity_search).send_keys('Сарапул')
    browser.find_element(By.CSS_SELECTOR, css_sity_search_click).click()
    time.sleep(0.3)
    browser.find_element(By.CSS_SELECTOR, css_search_dns).send_keys('macbook air')
    time.sleep(0.3)
    browser.find_element(By.CSS_SELECTOR, css_search_dns_click).click()
    product = browser.find_elements(By.CSS_SELECTOR, css_product_dns)
    link = None
    for i in product:
        link = i.get_attribute('href')
    time.sleep(0.3)
    price = browser.find_element(By.CSS_SELECTOR, '#search-results > div.products-list > div > div.catalog-products.view-simple > div:nth-child(1) > div.product-buy.product-buy_one-line.catalog-product__buy > div > div.product-buy__price').text

    return link, price


print(parser_dns())


