import pandas as pd

# Function to display menu and get user choice
def display_menu():
    print("\nInventory Management System")
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Update Item")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    return choice

# Function to view the inventory
def view_inventory():
    try:
        df = pd.read_excel(excel_file)
        print("\nCurrent Inventory:")
        print(df)
    except FileNotFoundError:
        print("Inventory file not found. Please add items first.")

# Function to add an item to the inventory
def add_item():
    name = input("Enter the name of the item: ")
    quantity = int(input("Enter the quantity: "))
    price = float(input("Enter the price per unit: "))

    try:
        df = pd.read_excel(excel_file)
    except FileNotFoundError:
        df = pd.DataFrame(columns=['Item', 'Quantity', 'Price'])

    new_item = pd.DataFrame({'Item': [name], 'Quantity': [quantity], 'Price': [price]})
    df = pd.concat([df, new_item], ignore_index=True)
    df.to_excel(excel_file, index=False)
    print(f"\nItem '{name}' added to the inventory.")

# Function to remove an item from the inventory
def remove_item():
    try:
        df = pd.read_excel(excel_file)
        print("\nCurrent Inventory:")
        print(df)

        item_to_remove = input("Enter the name of the item to remove: ")
        df = df[df['Item'] != item_to_remove]
        df.to_excel(excel_file, index=False)
        print(f"\nItem '{item_to_remove}' removed from the inventory.")
    except FileNotFoundError:
        print("Inventory file not found. No items to remove.")

# Function to update an item in the inventory
def update_item():
    try:
        df = pd.read_excel(excel_file)
        print("\nCurrent Inventory:")
        print(df)

        item_to_update = input("Enter the name of the item to update: ")
        quantity = int(input("Enter the new quantity: "))
        price = float(input("Enter the new price per unit: "))

        df.loc[df['Item'] == item_to_update, ['Quantity', 'Price']] = [quantity, price]
        df.to_excel(excel_file, index=False)
        print(f"\nItem '{item_to_update}' updated in the inventory.")
    except FileNotFoundError:
        print("Inventory file not found. No items to update.")

# Main program
excel_file = 'inventory.xlsx'

while True:
    choice = display_menu()

    if choice == '1':
        view_inventory()
    elif choice == '2':
        add_item()
    elif choice == '3':
        remove_item()
    elif choice == '4':
        update_item()
    elif choice == '5':
        print("Exiting the Inventory Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
