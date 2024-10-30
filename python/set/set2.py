s={1,2,3,4,5}
s1={1,2,3,6}
s2=s.copy()
s.difference_update(s1)
# s.symmetric_difference_update(s1)
print(s)