from flask import Flask, request,render_template,Response
from flask_pymongo import PyMongo
#from flask_mongoengine import MongoEngine
from pymongo import MongoClient
client = MongoClient('mongodb+srv://vitol:vitol486070920@ebay.elcsu.mongodb.net/test?retryWrites=true&w=majority')
db = client['ebay']
collection = db['users']
post = {'id':0,'title':'dfs'}
collection.insert_one(post)