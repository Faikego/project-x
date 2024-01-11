from datetime import time
import time
from selenium.webdriver.common.by import By
from browser_helpers import browser_init

def citi_search_and_select (target):
    '''
    Функция по поиску нужного товара в Ситилинке, возвращает название товара и его ценник
    :param target:
    :return:
    '''
    driver = browser_init('https://www.citilink.ru')
    element = driver.find_element(By.CSS_SELECTOR,'#__next > div > header > div.fresnel-container.fresnel-lessThan-tabletL > div.css-1ck99ji.es4sr930 > div > button:nth-child(3) > span').click()
    element = driver.find_element(By.CSS_SELECTOR, '#__next > div > div.css-1c45yj0.e1p9cxpz0 > div > div.css-1ck99ji.es4sr930 > div > div > div.css-i9gxme.e10t34ck0 > form > div > div > label > input')
    element.send_keys(target)
    element = driver.find_element(By.CSS_SELECTOR, '#__next > div > div.css-1c45yj0.e1p9cxpz0 > div > div.css-1ck99ji.es4sr930 > div > div > div.css-i9gxme.e10t34ck0 > form > div > div > label > div > div > button:nth-child(2) > span').click()
    time.sleep(2)
    element = driver.find_element(By.CSS_SELECTOR,'#__next > div > main > div.app-catalog-c3ky1w.eg0q2u20 > div > div.app-catalog-1pwu1hf.ewjft870 > section > div.e12wdlvo0.app-catalog-sp8nf.e1loosed0 > div.egwx31q0.app-catalog-oig9jo.e1loosed0 > div.app-catalog-14dnwby.ehj6uxk0 > div.fresnel-container.fresnel-lessThan-tabletL > div > button').click()
    element = driver.find_element(By.CSS_SELECTOR,'#__next > div > main > div.app-catalog-c3ky1w.eg0q2u20 > div > div.app-catalog-1pwu1hf.ewjft870 > section > div.e12wdlvo0.app-catalog-sp8nf.e1loosed0 > div.egwx31q0.app-catalog-oig9jo.e1loosed0 > div.app-catalog-14dnwby.ehj6uxk0 > div.fresnel-container.fresnel-lessThan-tabletL > div > div > div > div > button:nth-child(2)').click()
    element = driver.find_element(By.CSS_SELECTOR,'#__next > div > main > div.app-catalog-c3ky1w.eg0q2u20 > div > div.app-catalog-1pwu1hf.ewjft870 > section > div.e12wdlvo0.app-catalog-sp8nf.e1loosed0 > div.egwx31q0.app-catalog-oig9jo.e1loosed0 > div.app-catalog-14dnwby.ehj6uxk0 > div.fresnel-container.fresnel-greaterThanOrEqual-tabletL > div > button:nth-child(2)')
    element.click()
    time.sleep(5)
    element = driver.find_element(By.CSS_SELECTOR, '#__next > div > main > div.app-catalog-c3ky1w.eg0q2u20 > div > div.app-catalog-1pwu1hf.ewjft870 > section > div.e12wdlvo0.app-catalog-sp8nf.e1loosed0 > div.ehanbgo0.app-catalog-1yt54f0.e1loosed0 > div:nth-child(1) > div > div > div.app-catalog-gt3vul.eyol3820 > div.app-catalog-npkzzu.e6iq6rb0 > button > span > div.app-catalog-12y5rbz.elmcou80 > span > span > span.e1j9birj0.e106ikdt0.app-catalog-175fskm.e1gjr6xo0')
    print(element.text)
target='Infinix'
citi_search_and_select(target)

