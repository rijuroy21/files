# a="helo"
# rev=" "
# for i in a:
#     rev=i+rev
# print(rev)

a="helo"
length=len(a)
for i in range(length-1,-1,-1):
    print (a[i],end="")