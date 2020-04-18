from flask import Flask, render_template
from flask import request, redirect
app = Flask(__name__)
import sqlite3  
conn = sqlite3.connect('myshop.db')
import sqlite_test as mydb

@app.route("/")
def hello():
    title = 'Shop Website'
    conn = sqlite3.connect('myshop.db')
    mydb.listProducts(conn, 'price < 10000')
    pds = mydb.getProducts(conn)
    
    return render_template('shop.html', title = title, products = pds)