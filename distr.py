from bs4 import BeautifulSoup
import requests
import re
def links(main_link,N):
    links = []
    from tqdm import tqdm
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
        #print(flat_urls)
        flat_urls_splited = re.split('/', str(flat_urls))
        #print (flat_urls[2])
        old_len =len(links)
        
        for link in flat_urls_splited:
            if (link.isdigit())& (len(link)==9):
                if link not in links:
                    links.append(link)
                    #print(link,end =' ')
        new_len =len(links)
        if old_len==new_len:
            #print('Break')
            break
    return links
    #return flat_urls_splited
