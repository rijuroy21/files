import sqlite3

con=sqlite3.connect('/home/synnefo/Desktop/Riju/files/database/datbase4.db')

try:
    con.execute("create table std_details(admno int,name text,age int,email text)")
except:
    pass    

# a=int(input("how many members do you want to add:"))
# for i in range(a):
#     admno=int(input("Enter the admno of the student:"))
#     name=input("Enter name of the student:")
#     age=int(input("Enter age of the student:"))
#     email=input("Enter email of the student:")
#     con.execute("insert into std_details values(?,?,?,?)",(admno,name,age,email))
#     con.commit() 
  
# data=con.execute("select * from std_details where name='shino'" )
# for i in data:
#     print(i)   

# data=con.execute("select * from std_details" )
# print("{:<20}{:<20}{:<20}{:<20}".format("Admno","Name","Age","Email"))
# print("_"*90)
# for i in data:
#     print("{:<20}{:<20}{:<20}{:<20}".format(i[0],i[1],i[2],i[3]))
#     print("_"*90)

# c=con.execute('select min(age) from std_details')
# for i in c:
#     print(i)

data=con.execute("select * from std_details order by age" )
for i in data:
    print(i)