from zeon import parser_zeo
from citi import parser_citi
from nix import parser_nix
from center import parser_center

def initializer (target):
    zeo_text=parser_zeo(target)
    nix_text=parser_nix(target)
    citi_text=parser_citi(target)
    center_text=parser_center(target)

    text = (
        zeo_text+
        nix_text+
        citi_text+
        center_text
    )
    return text


