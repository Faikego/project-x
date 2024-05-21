import statistics
def avg_null_destroyer (destroyer_list):
    '''
    Функция по получению средней цены из списка с предварительным удалением None из листа
    Возвращает список цен и среднюю цену на таргет
    :param destroyer_list:
    :return:
    destroyer_list,avg_price
    '''
    while None in destroyer_list:
        destroyer_list.remove (None)
    avg_price=statistics.mean(destroyer_list)
    return destroyer_list,avg_price

#def sql_appender(item,avg_price,price_list):


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


