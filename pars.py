from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://zeon18.ru')

xpath_search = '/html/body/div[2]/div/header/div/div[1]/div[1]/div[2]/div/form/div/input'

browser.find_element(By.XPATH, xpath_search).send_keys('монитор')

xpath_search_click = '/html/body/div[2]/div/header/div/div[1]/div[1]/div[2]/div/form/button'

browser.find_element(By.XPATH, xpath_search_click).click()

xpath_cat = '/html/body/div[2]/div/div[4]/div/div[2]/div/div/div[2]/div/div/div/div[1]/article/div[1]/a'

elem = browser.find_elements(By.XPATH, xpath_cat)

for i in elem:
    print(i.get_attribute('href'))


