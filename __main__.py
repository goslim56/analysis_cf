import urllib
import xml.etree.ElementTree as et
import pandas as pd
from bs4 import BeautifulSoup
from itertools import count
import collection


RESULT_DIRECTORY = '__result__/crawling'


def crawling_pelicana():

    results = []

    # collection
    for page in count(start=1):
        url = 'http://www.pelicana.co.kr/store/stroe_search.html?branch_name=&gu=&si=&page=%d' % page
        html = collection.crawling(url)

        bs = BeautifulSoup(html, 'html.parser')

        tag_table = bs.find('table', attrs={'class': 'table mt20'})
        tag_tbody = tag_table.find('tbody')
        tags_tr = tag_tbody.findAll('tr')

        if len(tags_tr) == 0:
            break

        for tag_tr in tags_tr:
            strings = list(tag_tr.strings)
            name = strings[1]
            address = strings[3]
            sidogu = address.split()[:2]

            results.append((name, address) + tuple(sidogu))

    # store
    table = pd.DataFrame(results, columns=['name', 'address', 'sido', 'gungu'])

    table['sido'] = table.sido.apply(lambda v: collection.sido_dict.get(v, v))
    table['gungu'] = table.sido.apply(lambda v: collection.gungu_dict.get(v, v))

    table = table.reset_index().set_index('index')
    table.to_csv('{0}/table_pelica.csv'.format(RESULT_DIRECTORY), encoding='utf-8', mode='w', index=True)



def proc_nene(xml):
    results = []
    root = et.fromstring(xml)
    for item in root.findall('item'):
        name = item.findtext('aname1')
        sido = item.findtext('aname2')
        gungu = item.findtext('aname3')
        address = item.findtext('aname4')
        results.append((name, address, sido, gungu))

    return results


def store_nene(data):
    table = pd.DataFrame(data, columns=['name', 'address', 'sido', 'gungu'])

    table['sido'] = table.sido.apply(lambda v: collection.sido_dict.get(v, v))
    table['gungu'] = table.sido.apply(lambda v: collection.gungu_dict.get(v, v))

    table = table.reset_index().set_index('index')
    table.to_csv('{0}/table_nene.csv'.format(RESULT_DIRECTORY), encoding='utf-8', mode='w', index=True)


if __name__ == '__main__':

    # pelicana collection
    crawling_pelicana()

    # nene collection
    collection.crawling(
        url='http://nenechicken.com/subpage/where_list.asp?target_step2=%s&proc_type=step1&target_step1=%s'
            % (urllib.parse.quote('전체'), urllib.parse.quote('전체')) ,
        proc=proc_nene,
        store=store_nene)
