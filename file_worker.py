import statistics
import psycopg2
from psycopg2 import sql
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

def sql_creator():
    '''
    Открывает соединение с базой данных
    После чего создаёт таблицу Dinfo с столбцами id, item,avg_price,price_list
    В конце закрывает соединение
    :return:
    '''
    connector= psycopg2.connect(dbname='diplom_db', user='db_user',
                        password='P@$$w0rd', host='localhost')
    cursor = connector.cursor()
    cursor.execute('CREATE table Dinfo (\n'
                   'id BIGSERIAL PRIMARY KEY,\n'
                   'item VARCHAR(50),\n'
                   'avg_price VARCHAR(50),\n'
                   'price_list VARCHAR(50);\n'
                   )
    del connector

def sql_appender (item,avg_price,price_list):
    '''
    Добавляет строки в БД
    :param item:
    :param avg_price:
    :param price_list:
    :return:
    '''
    price_list=str(price_list)
    try:
        connector = psycopg2.connect(dbname='diplom_db', user='db_user',
                                     password='P@$$w0rd', host='localhost')
    except:
        sql_creator()
    with connector.cursor() as cursor:
        connector.autocommit = True
        values = [
            (item, avg_price, price_list),
        ]
        insert = sql.SQL('INSERT INTO Dinfo (item, avg_price, price_list) VALUES {}').format(
            sql.SQL(',').join(map(sql.Literal, values))
        )
        cursor.execute(insert)
    del connector

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


