import sqlite3

con=sqlite3.connect('/home/synnefo/Desktop/Riju/files/database/employee.db')

data=con.execute("select * from employee")
for i in data:
    print("{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
    
con.execute("update employee set username='harikrishnan' where email='hari@gmail'")  
con.commit() 
try:
    con.execute("delete from employee where email='hari@gmail'")  
    con.commit()   
except:
    pass    