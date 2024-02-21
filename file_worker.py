def list_separator(list):
    list = str(list)
    true_list=[]
    counter = 0
    for i in list:
        #counter = counter +1
        if i == "\n":
            print(counter)
            true_list.append(list[counter:list.index(i)])
            print(list)
            counter=list.index(i)
            list.pop(counter)
    print(true_list,counter)
    return true_list
list_separator('+\nСмартфон Infinix HOT 30i NFC 4 / 128Gb < X669D > Black (1.6GHz, 4Gb, 6.56"1612x720 IPS, 4G+WiFi+BT, 128Gb+microSD, 13+0.08Mpx)\nЕСТЬ\n10 366 10 912')