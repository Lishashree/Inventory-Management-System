from database import execute_query, fetch_query

def add_item(name, quantity, price):
    query = "INSERT INTO inventory (name, quantity, price) VALUES (?, ?, ?)"
    execute_query(query, (name, quantity, price))

def update_item(item_id, name, quantity, price):
    query = "UPDATE inventory SET name = ?, quantity = ?, price = ? WHERE id = ?"
    execute_query(query, (name, quantity, price, item_id))

def delete_item(item_id):
    query = "DELETE FROM inventory WHERE id = ?"
    execute_query(query, (item_id,))

def view_items():
    query = "SELECT * FROM inventory"
    return fetch_query(query)
