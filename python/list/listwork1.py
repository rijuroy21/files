l=[2,8,10,5,4]
length=len(l)
for i in range(length):
    s=i
    for j in range(i+1,length):
        if l[j]<l[s]:
            s=j
    l[i],l[s]=l[s],l[i]
print(l)
print(l[0])