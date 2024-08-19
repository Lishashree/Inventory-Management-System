from inventory import add_item, update_item, delete_item, view_items
from database import connect

def main_menu():
    print("Inventory Management System")
    print("1. Add Item")
    print("2. Update Item")
    print("3. Delete Item")
    print("4. View All Items")
    print("5. Exit")

def add_item_flow():
    name = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))
    add_item(name, quantity, price)
    print(f"Added {name} to inventory.")

def update_item_flow():
    item_id = int(input("Enter item ID to update: "))
    name = input("Enter new item name: ")
    quantity = int(input("Enter new quantity: "))
    price = float(input("Enter new price: "))
    update_item(item_id, name, quantity, price)
    print(f"Item ID {item_id} updated.")

def delete_item_flow():
    item_id = int(input("Enter item ID to delete: "))
    delete_item(item_id)
    print(f"Item ID {item_id} deleted.")

def view_items_flow():
    items = view_items()
    for item in items:
        print(f"ID: {item[0]}, Name: {item[1]}, Quantity: {item[2]}, Price: ${item[3]}")

if __name__ == "__main__":
    connect()
    while True:
        main_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            add_item_flow()
        elif choice == '2':
            update_item_flow()
        elif choice == '3':
            delete_item_flow()
        elif choice == '4':
            view_items_flow()
        elif choice == '5':
            break
        else:
            print("Invalid option. Please choose again.")
