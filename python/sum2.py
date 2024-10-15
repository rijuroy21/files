
i=1
sum=0
osum=0
esum=0
while(i<=10):
    sum+=i

    if(i%2==0):
        esum+=i
    elif(i%2!=0): 
        osum+=i
    i+=1
print(sum,"is sum")
print(osum,"is Sum of odd numbers")
print(esum,"is Sum of even numbers")


