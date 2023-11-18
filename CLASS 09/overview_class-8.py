customer_data={
    "customer_id":[1,2,3,4,5,6],
    "name":["Qaseem","Hasan","Hasaan","Oun","Ambreen","Ali"],
    "age":[20,30,40,50,60,70],
    "purchase_amount":[100,200,300,400,500,700],    
    }
dollar_amount=278.40
#customer_data['purchase_amount']=[amount*dollar_amount for amount in customer_data['purchase_amount']]
    

#dollar=278
#customer_data['purchase_amount']=[amount*dollar for amount in customer_data['purchase_amount']]
#print(customer_data)
'''threshold=400

big_spenders={
    "customer_id":[],
    "name":[],
    "age":[],
    "purchase_amount":[]
    }


for new in range(len(customer_data['customer_id'])):
    if customer_data['purchase_amount'][new]>threshold:
        for key in big_spenders:
            big_spenders[key].append(customer_data[key][new])
print("Big spenders data :", big_spenders)
        
        '''
        
#a=[1,2,3,4,5]
#b=[6,7,7,8,9]
data_one={
    "a":1,
    "b":2
    } 
data_two={
    "c":3,
    "d":4
    }
data_merge=({**data_one,**data_two})
data_merge.update({"d":8})
print(data_merge)



