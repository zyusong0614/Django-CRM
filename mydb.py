import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "password123",
)

# prepare a cursor object using cursor() method
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE dcrm_database")

print("Database created successfully........")

