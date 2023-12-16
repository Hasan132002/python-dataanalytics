import mysql.connector
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='principaldb'
    )
cursor=conn.cursor()
cursor.execute("INSERT INTO principal VALUES (1,'Hassan',10)")
cursor.execute("INSERT INTO student VALUES (1,'Tauheed',22,'A',1)")
conn.commit()
cursor.close()
conn.close()
