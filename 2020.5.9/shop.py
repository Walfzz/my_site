from flask import Flask, render_template
from flask import request, redirect

app = Flask(__name__)

products = {
  "sku01": { "id": "sku01", "name": "Pen", "price": 15, 'desc': 'A pen...', 'src': "https://www.montblanc.com/content/dam/rcq/mtb/18/42/70/9/1842709.png.adapt.306.306.png" },
  "sku02": { "id": "sku02", "name": "Cup", "price": 80, 'desc': 'A cup...', 'src': 'https://images.lookhuman.com/render/standard/u1HAdDDuR3DhfrYIp7QH707Tb55DvPtB/mug11oz-whi-z1-t-the-tea-is-strong-with-this-one-baby-yoda.jpg'},
  "sku03": { "id": "sku03", "name": "Notebook", "price": 25, 'desc': 'A notebook...', 'src': 'https://images.samsung.com/is/image/samsung/br-notebook-expert-x20-np350xaa-kfwbr-np350xaa-kfwbr-frontovergray-108088753?$PD_GALLERY_L_JPG$'},
  "sku04": { "id": "sku03", "name": "Paper", "price": 5, 'desc': 'A piece of paper...', 'src':'https://paper-media.com/media/image/product/3576/md/mbc-8341_motif-stationery-antique-history-old-style.jpg'}
}
mycart = {
  'sku01': 3
}

@app.route("/")
def hello():
    #title = 'Shop Website'
    
    return render_template('shop.html', products = products)

@app.route("/product/<sid>")
def productView(sid):
    pd = products[sid]
    return render_template('product2.html', product = pd)

@app.route("/cart")
def cartView():
  return render_template('cart.html', mycart = mycart, products = products)

@app.route('/add-cart/<sid>')
def addCart(sid):
  mycart[sid] = mycart.get(sid, 0) + 1
  return redirect('/cart')