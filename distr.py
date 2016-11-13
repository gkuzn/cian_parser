# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 01:57:07 2016
@author: Artem
"""
from bs4 import BeautifulSoup
import requests
import re
def links(main_link,N):
    links = []
     #N число страниц при выдаче
    for page in range(1, N+1):
        #print('page      '+str(page))
        ''' format - хитрый метод, который превратит ссылку на любую страницы в ссылку
        на страницу с номером page'''
        page_url =  main_link.format('&p='+str(page))
        #print(page_url)
        #Ответ от страницы
        search_page = requests.get(page_url)
        search_page = search_page.content
        search_page = BeautifulSoup(search_page, 'lxml')

        flat_urls = search_page.findAll('div', attrs = {'ng-class':"{'serp-item_removed': offer.remove.state, 'serp-item_popup-opened': isPopupOpen}"})
        flat_urls = re.split('http://www.cian.ru/sale/flat/|/" ng-class="', str(flat_urls))

        for link in flat_urls:
            if link.isdigit():
                links.append(link)
    return links
    