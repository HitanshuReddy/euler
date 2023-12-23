u = 1000
l = list(range(1, u))
x = []
for i in l:
    if i%3 == 0 or i%5 == 0: 
        x.append(i)

y = sum(x)
print(y)
