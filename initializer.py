from zeon import parser_zeo
from citi import parser_citi
from nix import parser_nix
from center import parser_center

def initializer (target):
    price_list=[]
    name_list=[]
    link_list=[]
    magazine_list=['zeon','nix','citi','center']
    price,name,link=parser_zeo(target)
    price_list.append(price)
    name_list.append(name)
    link_list.append(link)
    price,name,link=parser_nix(target)
    price_list.append(price)
    name_list.append(name)
    link_list.append(link)
    price,name,link=parser_citi(target)
    price_list.append(price)
    name_list.append(name)
    link_list.append(link)
    price,name,link=parser_center(target)
    price_list.append(price)
    name_list.append(name)
    link_list.append(link)
    min_price=min(price_list)
    min_price_index=price_list.index(min_price)
    text = (
            "НАЗВАНИЕ ТОВАРА-" + str (name_list[min_price_index]) +
            "\nЦЕНА-" + str(price_list[min_price_index]) +
            "\nМАГАЗИН-" + str(magazine_list[min_price_index])+
            "\nССЫЛКА- " + str(link_list[min_price_index])
    )
    return text
print(initializer('Смартфон Iphone 13'))


