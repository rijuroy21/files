import sqlite3
con=sqlite3.connect('/home/synnefo/Desktop/Riju/files/database/employee.db')
try:
    con.execute("create table employee(emp_name text,age int,email text,phn_no int,username text,password text)")
except:
    pass
a=int(input("How many members do you want to add:" ))
for i in range (a):
    name=input("Enter your name:")
    age=int(input("Enter your age:"))
    email=input("Enter your mail:")
    phnno=int(input("Enter your phnno:"))
    username=input("Enter your username:")
    password=input("Enter your password:")
    con.execute("insert into employee values(?,?,?,?,?,?)",(name,age,email,phnno,username,password)) 
    con.commit()