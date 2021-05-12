from flask import Flask, request,render_template,Response
from flask_pymongo import PyMongo
app = Flask(__name__)
app.config['MONGO_URI']="mongodb://localhost:27017/myDatabase"
mongo=PyMongo(app)

@app.route('/',methods=['GET','POST'])
def index(seller=None):
    if request.method=='POST':
        seller = request.form['seller']
    return render_template('index.html',seller=seller)
@app.route('/<name>')
def name(name):
    return "Hellp"+name
if __name__=='_main_':
    app.run(debug=True)