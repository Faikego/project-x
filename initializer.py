from zeon import parser_zeo
from citi import parser_citi
from nix import parser_nix
from center import parser_center
from file_worker import avg_null_destroyer
def initializer (target):
    zeo_text,zeo_price=parser_zeo(target)
    nix_text,nix_price=parser_nix(target)
    citi_text,citi_price=parser_citi(target)
    center_text,center_price=parser_center(target)
    price_list=[]
    price_list.append(zeo_price,nix_price,citi_price,center_price)
    price_list,avg_price=avg_null_destroyer(price_list)
    text = (
        zeo_text+
        nix_text+
        citi_text+
        center_text
    )
    return text,price_list,avg_price


