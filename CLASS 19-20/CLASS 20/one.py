import mysql.connector 
#database connections info
host_name='localhost'
user_name='root'
password_one=''
database_name='dataanalytics'
#establishing connection
connection=mysql.connector.connect(
    host=host_name,
    user=user_name,
    password=password_one,
    database=database_name
    )

#creating a cursor object to execute sql queries
cursor=connection.cursor()
x="""CREATE TABLE `principal` (
  `id` int(11) NOT NULL, 
  `name` varchar(55) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `grade` float DEFAULT NULL
)
""" 
cursor.execute(x)



y="""INSERT INTO `principal` (`id`, `name`, `age`, `grade`) VALUES
('1', 'Qaseem Bhai', 21, 95.7),
('2', 'Ambreeen Baji', 22, 67.6),
('3', 'Danish Bhai', 24, 79)"""
cursor.execute(y)
connection.commit()
print('execute')
 


