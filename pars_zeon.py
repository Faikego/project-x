


Хули палишь?



from datetime import time
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def parser():
    browser = webdriver.Chrome()
    browser.get('https://zeon18.ru')
    time.sleep(1)

    xpath_search = '/html/body/div[2]/div/header/div/div[1]/div[1]/div[2]/div/form/div/input'
    browser.find_element(By.XPATH, xpath_search).send_keys('Видеокарта Palit GeForce RTX 3060 Dual')

    xpath_search_click = '/html/body/div[2]/div/header/div/div[1]/div[1]/div[2]/div/form/button'
    browser.find_element(By.XPATH, xpath_search_click).click()

    xpath_cat = '/html/body/div[2]/div/div[4]/div/div[2]/div/div/div[2]/div/div/div/div[1]/article/div[1]/a'
    elem = browser.find_elements(By.XPATH, xpath_cat)

    # xpath_price = '/html/body/div[2]/div/div[4]/div/div[2]/div/div/div[2]/div/div/div/div/article/div[2]/div[2]/div[2]/div[1]/div/div[1]/span'
    price_ = browser.find_element(By.CLASS_NAME, 'value')

    price = price_.get_attribute('value')

    site = None

    for i in elem:
        site = i.get_attribute('href')

    return site, price


print(parser())
