import sqlite3

db = 'first_db.sqlite'

def create_table():
    with sqlite3.connect(db) as connection: # Context manager automatically commits
        connection.execute('CREATE TABLE IF NOT EXISTS products (id int, name text)')
    connection.close()

def insert_example_data():
    with sqlite3.connect(db) as connection:
        connection.execute('INSERT INTO products values (1000, "hat")')
        connection.execute('INSERT INTO products values (1001, "jacket")')
    connection.close()

def display_all_data():
    connection = sqlite3.connect(db)
    results = connection.execute('SELECT * FROM products')
    print('All products: ')
    for row in results:
        print(row) # Each row is a tuple object
    
    connection.close()

def display_one_product(product_name):
    connection = sqlite3.connect(db)
    results = connection.execute('SELECT * FROM products WHERE name like ?', (product_name,))
    first_row = results.fetchone()
    if first_row:
        print('Your product is: ', first_row)
    else:
        print('Not found')
    connection.close()

def create_new_product():
    new_id = int(input('enter new id: '))
    new_name = input('enter new name: ')

    with sqlite3.connect(db) as connection:
        connection.execute(f'INSERT INTO products VALUES (?, ?)', (new_id, new_name)) # Using paramaters, neater, safer

    connection.close()

def update_product():
    updated_product = 'wool hat'
    updated_id = 1000
    with sqlite3.connect(db) as connection:
        connection.execute('UPDATE products SET name = ? WHERE id = ?', (updated_product, updated_id))

def delete_product(product_name):
    with sqlite3.connect(db) as connection:
        connection.execute('DELETE from PRODUCTS WHERE name = ?', (product_name,))


create_table()
insert_example_data()
display_all_data()
display_one_product('jacket')
create_new_product()
update_product()
delete_product('jacket')
display_all_data()