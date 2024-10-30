a=int(input("enter a number:"))
last_digit=a%10
if(last_digit%3==0):
    print(a,"divisible by 3")
else:
    print(a,"is not divisible by 3")