from flask import Flask, render_template
app = Flask(__name__)

products = {
  "sku01": { "id": "sku01", "name": "Pen", "price": 15, 'src': "https://www.montblanc.com/content/dam/rcq/mtb/18/42/70/9/1842709.png.adapt.306.306.png" },
  "sku02": { "id": "sku02", "name": "Cup", "price": 80, 'src': 'https://images.lookhuman.com/render/standard/u1HAdDDuR3DhfrYIp7QH707Tb55DvPtB/mug11oz-whi-z1-t-the-tea-is-strong-with-this-one-baby-yoda.jpg'},
  "sku03": { "id": "sku03", "name": "Notebook", "price": 25, 'src': 'https://images.samsung.com/is/image/samsung/br-notebook-expert-x20-np350xaa-kfwbr-np350xaa-kfwbr-frontovergray-108088753?$PD_GALLERY_L_JPG$'},
  "sku04": { "id": "sku03", "name": "Paper", "price": 5, 'src':'http://www.mysteryworkspl.com/wp-content/uploads/2017/07/White-paper-2.jpg'}
}

cart = [
    {'id': 'sku01', 'num': 5},
    {'id': 'sku03', 'num': 3}
]

@app.route("/")
def hello():
    title = 'Shop Website'
    subtitle = 'a shopping website...'
    price = 0
    subtotal = 0
    for item in cart:
        prod = products.get(item.get('id'))
        price += prod.get('price') * item.get('num')    
    return render_template("shop.html", title=title,
        subtitle = subtitle, products = products, cart = cart, price = price)

@app.route("/product/<id>")
def product(id):
    p = products[id]
    return render_template("product.html", product=p)