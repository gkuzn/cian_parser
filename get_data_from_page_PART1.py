# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 00:50:56 2016
@author: Artem
"""
import requests
import re
from bs4 import BeautifulSoup
def html_stripper(text):
    return re.sub('<[^<]+?>', '', str(text))
    
#Получение цены
def Price(flat_page):
    price = flat_page.find('div', attrs={'class':'object_descr_price'})
    price = re.split('<div>|руб|\W', str(price))
    price = "".join([i for i in price if i.isdigit()][-3:])
    return int(price)
#Получение координат    
def Coords(flat_page):
    coords = flat_page.find('div', attrs={'class':'map_info_button_extend'}).contents[1]
    coords = re.split('&amp|center=|%2C', str(coords))
    coords_list = []
    for item in coords:
        if item[0].isdigit():
            coords_list.append(item)
    lat = float(coords_list[0])
    lon = float(coords_list[1])
    return lat, lon
#Получение количества комнат
def Room(flat_page):
    rooms = flat_page.find('div', attrs={'class':'object_descr_title'})
    rooms = html_stripper(rooms)
    room_number = ''
    for i in re.split('-|\n', rooms):
        if 'комн' in i:
            break
        else:
            room_number += i
    room_number = "".join(room_number.split())
    return room_number
