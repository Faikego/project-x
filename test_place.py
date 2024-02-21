import matplotlib as mpl
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import time
import datetime
day=datetime.date.today()
day=str (day)
colon=":"
dash="-"
space=" "
t = time.localtime()
time_input=input('Через сколько времени остановится? (В секундах)')
time_input=int (time_input)
times = time_input
time_input_h=time_input/3600
time_input_h=int (time_input_h)
time_input=time_input%3600
time_input_m=time_input/60
time_input_m=int (time_input_m)
time_input=time_input%60
current_time_h = time.strftime("%H", t)
current_time_h = int (current_time_h)

current_time_m = time.strftime("%M", t)
current_time_m = int (current_time_m)

current_time_s = time.strftime("%S", t)
current_time_s = int (current_time_s)


current_time_s = current_time_s+time_input
if current_time_s >59:
    current_time_s=current_time_s-60
    current_time_m=current_time_m+1
if current_time_s<10:
    current_time_s = str(current_time_s)
    current_time_s = '0'+current_time_s
else:
    current_time_s = str (current_time_s)

current_time_m = current_time_m+time_input_m
if current_time_m >59:
    current_time_m=current_time_m-60
    current_time_h=current_time_h+1
if current_time_m<10:
    current_time_m = str(current_time_m)
    current_time_m = '0'+current_time_m
else:
    current_time_m = str (current_time_m)

current_time_h = current_time_h+time_input_h
while current_time_h > 23:
    current_time_h=current_time_h-24
if current_time_h<10:
    current_time_h = str(current_time_h)
    current_time_h = '0'+current_time_h
else:
    current_time_h = str (current_time_h)

future_time = current_time_h+colon+current_time_m+colon+current_time_s
current_time = time.strftime("%H:%M:%S", t)
print ('Время начала работы парсера-',current_time)
print ('Примерное время окончания работы парсера и получения графика-',future_time)
label=day+space+current_time+dash+future_time

i=0
url = 'https://www.rbc.ru/crypto/currency/btcusd'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('div', class_='chart__subtitle js-chart-value')
bitcoinc=[]
timesmassive=[]
while i != times :
    i=i+1
    i=float (i)
    timesmassive.append (i)
for quote in quotes:
    bitcoin = quote.text
    bitcoin = bitcoin.strip()
    bitcoin = bitcoin[:6]
    bitcoin = bitcoin.strip()
    bitcoin = bitcoin.replace(" ", "")
    bitcoin = int (bitcoin)
    print ('Изначальный курс-',bitcoin,"$")
    i=0
while i != times :
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('div', class_='chart__subtitle js-chart-value')
    time.sleep(1)
    for quote in quotes:
        TEXT=quote.text
        TEXT=TEXT.strip()
        TEXT=TEXT [:6]
        TEXT = TEXT.strip()
        TEXT = TEXT.replace(" ", "")
        TEXT = float (TEXT)
        bitcoinc.append (TEXT)


    i=i+1
dpi = 80
fig = plt.figure(dpi = dpi, figsize = (512 / dpi, 384 / dpi) )
mpl.rcParams.update({'font.size': 10})

plt.title(label)
plt.xlabel('Время в секундах')
plt.ylabel('Цена битка в долларах')

plt.plot(timesmassive, bitcoinc,  color = 'green', linestyle = 'solid',
         label = 'Биток')


plt.legend(loc = 'upper right')
fig.savefig('биток.png')

