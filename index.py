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
from ebaysdk.finding import Connection as finding
def ss(seller):
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
    print(dictstr.get('searchResult').get('item')[0].get('sellingStatus').get('sellingState'))
#ss('redstarus')
#save_item_quantity()
#save_item_quantity(item_id_list[0],'redstarus')
#get_seller_data('jacobsparts')
# #
# collection = db['items_quantity'] #,'items_quantity','users
# collection.drop()
# collection = db['items_data'] #,'items_quantity','users
# collection.remove({'storeName':'redstarus'})
# collection = db['items_quantity'] #,'items_quantity','users
# collection.remove({'storeName':'redstarus'})
date = ['2021-05-30','2021-05-29','2021-05-28','2021-05-28','2021-05-28','2021-05-27','2021-05-26','2021-05-25','2021-05-24','2021-05-23','2021-05-21']
now  = datetime.today().strftime('%Y-%m-%d')
print(now)
lst_7d = datetime.today() - timedelta(days=8)
lst_7d = lst_7d.strftime('%Y-%m-%d')
collection = db['items_quantity']
#res = collection.find({'date': {'$gte': lst_7d, '$lt': now},'storeName':'redstarus','itemId':'313405796455'})#,'storeName':'redstarus','itemId':'313405796455'
res = collection.aggregate([ { '$match': { 'date': {'$gte': lst_7d, '$lt': now},'storeName': "redstarus",'itemId':'313405796455' } },{
    '$group': {
        '_id': 'null',
        'total': {
            '$sum': '$quantity'
        }
    }
} ] )
print(res)
for a in res:
    print(a)

#print(now7)