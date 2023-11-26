import pandas as pd
def display_menu():
    print('Inventory Management System')
    print('1 - View Inventory')
    print('2 - Add Inventory')
    print('3 - Update Inventory')
    print('4 - Delete Inventory')
    print('5 - Exit')
    choice=input('Enter the input from (1 - 5):')
    return choice
def add_item():
    name=input("Enter the name of the product")
    quantity=input("Enter the quantity of the product")
    price=input("Enter the price of the product")
    try:
        df=pd.read_excel(excel_file)
    except FileNotFoundError:
        df=pd.DataFrame(columns=['Item','Quantity','Price'])
    new_item=pd.DataFrame({'Item':[name],'Quantity':[quantity],'Price':[price]})
    if df.empty:
        df=new_item
    else:
        df=pd.concat([df,new_item],ignore_index=True)
        print(df)
    df.to_excel(excel_file,index=False)
    print('Items has been stored to Inventory')
    
def remove_item():
    try:
        df=pd.read_excel(excel_file)
        print('Current Inventory')
        print(df)
        item_to_remove = input("Enter the name of the item you want to remove")
        df=df[df['Item'] != item_to_remove]
        df.to_excel(excel_file,index=False)
        print("Item is removed")
    except FileNotFoundError:
        print("No item file exist")
        

def update_item():
    try:
        df=pd.read_excel(excel_file)
        print('Current Inventory')
        print(df)
        item_to_update=input('Enter the name of the item you want ot update')
        quantity=int(input('Enter the updated Quantity'))
        price=int(input('Enter the updatd Price'))
        df.loc[df['Item']==item_to_update,['Quantity','Price']]=[quantity,price]
        df.to_excel(excel_file,index=False)
        print('Item is Updated')
    except FileNotFoundError:
        print('Inventory File not found')
def view_inventory():
    try:
        df=pd.read_excel(excel_file)
        print("Current Inventory")
        print(df)
    except FileNotFoundError:
        print('Inventory File not found')
        

excel_file='Inventory.xlsx'
while True:
    choice=display_menu()
    
    if choice=='1':
        view_inventory()
    elif choice=='2':
        add_item()
    elif choice=='3':
        update_item()
    elif choice=='4':
        remove_item()
    elif choice=='5':
        print('Exiting the Inventory Management System . Tata')
        break
    else:
        print('Enter the Right Number')
        
        
        
        
        
#update_item()

#remove_item()

#add_item()
    

    


    