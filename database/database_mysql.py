import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='riju',
    password='Riju@123',
    database='sample',
)
mycursor=mydb.cursor()

try:
    mycursor.execute("create database sample")
except:
    pass