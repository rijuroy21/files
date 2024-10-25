# l=[1,2,3,4,5]
# res=list(map(lambda x:x*x,l))
# print(res)

def square(x):
    return x*x
l=[1,2,3,4,5]
res=map(square,l)
print(list(res))