import time

from browser import browser_init
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from Css import *


target_1 = 'Монитор MSI G274QPF'                  # 70 секунд
target_2 = 'g 102'                                    # 92 секунд
target_3 = 'удлинитель 2 метра'          # 80 секунд - не найден

city = 'Сарапул'


def parser_dns():
    start = time.time()
    browser = browser_init('https://www.dns-shop.ru')
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, css_sity_dns_click).click()
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, css_sity_search).send_keys(city)
    browser.find_element(By.CSS_SELECTOR, css_sity_search_click).click()
    time.sleep(1)
    element = browser.find_element(By.CSS_SELECTOR, css_search_dns)
    time.sleep(1)
    element.send_keys(target_2)
    search = browser.find_element(By.CSS_SELECTOR, css_search_dns_click)
    search.click()
    time.sleep(1)

    stopper_1 = 0
    stopper_2 = 0

    if stopper_1 == 0 and stopper_2 == 0:
        try:
            name = browser.find_element(By.XPATH, xpath_name_product_dns)
            time.sleep(1)
            price = browser.find_element(By.XPATH, xpath_price_dns)
        except NoSuchElementException:
            stopper_2 += 1
        else:
            name = name.text
            price = price.text
            price = price.split('₽')
            browser.close()
            stopper_1 += 1
            finish = time.time()
            res = finish - start
            return name, price[0], res

    if stopper_1 == 0 and stopper_2 == 1:
        try:
            browser.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div[2]/div[1]/div/div[1]/div[2]/a/span[2]').click()
            time.sleep(1)
            browser.find_element(By.XPATH, '/html/body/div[10]/div/label[3]/span').click()
            time.sleep(1)
            browser.find_element(By.CSS_SELECTOR, css_product_click).click()
            time.sleep(2)
            name = browser.find_element(By.XPATH, xpath_name_product_dns)
            time.sleep(1)
            price = browser.find_element(By.XPATH, xpath_price_dns)
        except NoSuchElementException:
            return 'товар не найден'
        else:
            name = name.text
            price = price.text
            price = price.split('₽')
            browser.close()
            stopper_1 += 1
            finish = time.time()
            res = finish - start
            return name, price[0], res


if __name__ == '__main__':
    print(parser_dns())


