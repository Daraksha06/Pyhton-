import mysql.connector
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password='root',
    port=3306,
    database="DARAKSHA"
)

cursor = con.cursor()

# cursor.execute("CREATE DATABASE DARAKSHA")
# cursor.execute("CREATE TABLE reg(id int primary key, name varchar(20) , email varchar(50))")
cursor.execute("INSERT INTO  reg VALUES(1,'Daraksha', 'daraksha@gmail.com')")
con.commit()
con.close()
