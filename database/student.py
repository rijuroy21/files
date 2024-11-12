import sqlite3

con=sqlite3.connect('/home/synnefo/Desktop/Riju/files/database/students.db')

try:
    con.execute("create table std_details(admno int,name text,age int,email text)")
except:
    pass    

# con.execute("insert into std_details values(101,'Akshay',22,'akshay8055@gmail.com')")
# con.commit()

a=int(input("how many members do you want to add:"))
for i in range(a):
    admno=int(input("Enter the admno of the student:"))
    name=input("Enter name of the student:")
    age=int(input("Enter age of the student:"))
    email=input("Enter email of the student:")
    con.execute("insert into std_details values(?,?,?,?)",(admno,name,age,email))
    con.commit() 