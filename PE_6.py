import math as m 
x = list(range(1,101))
y = list()
for i in x:
    q = m.pow(i, 2)
    y.append(q)

r = sum(x)
#print(r)
t = m.pow(r, 2)
#print(t)
z = sum(y) - t
print(abs(z))


            
