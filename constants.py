#Список селекторов для парсера Ситилинка
citi_selectors=[
    '//*[@id="__next"]/div/main/div[1]/div/div[2]/section/div[2]/div[1]/div[2]/div[2]/div/button[2]',
    '//*[@id="__next"]/div/main/div[1]/div/div[2]/section/div[2]/div[2]/div[1]/div/div[3]/div[1]/a',
    '//*[@id="__next"]/div/main/div[1]/div/div[2]/section/div[2]/div[2]/div[1]/div/div[7]/div[1]/div[2]/span/span/span[1]',
    '.css-hyxlzm'
 ]
#Список селекторов для парсера Никса
nix_selectors=[
    '#textfield',
    '#search_button',
    '.cell-price-top',
    '.cell-half-price',
    '.cell-name'
]

css_search_zeon = 'body > div.site-wrapper > div > header > div > div.site-header-menu.if-size-pc > div.site-header-menu-main > div.site-header-search > div > form > div > input'
css_search_zeon_click = 'body > div.site-wrapper > div > header > div > div.site-header-menu.if-size-pc > div.site-header-menu-main > div.site-header-search > div > form > button'
css_product_zeon = 'body > div.site-wrapper > div > div.site-content > div > div.laypart-main > div > div > div.catalog-browser-content > div > div > div > div:nth-child(1) > article > div.catalog-item-body > div.catalog-item-except-picture > div.catalog-item-info > a'
css_price_zeon = 'body > div.site-wrapper > div > div.site-content > div > div.laypart-main > div > div > div.catalog-browser-content > div > div > div > div:nth-child(1) > article > div.catalog-item-body > div.catalog-item-except-picture > div.catalog-item-shop > div.if-size-pc > div > div.catalog-item-price-main > span'
css_city = 'body > div.site-wrapper > div > header > div > div.site-header-menu.if-size-pc > div.site-header-menu-main > div.site-header-select-city-wrapper > div > div.dropdown-current.site-header-select-city-icon.with-icon-map-point > span > span'
css_my_city = 'body > div.site-wrapper > div > header > div > div.site-header-menu.if-size-pc > div.site-header-menu-main > div.site-header-select-city-wrapper > div > div.dropdown-menu > ul > li:nth-child(4) > a > span'
css_sort_zeon = 'body > div.site-wrapper > div > div.site-content > div > div.laypart-main > div > div > div.catalog-browser-header > div.catalog-browser-controls.if-size-pc > div:nth-child(1) > div > div.catalog-combobox-current.logic-dropdown-current'
xpath_sort_zeon = '/html/body/div[2]/div/div[4]/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div[2]/div/div[2]/div'

css_city_kc = '#__layout > div > div._5cc02.e23f0 > div > div.eb18d > button._730f5._9088c._573f6.db695'
css_search_kc = '#__layout > div > div.header > div.header__main._592df > div > form > div.d6199.b2d48.undefined.c4952.b7a63 > div > input'
css_search_kc_click = '#__layout > div > div.header > div.header__main._592df > div > form > button'
xpath_price_min_kc = '/html/body/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/button'
xpath_price_min_kc_click = '/html/body/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/button[5]'
css_kc_link = '#__layout > div > div:nth-child(2) > div:nth-child(2) > div > div > div.d31c1 > div._9e75e > div:nth-child(1) > div._38940 > a'
css_price_kc = '#__layout > div > div:nth-child(2) > div:nth-child(2) > div > div > div.d31c1 > div._9e75e > div:nth-child(1) > div._2694e > div._6c337 > div._4de6c > div'
css_name_kc = '#__layout > div > div:nth-child(2) > div:nth-child(2) > div > div > div.d31c1 > div._9e75e > div:nth-child(1) > div._38940 > a > span'

