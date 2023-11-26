import pandas
data={
    'Name':['Qaseem','Hassan','Tauheed','Danish','Oun'],
    'Age':[10,20,40,50,60],
    'City':['Karachi','Islamabad','Quetta','Pehasawar','Sialkot']
    }

df=pandas.DataFrame(data)
excel_file='data.xlsx'
df.to_excel(excel_file,index=Fa  lse)
print("File has been created")
print(df)



