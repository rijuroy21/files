import sqlite3
con=sqlite3.connect ('/home/synnefo/Desktop/Riju/files/database/employee2.db')
# N_id=input("enter id:")
# Nname=input("Enter name:")
# con.execute("update students set name=? where id=?",(n_name,n_id))
# con.commit()_

data=con.execute("select * from employee2 orderd by age" )
for i in data:
    print(i)