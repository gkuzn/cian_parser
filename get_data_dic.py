# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 01:31:42 2016
@author: Artem
"""
#get1,2,3 - наборы фунция для получения фич из причесанной страницы
import get_data_from_page_PART1 as get1
import get_data_from_page_PART2 as get2
import get_data_from_page_PART3 as get3
#по координатам опредеояет расстояние
#до нулевого километра в километрах
import pith
import requests
import re
from bs4 import BeautifulSoup
#Берем на вход страницу
def get_data_dic(link_number):
    flat_url = 'http://www.cian.ru/sale/flat/' + str(link_number) + '/'
    #получим и причешем страницу
    flat_page = requests.get(flat_url)
    flat_page = flat_page.content
    flat_page = BeautifulSoup(flat_page, 'lxml')
    #Применяем на эту страницу функции, возвращающие значения фич
    #Все эти фичи записываем в словарь
    dic1 = {}
    dic1['Price'] = get1.Price(flat_page)
    dic1['lat'], dic1['lon'] = get1.Coords(flat_page)
    dic1['rooms'] = get1.Room(flat_page)
    #Получаем СЛОВАРЬ из фич
    dic2 = get2.many_get(flat_page)
    #Получаем СЛОВАРЬ из фич
    dic3 = get3.many_get3(flat_page)
    
    flatStats={**dic1,**dic2,**dic3}
    #Добавляем фичу "расстояние до нулевого километра в км"
    flatStats['dist']=pith.dist( flatStats['lat'],flatStats['lon'])
    return(flatStats)