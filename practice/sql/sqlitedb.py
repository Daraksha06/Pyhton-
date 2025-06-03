import sqlite3
con = sqlite3.connect("mydb.db")
con.execute("create table reg(id int primary key , name varchar(30) , email varchar(50))")
# sqlite three extension. db browser when want to do without without extension