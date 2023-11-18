#loop w.r.t list
#number=[1,2,3,4,5]
#sqaure_number=[]
#for i in number:
    #print(i**2)
#    sqaure_number.append(i**2)
#    print(sqaure_number)
#print(sqaure_number)
    
    
#loop w.r.t dictionary





'''data=[
    {"name":"Hassan","age":25},
    {"name":"Qaseem","age":30},
    {"name":"Tauheed","age":24},
    {"name":"Ali","age":18}]


for i in data:
    print(i['name'])
#    if i['age']>=25:
#        print(i['name'],i['age'])




'''

sales_data=[
    {"product_name":"A","Category":"Food Items","Amount":500},
    {"product_name":"B","Category":"Natural Items","Amount":600},
    {"product_name":"C","Category":"Grocery Items","Amount":700},
    {"product_name":"D","Category":"Food Items","Amount":700},
    {"product_name":"E","Category":"Food Items","Amount":900},
    {"product_name":"F","Category":"Grocery Items","Amount":100},
    {"product_name":"G","Category":"Kirayana","Amount":1000},]
total_sales_category={}
for transaction in sales_data:
#    print(transaction)
    Category=transaction['Category']
    amount=transaction['Amount']
#    print(Category)
#    print(amount)
    if Category in total_sales_category:
        total_sales_category[Category]+=amount
        #print(total_sales_category[Category])
    else:
        total_sales_category[Category] = amount
        #print(total_sales_category[Category])
#print(total_sales_category.items())
#print(total_sales_category.keys())
#print(total_sales_category.values())
        
for category,amount in total_sales_category.items():
    print(category,amount)
    #print(amount)