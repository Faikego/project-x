import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from browser_helpers import browser_init
from constants import *


def parser_nix(target):
    '''
    Функция по поиску искомого в никсе
    Парсит все достижимые для него ценники в словарь (Название+ценник) и выбирает наименьшую сумму
    Принимает название товара
    Возвращает пару сумма+имя
    :param target:
    :return:
    '''
    try:
        driver = browser_init('https://www.nix.ru')
        element = driver.find_element(By.CSS_SELECTOR, css_search_nix)
        element.send_keys(target)
        element = driver.find_element(By.CSS_SELECTOR, css_search_button_nix).click()
        time.sleep(5)
        element = driver.find_element(By.CSS_SELECTOR,css_sorter_button_nix).click()
        time.sleep(0.3)
        price_list = driver.find_elements(By.CSS_SELECTOR,css_price_list_nix)
        price=price_list[3].text
        name = driver.find_element(By.CSS_SELECTOR,css_name_nix).text
        unsorted_links=driver.find_elements(By.CSS_SELECTOR, css_link_nix)
        link = unsorted_links[0].get_attribute('href')
        text = (
                    "НАЗВАНИЕ ТОВАРА-" + str(name) +
                    "\nЦЕНА-" + str(price) +
                    "\nМАГАЗИН-" + str('Никс') +
                    "\nССЫЛКА- " + str(link)
            )
    except NoSuchElementException:
        driver.close()
        text=''
        return text
    return text,price

if __name__ == '__main__':
    print(parser_nix('LOGITECH G435'))
