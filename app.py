from flask import Flask, request,render_template,Response
from flask_pymongo import PyMongo
#from flask_mongoengine import MongoEngine
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb+srv://vitol:vitol486070920@ebay.elcsu.mongodb.net/test?retryWrites=true&w=majority')
db = client['test']


@app.route('/',methods=['GET','POST'])
def index(seller=None):
    if request.method=='POST':

        seller = request.form['seller']
        collection = db['test']
        post = {'id': 0, 'title': 'dfs'}
        collection.insert_one(post)
    return render_template('index.html',seller=seller)
@app.route('/<name>')
def name(name):
    return "Hellp"+name
if __name__=='_main_':
    app.run(debug=True)