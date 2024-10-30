from functools import reduce
l=[1,2,3]
res=reduce(lambda x,y:x+y,l)
print(res)

# from functools import reduce
# def add(x,y):
#      return x+y
# l=[1,2,3]
# res=reduce(add,l)
# print(res)