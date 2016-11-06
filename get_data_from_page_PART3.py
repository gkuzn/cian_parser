# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 03:11:18 2016
@author: Artem
"""
import requests
import re
def html_stripper(text):
    return re.sub('<[^<]+?>', '', str(text))
from bs4 import BeautifulSoup
#получить минисловарь со временем до метро и способом добраться до метро
link_number=149031368
flat_url = 'http://www.cian.ru/sale/flat/' + str(link_number) + '/'
flat_page = requests.get(flat_url)
flat_page = flat_page.content
flat_page = BeautifulSoup(flat_page, 'lxml')
#Выдаёт не один элемент, а сразу словарь из двух элементов
def metro(flat_page):
    #в sth (от англиского something) содержится много того, что нам нужно   
    sth = flat_page.find('span', attrs={'class':'object_item_metro_comment'})
    #print(sth)
    #print('########')
    sth = html_stripper(sth)
    dic={}
    #print(sth)
    sth_list=sth.split('\n')
    sth_list = list(filter(None, sth_list))
    #print(sth_list)
    Metrdist = re.findall('\d+', sth)
    if len(Metrdist)==1:
        dic['Metrdist'] = int( Metrdist[0] )
    if 'пешком'in sth:
        dic['Walk']=int(1)
    if 'машин' in sth:
        dic['Walk']=int(0)
    return dic        
#print(metro(flat_page))
