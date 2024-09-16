import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",  
    user="root",       
    password="root",   
)

try:
    my_cursor = mydb.cursor()
    
    my_cursor.execute("CREATE DATABASE IF NOT EXISTS Contact")

    mydb.commit()
    print("Database created")

except Exception as e:
    print(e)
    print("Error Occurred")

