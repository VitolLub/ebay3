#findItemsIneBayStores
#GetItems
#GetItemTransaction
from lxml import html,etree
from bs4 import BeautifulSoup
import requests
from datetime import datetime
from dateutil.relativedelta import *
from dateutil.easter import *
from dateutil.rrule import *
from dateutil.parser import *
from datetime import *
from pymongo import MongoClient

import datefinder
client = MongoClient('mongodb+srv://vitol:vitol486070920@ebay.elcsu.mongodb.net/test?retryWrites=true&w=majority')
db = client['ebay']
def is_date(string, fuzzy=False):
    """
    Return whether the string can be interpreted as a date.

    :param string: str, string to check for date
    :param fuzzy: bool, ignore unknown tokens in string if True
    """
    try:
        parse(string, fuzzy=fuzzy)
        return True

    except ValueError:
        return False
def fin_in_string(string):
    input_string = string
    # a generator will be returned by the datefinder module. I'm typecasting it to a list. Please read the note of caution provided at the bottom.
    matches = list(datefinder.find_dates(input_string))

    if len(matches) > 0:
        # date returned will be a datetime.datetime object. here we are only using the first match.
        date = matches[0]
        if input_string.find("$")==-1:
            print('Date is correct')
            return False
    else:
        return True


#
# import ebaysdk
# from ebaysdk.finding import Connection as finding
# #arr  stock
# full_data=[]
# itemId = {}
# title={}
# globalId={}
# galleryURL={}
# viewItemURL={}
# storeNme = {}
# storeUrl={}
# money_type={}
# money_vlue={}
#
# api = finding(siteid='EBAY-US', appid='LubomirV-devbattl-PRD-9b058513b-91c210eb', config_file=None)
# api.execute('findItemsIneBayStores', {
#     'keywords': 'mask',
#     'storeName' : 'smarttree66',
#     'outputSelector': 'StoreInfo',
#     'paginationInput': {
#         'entriesPerPage': '100',
#         'pageNumber':1
#     }
# })
# import json
# dictstr = api.response_dict()
# ack = dictstr.get('ack')
# if ack=='Success':
#
#     totalPages = dictstr.get('paginationOutput').get('totalPages')
#     print('totalPages='+totalPages)
#     totalEntries = dictstr.get('paginationOutput').get('totalEntries')
#     for i in range(0,5):
#         itemId['itemId'] = dictstr.get('searchResult').get('item')[i].get('itemId')
#         itemId['title'] = dictstr.get('searchResult').get('item')[i].get('title')
#         itemId['globalId']= dictstr.get('searchResult').get('item')[i].get('globalId')
#         # galleryURL.append(dictstr.get('searchResult').get('item')[i].get('galleryURL'))
#         # viewItemURL.append(dictstr.get('searchResult').get('item')[i].get('viewItemURL'))
#         # storeNme.append(dictstr.get('searchResult').get('item')[i].get('storeInfo').get('storeName'))
#         # storeUrl.append(dictstr.get('searchResult').get('item')[i].get('storeInfo').get('storeURL'))
#         # money_type.append(dictstr.get('searchResult').get('item')[i].get('sellingStatus').get('currentPrice').get('_currencyId'))
#         # money_vlue.append(dictstr.get('searchResult').get('item')[i].get('sellingStatus').get('currentPrice').get('value'))
#         full_data.append(itemId)
# print(full_data)
# for item in range(0,2):
#     start(itemId[item])

# print(dictstr.get('searchResult').get('item')[0].get('itemId'))
# itemId=dictstr.get('searchResult').get('item')[0].get('itemId')
# print('Item len')
# print(len(dictstr.get('searchResult').get('item')))
# print(dictstr.get('searchResult').get('item')[0].get('title'))
# print(dictstr.get('searchResult').get('item')[0].get('globalId'))
# print(dictstr.get('searchResult').get('item')[0].get('galleryURL'))
# print(dictstr.get('searchResult').get('item')[0].get('viewItemURL'))
# print(dictstr.get('searchResult').get('item')[0].get('storeInfo').get('storeName'))
# print(dictstr.get('searchResult').get('item')[0].get('storeInfo').get('storeURL'))
# print(dictstr.get('searchResult').get('item')[0].get('sellingStatus').get('currentPrice').get('_currencyId'))
# print(dictstr.get('searchResult').get('item')[0].get('sellingStatus').get('currentPrice').get('value'))

#start('313527610431')

import requests
import uuid
from concurrent.futures import ThreadPoolExecutor, as_completed
import random
url_list = ['313444098146', '313520982536', '313490841654', '313525085398', '313527712889', '313457798277', '313484480949', '313296827343', '313521939841', '313459268269', '313534904396', '313484563222', '313157057206', '313528720210', '313315906377', '313508573596', '313509839559', '313426035212', '313490940381', '313485766538', '313486685950', '313535841976', '313397872123', '313518119913', '313498853275', '313533274112', '313522065700', '313518159531', '313455501994', '313442725060', '313516957279', '313400240768', '313509866352', '313317355571', '313540445632', '313430771008', '313404934994', '313407276048', '313469877538', '313518276440', '313512495086', '313273512292', '313460542511', '313499992591', '313329850133', '313487380502', '313428047227', '313406454785', '313540251689', '313444789629']


def save_item_quantity(item_id_list,seller):
    url = "https://offer.ebay.com/ws/eBayISAPI.dll?ViewBidsLogin&item=" + item_id_list
    # url='https://www.proxysite.com/'
    collection = db['items_quantity']
    ip_addresses = ['109.74.195.4:80', '138.201.2.120:3128', '138.68.165.154:8080', '61.37.223.152:8080',
                    '161.202.226.194:80', '5.252.161.48:8080', '82.99.232.18:58689']
    proxy_index = random.randint(0, len(ip_addresses) - 1)
    print(proxy_index)
    proxy = {"http": ip_addresses[proxy_index]}
    print(proxy)
    r = requests.get(url, proxies=proxy)
    print(r.status_code)
    soup = BeautifulSoup(r.content, 'lxml')
    arr_quntiry = []
    res_quantity = soup.findAll('td', {"class": "contentValueFont", "align": "middle"})
    print('Quantuty res')
    for q in res_quantity:
        try:
            # print(q.text)
            arr_quntiry.append(q.text)
        except:
            pass
    res_date = soup.findAll('td', {"class": "contentValueFont"})
    dada_arr = []
    arr = []
    print('Date res')
    for result in res_date:
        date_time_str = result.text

        if fin_in_string(date_time_str) == False:
            print(date_time_str)
            print(fin_in_string(date_time_str))
            try:
                aa = parse(date_time_str, fuzzy_with_tokens=True)
                print('Correct')
                if is_date(aa[0].strftime('%m/%d/%Y')) == True:
                    arr.append(aa[0].strftime('%m/%d/%Y'))
            except:
                pass

    print(arr)
    print(len(arr))
    print(arr_quntiry)
    print(len(arr_quntiry))
    acc = {}
    print('ddd')
    for da in range(0, len(arr)):
        print(arr[da])
        dda = str(arr[da])
        try:
            print('try')
            print(arr_quntiry[da])
            acc[arr[da]] += int(arr_quntiry[da])
        except:
            print('try2')
            print(arr_quntiry[da])
            acc[arr[da]] = int(arr_quntiry[da])
    print(acc)
    print(len(acc))
    for key in acc:
        dd = {}
        print(url.find('item='))
        res = url
        print(url[59:])
        itemId = url[59:]
        dd['itemId'] = itemId
        dd['date'] = key
        dd['quantity'] = acc[key]
        dd['storeName']=seller
        res = collection.count_documents({'itemId': itemId, 'date': key})
        if res == 0:
            collection.insert_one(dd)
def runner():
    seller='cocobabyusa'
    threads = []
    with ThreadPoolExecutor(max_workers=20) as executor:
        for url in url_list:
            threads.append(executor.submit(save_item_quantity, url,seller))

        for task in as_completed(threads):
            print(task.result())


#runner()


# all_date = {}
# collection = db['items_data']
# res = collection.find({'storeName': 'cocobabyusa'})
# item_date = res
#
# item_arr = []
# for s in item_date:
#     item_res = {}
#     item_res['itemId'] =s.get('itemId')
#     item_res['title'] =s.get('title')
#     item_res['globalId'] =s.get('globalId')
#     item_res['galleryURL'] =s.get('galleryURL')
#     item_res['viewItemURL'] =s.get('viewItemURL')
#     item_res['storeName'] =s.get('storeName')
#     item_res['storeURL'] =s.get('storeURL')
#     item_res['_currencyId'] =s.get('_currencyId')
#     item_res['value'] =s.get('value')
#
#     #print(item_res)
#     collection = db['items_quantity']
#     res_qt = collection.find({'storeName': 'cocobabyusa','itemId':s.get('itemId')})
#     qt_arr = []
#     for a in res_qt:
#         qt_res = {}
#         #print(a)
#         qt_res['id'] = a.get('itemId')
#         qt_res['date'] = a.get('date')
#         qt_res['qt'] = a.get('quantity')
#         qt_arr.append(qt_res)
#     item_res['qt_res'] = qt_arr
#     item_arr.append(item_res)
#
# print(item_arr)


from ebaysdk.finding import Connection as finding
def get_seller_data(seller):
    print('Seller name')
    print(seller)
    api = finding(siteid='EBAY-US', appid='LubomirV-devbattl-PRD-9b058513b-91c210eb', config_file=None)
    api.execute('findItemsIneBayStores', {
        'storeName': seller,
        'outputSelector': 'StoreInfo',
        'paginationInput': {
            'entriesPerPage': '100',
            'pageNumber': 1
        }
    })
    dictstr = api.response_dict()
    ack = dictstr.get('ack')
    print(ack)

get_seller_data('wx6688')
# #
# collection = db['items_quantity'] #,'items_quantity','users
# collection.drop()
# collection = db['items_data'] #,'items_quantity','users
# collection.drop()
