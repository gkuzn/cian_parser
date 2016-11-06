# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 03:11:18 2016
@author: Artem
получить данные из "основного блока" информации 
"""
import requests
import re
def html_stripper(text):
    return re.sub('<[^<]+?>', '', str(text))
from bs4 import BeautifulSoup

link_number=49362529
flat_url = 'http://www.cian.ru/sale/flat/' + str(link_number) + '/'
flat_page = requests.get(flat_url)
flat_page = flat_page.content
flat_page = BeautifulSoup(flat_page, 'lxml')
#Выдаёт не один элемент, а сразу небольшой словарь с переменными
def many_get(flat_page):
    #в sth (от англиского something) содержится много того, что нам нужно
    sth = flat_page.find('table', attrs={'class':'object_descr_props flat sale'})
    sth = html_stripper(sth)
    sth_list=sth.split('\n')
    sth_list = list(filter(None, sth_list))
    #print(sth_list)
    dic={}
    for i in range( len (sth_list)-1 ) :
        if sth_list[i]=='Тип дома:':
            New=sth_list[i+1]
            if 'новост' in New:
                dic['New']=1
            elif 'втор' in New:
                dic['New']=0
            if 'ирпич' in New:
                dic['Brick']=1
            else:
                dic['Brick']=0
    for i in range( len (sth_list)-1 ) :
        if sth_list[i]=='Общая площадь:':
            Totsp=sth_list[i+1]
            if  Totsp!='–':
                Totsp = Totsp.replace('\xa0м2','')
                Totsp = Totsp.replace(',','.')
                dic['Totsp']=float(Totsp)
            
    
    for i in range( len (sth_list)-1 ) :
        if sth_list[i]=='Жилая площадь:':
            Livesp=sth_list[i+1]
            if Livesp!='–':    
                Livesp = Livesp.replace('\xa0м2','')
                Livesp = Livesp.replace(',','.')
                dic['Livesp']=float(Livesp)
            
    for i in range( len (sth_list)-1 ) :
        if sth_list[i]=='Площадь кухни:':
            Kitsp=sth_list[i+1]
            Kitsp = Kitsp.replace('\xa0м2','')
            Kitsp = Kitsp.replace(',','.')
            if Kitsp!='–':
                Kitsp = Kitsp.replace('\xa0м2','')
                Kitsp = Kitsp.replace(',','.')
                dic['Kitsp']=float(Kitsp)
    for i in range( len (sth_list)-1 ) :
        if sth_list[i]=='Балкон:':
            Bal=sth_list[i+1]
            if Bal=='нет':
                dic['Bal']=0
            elif '1' in Bal:
                dic['Bal']=1
            else:
                dic['Bal']=Bal
    for i in range( len (sth_list)-1 ) :
        if sth_list[i]=='Этаж:':
            fl2=sth_list[i+1]
            fl_list=fl2.split('\xa0/\xa0')
            dic['Floor']=int(fl_list[0])
            if len(fl_list)==2:
                dic['Nfloor']=int(fl_list[1])
    for i in range( len (sth_list)-1 ) :
        if sth_list[i]=='Лифт:':
            Lift=sth_list[i+1]
            Lift=sth_list[i+1]
            if Lift=='нет':
                dic['Lift']=0
            elif '1' in Lift:
                dic['Lift']=1
            elif '2' in Lift:
                dic['Lift']=1
            else:
                dic['Lift']=Lift            


    for i in range( len (sth_list)-1 ) :
        if sth_list[i]=='Ремонт:':
            Remont=sth_list[i+1]
            dic['Remont']=Remont
    for i in range( len (sth_list)-1 ) :
        if sth_list[i]=='Телефон:':
            Tel=sth_list[i+1]
            if Tel=='да':
                dic['Tel']=1
            elif   Tel=='нет':
                dic['Tel']=0    
    
    return dic
        
        
#print(many_get(flat_page))
