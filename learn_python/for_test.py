name = ['Bart', 'Lisa', 'Adam']
for i in range(3):
    print(name[i])
    
n = 0
while n < 11:
    n = n + 1
    if n%2 == 1:
        continue
    else:
        print(n)
print('end')