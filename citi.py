from datetime import time
import time
from selenium.webdriver.common.by import By
from browser_helpers import browser_init
from selenium.webdriver.common.keys import Keys
target='Пылесос'
def citi_search_and_select (target):
    '''
    Функция по поиску нужного товара в Ситилинке, возвращает название товара и его ценник
    :param target:
    :return:
    '''
    driver = browser_init('https://www.citilink.ru')
    #time.sleep(20)
    element = driver.find_element(By.CSS_SELECTOR,'.css-hyxlzm')
    element.click()
    time.sleep(0.2)
    element.send_keys(target)
    time.sleep(0.2)
    element.send_keys(Keys.ENTER);
    time.sleep(2)
    element=driver.find_element(By.CSS_SELECTOR,'#__next > div > main > div.app-catalog-c3ky1w.eg0q2u20 > div > div.app-catalog-1pwu1hf.ewjft870 > section > div.e12wdlvo0.app-catalog-1kzfd3s.e1loosed0 > div.egwx31q0.app-catalog-1v1smf8.e1loosed0 > div.app-catalog-14dnwby.ehj6uxk0 > div.fresnel-container.fresnel-greaterThanOrEqual-tabletL > div > button:nth-child(2)').click()
    time.sleep(0.5)
    price=driver.find_element(By.CSS_SELECTOR,'#__next > div > main > div.app-catalog-c3ky1w.eg0q2u20 > div > div.app-catalog-1pwu1hf.ewjft870 > section > div.e12wdlvo0.app-catalog-1kzfd3s.e1loosed0 > div.ehanbgo0.app-catalog-1rygk07.e1loosed0 > div:nth-child(1) > div > div > div.app-catalog-gt3vul.eyol3820 > div.app-catalog-npkzzu.e6iq6rb0 > button > span > div.app-catalog-12y5rbz.elmcou80 > span > span > span.e1j9birj0.e106ikdt0.app-catalog-56qww8.e1gjr6xo0').text
    name=driver.find_element(By.CSS_SELECTOR,'#__next > div > main > div.app-catalog-c3ky1w.eg0q2u20 > div > div.app-catalog-1pwu1hf.ewjft870 > section > div.e12wdlvo0.app-catalog-1kzfd3s.e1loosed0 > div.ehanbgo0.app-catalog-1rygk07.e1loosed0 > div:nth-child(1) > div > div > div.app-catalog-632im3.e1sv2xw70 > div.app-catalog-oacxam.e1xes8vl0').text
    return price,name
price,name=citi_search_and_select(target)
print('Название-',name)
print('Цена-',price)