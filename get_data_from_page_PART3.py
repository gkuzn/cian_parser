#get_data_from_page_PART3.py NEW!!!
import pandas as pd
import requests
import re
def html_stripper(text):
    return re.sub('<[^<]+?>', '', str(text))
from bs4 import BeautifulSoup

link_number = 151558515
flat_url = 'http://www.cian.ru/sale/flat/' + str(link_number) + '/'
flat_page = requests.get(flat_url)
flat_page = flat_page.content
flat_page = BeautifulSoup(flat_page, 'lxml')

#Выдаёт не один элемент, а сразу небольшой словарь с переменными
def metro(flat_page,dic):
    #в sth (от англиского something) содержится много того, что нам нужно   
    # сколько миниут до метро и на машине или пешком
    sth = flat_page.find('span', attrs={'class':'object_item_metro_comment'})
    sth = html_stripper(sth)
    sth_list=sth.split('\n')
    sth_list = list(filter(None, sth_list))
    Metrdist = re.findall('\d+', sth)
    if len(Metrdist)==1:
        dic['Metro_time'] = int( Metrdist[0] )
    if 'пешком'in sth:
        dic['Walk_metro']=int(1)
    if 'машин' in sth:
        dic['Walk_metro']=int(0)
    # Станция метро
    sth = flat_page.find('a', attrs={'class':"object_item_metro_name"})
    sth = html_stripper(sth)
    dic["Metro_station"] = str(sth)
    
def add_feat4(dic,sth,spliter1,spliter2, key):
    #sth_list =str(sth).split(spliter)
    sth_list = re.split(spliter1+'|'+spliter2,sth)
    if len(sth_list)>1:
        dic[key] = sth_list[1]
    else:
        dic[key] = sth_list[0]

def many_get3(flat_page):
    #print(flat_page)
    dic ={}
    #Всякая хрень почти из подзаголовка
    sth = flat_page.find('span', attrs={'class':'object_descr_dt_added'})#.contents[1]
    sth=str(sth)
    #print(sth)
    add_feat4(dic=dic ,sth=sth ,spliter1='"deal_type": ',spliter2 = '"publication_date"',key= 'sale')
    add_feat4(dic=dic ,sth=sth ,spliter1='"publication_date": ',spliter2 = ', "id":',key= 'publication_date')
    add_feat4(dic=dic ,sth=sth ,spliter1='"is_premium":',spliter2 = '"deal_type":',key= 'is_premium')
    # Добавать ближайшую (первую в списке из ближайших) станций метро, время на способ добраться (пешком или на машине)
    metro(flat_page,dic)
    
    sth = flat_page.find('div', attrs={'class':'object_descr_text'})
    sth = html_stripper(sth)
    sth.replace('\n',' ')
    #print()
    dic['Description'] = re.sub(' +',' ',sth)
    return(dic)