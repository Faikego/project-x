import time

from browser import browser_init
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from Css import *

target = 'LOGITECH G435'


def parser_eld():
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
        name = browser.find_element(By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > div:nth-child(2) > div > div > div.d31c1 > div._9e75e > div:nth-child(1) > div._38940 > a > span').text

        browser.close()
    except NoSuchElementException:
        browser.close()
        return 'товар не найден'

    return name, link, price


if __name__ == '__main__':
    print(parser_eld())
