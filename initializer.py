from zeon import parser_zeo
from citi import parser_citi
from nix import parser_nix
from center import parser_center


def initializer(target):
    text = []
    kc = parser_center(target)
    zeo = parser_zeo(target)
    cit = parser_citi(target)
    nix = parser_nix(target)

    if kc is not None:
        text += kc
    if zeo is not None:
        text += kc
    if cit is not None:
        text += kc
    if nix is not None:
        text += kc

    return text


if __name__ == '__main__':
    print(initializer('LOGITECH G435'))


