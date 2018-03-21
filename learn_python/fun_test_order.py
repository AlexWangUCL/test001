L = [2, 8, 11, 9, 25, 6]
for i in range((len(L)-1)):
    a = max(L)
    print(a)
    L = L.pop(i)
    i = i+1