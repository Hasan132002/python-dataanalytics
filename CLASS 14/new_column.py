import pandas
excel_file='data.xlsx'
df=pandas.read_excel(excel_file) 
df['Occupation']=['Engineer','Cricketer','Busniessman','Student','Artist']
df.to_excel(excel_file,index=False)
print('DATA INSERTED')  