from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongo', 27017)

db = client.flask_db
wishlist = db.wishlist

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form['title']
        price = request.form['price']
        wishlist.insert_one({'title': title, 'price': price})
        return redirect(url_for('index'))

    wished_items = wishlist.find()
    return render_template('index.html', wished_items=wished_items)