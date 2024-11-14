import sqlite3

con=sqlite3.connect("/home/synnefo/Desktop/Riju/files/database/alpha.db")
username=input("enter username:")
password=input("enter password:")
data=con.execute("select * from employee")
for i in data:
    if i[5]==username and i[6]==password:
        print("login successfully")
    # else:
    #     print("invalid username or password")