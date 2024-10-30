l=[6,3,9,6,2]
a=int(input("enter a number:"))
for i in l:
    if a not in l:
        l.append(a)
        print(l)
        break
    else:
        print("duplicate value")
        break
# l = [6,3,9,6,2]
# a = int(input("Enter a number: "))
# if a not in l:
#     l.append(a)
#     print(l)
# else:
#     print("Duplicate value")