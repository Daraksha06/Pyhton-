import mysql.connector
# Connect to MySQL server
con = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database_name"
)
# Create a cursor
cursor = con.cursor()
# Execute a query
cursor.execute("SELECT * FROM your_table")
# Fetch and print results
for row in cursor.fetchall():
    print(row)
# Close the connection
con.close()
