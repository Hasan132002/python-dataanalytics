   import pandas as pd
import os
import qrcode

def display_pos_menu():
    print("\nPoint of Sale (POS) System")
    print("1. Make a Sale")
    print("2. Exit POS")
    choice = input("Enter your choice (1 or 2): ")
    return choice

def  make_sale(excel_file):
    try:
        df=pd.read_excel(excel_file)
        print("Current Inventory")
        print(df)
        customer_name = input("Enter the name of the Customer : ")
        item_to_sale=input("Enter the name of the Item that customer wants : ")
        
        item_details=df[df['Item']==item_to_sale]
        if  not item_details.empty:
            quantity_sold=int(input("Enter Quantity Sold"))
            df.loc[df['Item']==item_to_sale,'Quantity']-=quantity_sold
            df.to_excel(excel_file,index=False)
            sales_data={
                "Customer Name":customer_name,
                "Item":item_to_sale,
                "Quantity Sold":quantity_sold
                }
            if os.path.exists(sales_file):
                sales_df=pd.read_csv(sales_file) if os.path.exists(sales_file) else pd.DataFrame()
                sales_df=pd.concat([sales_df,pd.DataFrame([sales_data])],ignore_index=True)
#                sales_df=sales_df.append(sales_data,ignore_index=True)


            else:
                sales_df=pd.DataFrame([sales_data])
            sales_df.to_csv(sales_file,index=False)
                
            qr_code = f"Customer Name  : {customer_name}\nItem : {item_to_sale}\n Quantity : {quantity_sold}"
            generate_qr_code(qr_code,customer_name)
            print("Sales Recorded QR Code Generated fo the Customer")
        else:
            print("Item Inventory Not Found")
    except FileNotFoundError:
        print("Bhai file hi nahi ha")
def generate_qr_code(data,customer_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")

    qr_folder = 'qr_codes'
    if not os.path.exists(qr_folder):
        os.makedirs(qr_folder)

    qr_filename = f'{qr_folder}/{customer_name}_qr.png'
    qr_img.save(qr_filename)

excel_file = 'inventory.xlsx'
sales_file='sales.csv'

while True:
    pos_choice=display_pos_menu()
    if pos_choice=='1':
        make_sale(excel_file)
    elif pos_choice=='2':
        print('Khatam tata bye bye')
        break
    else:
        print("Invalid choice 1 ya 2 likh bhai")
    
    











