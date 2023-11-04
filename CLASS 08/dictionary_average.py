customer_data={
    "customer_id":[1,2,3,4,5],
    "name":["Qaseem","Hasan","Hasaan","Oun","Ambreen"],
    "age":[20,30,40,50,60],
    "purchase_amount":[100,200,300,400,500,700]
    }
#print(len(customer_data['purchase_amount']))
#purchase_amounts=customer_data['purchase_amount']
#print(purchase_amounts)
#average_purchase=sum(purchase_amounts)/len(purchase_amounts)
#print(average_purchase)

threshold=300

big_spenders={
    "customer_id":[],
    "name":[],
    "age":[],
    "purchase_amount":[]
    }


for new in range(len(customer_data['customer_id'])):
    print(new)
    if customer_data['purchase_amount'][new]>threshold:
        
        for key in big_spenders:
            big_spenders[key].append(customer_data[key][new])
print("Big spenders data :", big_spenders)
        
        
        
    




