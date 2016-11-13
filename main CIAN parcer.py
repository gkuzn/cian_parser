# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 14:56:42 2016
@author: Artem
"""
import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
import time
#Библиотека содержит
import get_data_dic
import distr
#Вывод на экран текущего времени (час, мин)
localtime = time.localtime(time.time())
print ("Local current time :", localtime[3:5])
#Ссылкы на первую страницу выдачи при поиске
#квартир из определенного района при поиске квартир из ЦАО
cent = 'http://www.cian.ru/cat.php?deal_type=sale&district%5B0%5D=13&district%5B1%5D=14&district%5B2%5D=15&district%5B3%5D=16&district%5B4%5D=17&district%5B5%5D=18&district%5B6%5D=19&district%5B7%5D=20&district%5B8%5D=21&district%5B9%5D=22&engine_version=2&offer_type=flat&p={}&room1=1&room2=1&room3=1&room4=1&room5=1&room6=1'
sev=    'http://www.cian.ru/cat.php?deal_type=sale&district%5B0%5D=23&district%5B1%5D=24&district%5B10%5D=33&district%5B11%5D=34&district%5B12%5D=35&district%5B13%5D=36&district%5B14%5D=37&district%5B15%5D=38&district%5B2%5D=25&district%5B3%5D=26&district%5B4%5D=27&district%5B5%5D=28&district%5B6%5D=29&district%5B7%5D=30&district%5B8%5D=31&district%5B9%5D=32&engine_version=2&offer_type=flat{}&room1=1&room2=1&room3=1&room4=1&room5=1&room6=1&room7=1'
sev_vos='http://www.cian.ru/cat.php?deal_type=sale&district%5B0%5D=39&district%5B10%5D=49&district%5B11%5D=50&district%5B12%5D=51&district%5B13%5D=52&district%5B14%5D=53&district%5B15%5D=54&district%5B16%5D=55&district%5B1%5D=40&district%5B2%5D=41&district%5B3%5D=42&district%5B4%5D=43&district%5B5%5D=44&district%5B6%5D=45&district%5B7%5D=46&district%5B8%5D=47&district%5B9%5D=48&engine_version=2&offer_type=flat{}&room1=1&room2=1&room3=1&room4=1&room5=1&room6=1&room7=1&room9=1'
vos='http://www.cian.ru/cat.php?deal_type=sale&district%5B0%5D=56&district%5B10%5D=66&district%5B11%5D=67&district%5B12%5D=68&district%5B13%5D=69&district%5B14%5D=70&district%5B15%5D=71&district%5B1%5D=57&district%5B2%5D=58&district%5B3%5D=59&district%5B4%5D=60&district%5B5%5D=61&district%5B6%5D=62&district%5B7%5D=63&district%5B8%5D=64&district%5B9%5D=65&engine_version=2&offer_type=flat{}&room1=1&room2=1&room3=1&room4=1&room5=1&room6=1&room7=1&room9=1'
ug_vos='http://www.cian.ru/cat.php?deal_type=sale&district%5B0%5D=72&district%5B10%5D=82&district%5B11%5D=83&district%5B12%5D=327&district%5B13%5D=328&district%5B14%5D=329&district%5B15%5D=330&district%5B16%5D=331&district%5B17%5D=332&district%5B18%5D=333&district%5B19%5D=334&district%5B1%5D=73&district%5B20%5D=335&district%5B21%5D=336&district%5B22%5D=337&district%5B23%5D=338&district%5B24%5D=339&district%5B25%5D=340&district%5B26%5D=341&district%5B27%5D=342&district%5B28%5D=343&district%5B29%5D=344&district%5B2%5D=74&district%5B30%5D=345&district%5B31%5D=346&district%5B32%5D=347&district%5B3%5D=75&district%5B4%5D=76&district%5B5%5D=77&district%5B6%5D=78&district%5B7%5D=79&district%5B8%5D=80&district%5B9%5D=81&engine_version=2&offer_type=flat{}&room1=1&room2=1&room3=1&room4=1&room5=1&room6=1&room7=1&room9=1'
ug='http://www.cian.ru/cat.php?deal_type=sale&district%5B0%5D=84&district%5B10%5D=94&district%5B11%5D=95&district%5B12%5D=96&district%5B13%5D=97&district%5B14%5D=98&district%5B15%5D=99&district%5B1%5D=85&district%5B2%5D=86&district%5B3%5D=87&district%5B4%5D=88&district%5B5%5D=89&district%5B6%5D=90&district%5B7%5D=91&district%5B8%5D=92&district%5B9%5D=93&engine_version=2&offer_type=flat{}&room1=1&room2=1&room3=1&room4=1&room5=1&room6=1&room7=1&room9=1'
ug_zap='http://www.cian.ru/cat.php?deal_type=sale&district%5B0%5D=100&district%5B10%5D=110&district%5B11%5D=111&district%5B1%5D=101&district%5B2%5D=102&district%5B3%5D=103&district%5B4%5D=104&district%5B5%5D=105&district%5B6%5D=106&district%5B7%5D=107&district%5B8%5D=108&district%5B9%5D=109&engine_version=2&offer_type=flat{}&room1=1&room2=1&room3=1&room4=1&room5=1&room6=1&room7=1&room9=1'
zap='http://www.cian.ru/cat.php?deal_type=sale&district%5B0%5D=112&district%5B10%5D=122&district%5B11%5D=123&district%5B12%5D=124&district%5B13%5D=348&district%5B14%5D=349&district%5B15%5D=350&district%5B1%5D=113&district%5B2%5D=114&district%5B3%5D=115&district%5B4%5D=116&district%5B5%5D=117&district%5B6%5D=118&district%5B7%5D=119&district%5B8%5D=120&district%5B9%5D=121&engine_version=2&offer_type=flat{}&room1=1&room2=1&room3=1&room4=1&room5=1&room6=1&room7=1&room9=1'
sev_zap='http://www.cian.ru/cat.php?deal_type=sale&district%5B0%5D=125&district%5B1%5D=126&district%5B2%5D=127&district%5B3%5D=128&district%5B4%5D=129&district%5B5%5D=130&district%5B6%5D=131&district%5B7%5D=132&engine_version=2&offer_type=flat{}&room1=1&room2=1&room3=1&room4=1&room5=1&room6=1&room7=1&room9=1'

#Создаём список из гравных страниц для районов
dist_list=[cent,sev,sev_vos,vos,ug_vos,ug,ug_zap,zap,sev_zap]
#dist_list=[cent]
#X - будущий большой датасет со всеми квартирами и фичами
N=30 #число страниц, по которым мы бегаем, ища
X=[]#all data
#Цикл по всем районам. Номер района в цикле это и есть номер,
#под которым этот районом будет закодирован в конечном датасете
ID=0 #номер квартиры в датасете
for distN in range( len(dist_list) ):
    print("District  "+str(distN))
    time1 = time.localtime(time.time())
    print ("Local current time :", time1[3:5])
    #по главной ссылке находим номера страниц каждой из квартир
    #например, на нулевой итерации links - список уникальных номеров всех
    #квартир из ЦАО
    links=distr.links( dist_list[distN],N )
    #пробегаем во всем квартирам в округе
    for link in links:
        
        #словарь из фич для данной квартиры
        ind_data_dic=get_data_dic.get_data_dic (link)
        #добавляем поле District, которое зависит от района
        ind_data_dic['District']=distN
        ind_data_dic['ID']=ID
        ind_data_dic['Link']='http://www.cian.ru/sale/flat/' + str(link) + '/'
        ID+=1
        #добалвляем словарь фич для квартиры в итоговый датасет    
        X.append(ind_data_dic)
print("preparing data")
data=pd.DataFrame(X)
print ("Local current time :", localtime[3:5])
localtime = time.localtime(time.time())
print ("Local current time :", localtime[3:5])
data.to_csv("data" + str(localtime[3]) + str(localtime[4]) + ".csv")
