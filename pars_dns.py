from datetime import time
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from Css import xpath_search_dns, xpath_search_dns_click, xpath_product_dns, test


browser = webdriver.Chrome()
browser.get('https://www.dns-shop.ru')
time.sleep(1)

browser.find_element(By.CSS_SELECTOR, xpath_search_dns).screenshot()
# browser.find_element(By.XPATH, xpath_search_dns).send_keys('g 102')
# browser.find_element(By.XPATH, xpath_search_dns_click).click()

# product = browser.find_elements(By.XPATH, xpath_product_dns)
#
# link = None
#
# for i in product:
#     link = i.get_attribute('href')
#
# return link



