###get_data_from_page_PART2.py
import requests
import re
def html_stripper(text):
    return re.sub('<[^<]+?>', '', str(text))
from bs4 import BeautifulSoup

link_number=151450772
flat_url = 'http://www.cian.ru/sale/flat/' + str(link_number) + '/'
flat_page = requests.get(flat_url)
flat_page = flat_page.content
flat_page = BeautifulSoup(flat_page, 'lxml')

#Выдаёт не один элемент, а сразу небольшой словарь с переменными
def add_feat(dic,sth_list, sub_head, key):
    for i in range( len (sth_list)-1 ) :
        if sth_list[i]==sub_head:
            New=sth_list[i+1]
            dic[key]=New
    

def many_get(flat_page):
    #в sth (от англиского something) содержится много того, что нам нужно
    sth = flat_page.find('table', attrs={'class':'object_descr_props flat sale'})

    sth = html_stripper(sth)
    sth_list=sth.split('\n')
    sth_list = list(filter(None, sth_list))
    #for el in sth_list:
        #print(el)
    dic={}
    add_feat(dic,sth_list, sub_head='Тип дома:', key='Home_type')
    add_feat(dic,sth_list, sub_head='Тип продажи:', key='Sales_type')
    add_feat(dic,sth_list, sub_head='Высота потолков:', key='Roof_hight')
    add_feat(dic,sth_list, sub_head='Балкон:', key='Balcony')
    add_feat(dic,sth_list, sub_head='Лифт:', key='Lift')
    add_feat(dic,sth_list, sub_head='Ремонт:', key='Remont')
    add_feat(dic,sth_list, sub_head='Телефон:', key='Tel')
    add_feat(dic,sth_list, sub_head='Совмещенных санузлов:', key='WC')
    add_feat(dic,sth_list, sub_head='Вид из окна:', key='View')
    add_feat(dic,sth_list, sub_head='Сдача ГК:', key='Sdacha_GK')
    add_feat(dic,sth_list, sub_head='Парковка:', key='Parking')
    
    add_feat(dic,sth_list, sub_head='Год постройки:', key='Built_year')

            
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
        if sth_list[i]=='Этаж:':
            fl2=sth_list[i+1]
            fl_list=fl2.split('\xa0/\xa0')
            dic['Floor']=int(fl_list[0])
            if len(fl_list)==2:
                dic['Nfloor']=int(fl_list[1])
    
    return dic
        
#print( pd.DataFrame({'q':many_get(flat_page)}))