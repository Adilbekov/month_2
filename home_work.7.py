import sqlite3
bd = sqlite3.connect("hv.db")
cursor = bd.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS products (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               product_title VARCHAR (200) NOT NULL,
               price DOUBLE (10,2) NOT NULL DEFAULT 0.0,
               quantity INTEGER NOT NULL
);""")
#функция чтобы добовлять
def add_product(product_title, price, quantity):
    cursor.execute('INSERT INTO products (product_title, price, quantity) VALUES (?, ?, ?)', (product_title, price, quantity))
    bd.commit()

# функция для удаление по айди
def delete_product(product_id):
    cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
    bd.commit()

# доп дз
def product_100():
    cursor.execute('SELECT * FROM products WHERE price < 100')
    products = cursor.fetchall()
    for product in products:
        print(f'все продукты дешевле 100 сомов\nID: {product[0]}, Название: {product[1]}, Цена: {product[2]}, Количество: {product[3]}')


# add_product('Яблоко', 150.0, 20)
# add_product('Банан', 200.0, 10)
# add_product('Мандарин', 50.0, 5)
# delete_product(1)
# delete_product(3)

# доп дз
product_100()


bd.close()