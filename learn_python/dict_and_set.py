t1 = (1, 2, 3)
t2 = (1, (2, 3))

dict1 = {t1: t2}
set1 = set(t1)
set2 = set(t2)

print(dict1)
print(set1)
print(set2)
print(set1 & set2)