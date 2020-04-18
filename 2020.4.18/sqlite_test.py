import sqlite3  
conn = sqlite3.connect('myshop.db')

def createProductTable(conn):
    c = conn.cursor()
    sql = """
    CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    qty INTEGER NOT NULL
   )
    """
    c.execute(sql)
    conn.commit()

def insertProduct(conn, name, price, qty):
    c = conn.cursor()
    sql = """
    INSERT INTO products (name, price, qty)
    VALUES (?, ?, ?)
    """
    #c.execute(sql, ('Pen', 15, 45))
    #c.execute(sql, ('Cup', 80, 5))
    #c.execute(sql, ('Notebook', 25, 20))
    c.execute(sql, (name, price, qty))
    conn.commit()

def listProducts(conn, where):
    c = conn.cursor()
    sql = '''SELECT id, name, price, qty 
             FROM products 
             WHERE {}
          '''.format(where)
    c.execute(sql)
    products = c.fetchall()
    for pd in products:
        print(pd)

def update_product(conn, id, price, qty):  
    sql = """
        UPDATE products
        SET price = ?,
            qty = ?
        WHERE id = ?
    """
    c = conn.cursor()
    c.execute(sql, (price, qty, id))
    conn.commit()

def delete_by_id(conn, id):
    sql="""
    DELETE FROM products WHERE id = ?
    """
    c = conn.cursor()
    c.execute(sql, (id,))
    conn.commit()

def getProducts(conn):
    c = conn.cursor()
    sql = 'SELECT id, name, price, qty FROM products'
    c.execute(sql)
    products = c.fetchall()
    return products

def test():
    #insertProduct(conn, 'Stapler', 1000, 1)
    #insertProduct(conn, 'Pen', 1000000, 100)
    #insertProduct(conn, 'Nothing', 1000000000, 10)
    #insertProduct(conn, 'Ha', 1000, 100)
    #insertProduct(conn, 'Leuk', 1000, 10)
    #createProductTable(conn)
    delete_by_id(conn, 1)
    #update_product(conn, 1, 999, 100)
    listProducts(conn, 'price < 1000000')
    conn.close()

test()