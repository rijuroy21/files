import re
a=input("enter your password to check its strength: ")
res=re.search('[A-Z].{7}',a)
if res:
    print("password is strong")
else:
    print("password is weak")    