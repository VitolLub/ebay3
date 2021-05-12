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
import datefinder
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
            return False
    else:
        return True

def start(itemId):
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Contrfor item,k in example_list:ol-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
        }
    url = "https://offer.ebay.com/ws/eBayISAPI.dll?ViewBidsLogin&item="+itemId
    r = requests.get(url)
    #print(r.content)
    soup = BeautifulSoup(r.content, 'lxml')
    arr_quntiry=[]
    res_quantity = soup.findAll('td',{"class":"contentValueFont","align":"middle"})
    for q in res_quantity:
        try:
            #print(q.text)
            arr_quntiry.append(q.text)
        except:
            pass
    res_date = soup.findAll('td',{"class":"contentValueFont"})
    dada_arr = []
    arr = []
    for result in res_date :
        date_time_str = result.text

        if fin_in_string(date_time_str)==False:
            print(date_time_str)
            print(fin_in_string(date_time_str))
            try:
                #print(date_time_str)
                aa = parse(date_time_str, fuzzy_with_tokens=True)
                print('Correct')
                #print(aa[0])
                if is_date(aa[0].strftime('%m/%d/%Y')) == True:
                    arr.append(aa[0].strftime('%m/%d/%Y'))
            except:
                pass

    print(arr)
    print(len(arr))
    print(arr_quntiry)
    print(len(arr_quntiry))
    acc={}
    print('ddd')
    for da in range(0,len(arr)):
        print(arr[da])
        dda = str(arr[da])
        try:
            print('try')
            print(arr_quntiry[da])
            acc[arr[da]]+=int(arr_quntiry[da])
        except:
            print('try2')
            print(arr_quntiry[da])
            acc[arr[da]]= int(arr_quntiry[da])
    print(acc)
    print(len(acc))

import ebaysdk
from ebaysdk.finding import Connection as finding
#arr  stock
itemId = []
title=[]
globalId=[]
galleryURL=[]
viewItemURL=[]
storeNme = []
storeUrl=[]
money_type=[]
money_vlue=[]
api = finding(siteid='EBAY-US', appid='LubomirV-devbattl-PRD-9b058513b-91c210eb', config_file=None)
api.execute('findItemsIneBayStores', {
    'keywords': 'mask',
    'storeName' : 'smarttree66',
    'outputSelector': 'StoreInfo',
    'paginationInput': {
        'entriesPerPage': '100',
        'pageNumber':1
    }
})
import json
dictstr = api.response_dict()
ack = dictstr.get('ack')
if ack=='Success':

    totalPages = dictstr.get('paginationOutput').get('totalPages')
    print('totalPages='+totalPages)
    totalEntries = dictstr.get('paginationOutput').get('totalEntries')
    for i in range(len(dictstr.get('searchResult').get('item'))):
        itemId.append(dictstr.get('searchResult').get('item')[i].get('itemId'))
        title.append(dictstr.get('searchResult').get('item')[i].get('title'))
        globalId.append(dictstr.get('searchResult').get('item')[i].get('globalId'))
        galleryURL.append(dictstr.get('searchResult').get('item')[i].get('galleryURL'))
        viewItemURL.append(dictstr.get('searchResult').get('item')[i].get('viewItemURL'))
        storeNme.append(dictstr.get('searchResult').get('item')[i].get('storeInfo').get('storeName'))
        storeUrl.append(dictstr.get('searchResult').get('item')[i].get('storeInfo').get('storeURL'))
        money_type.append(dictstr.get('searchResult').get('item')[i].get('sellingStatus').get('currentPrice').get('_currencyId'))
        money_vlue.append(dictstr.get('searchResult').get('item')[i].get('sellingStatus').get('currentPrice').get('value'))

print(itemId)
print(title)
print(globalId)
print(galleryURL)
print(viewItemURL)
print(storeNme)
print(storeUrl)
print(money_type)
print(money_vlue)
for item in range(0,2):
    start(itemId[item])

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

#start(itemId)