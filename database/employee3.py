import sqlite3
con=sqlite3.connect('/home/synnefo/Desktop/Riju/files/database/employee2.db')
try:
    con.execute("create table emp_salary(emp_name text,salary int,bonus int,incentive)")
except:
    pass
# a=int(input("How many members do you want to add:" ))
# for i in range (a):
#     id=input("Enter your id:")
#     salary=int(input("Enter your salary:"))
#     bonus=int(input("Enter your bonus:"))
#     incentive=int(input("Enter your incentive:"))
#     con.execute("insert into emp_salary values(?,?,?,?)",(id,salary,bonus,incentive))
#     con.commit()