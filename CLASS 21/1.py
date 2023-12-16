import mysql.connector
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password=''
    )
cursor=conn.cursor()
db_name="hassan_bhai"
create_db_query=f"CREATE DATABASE IF NOT EXISTS {db_name}"

try:
    cursor.execute(create_db_query)
    print('DB BAN GAYA')
except mysql.connector.Error as error:
    print(f"Error in Creating db {error}")
finally:
    cursor.close()
    conn.close()
    
    
    
    
    
    
    
