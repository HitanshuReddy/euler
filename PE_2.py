import sys

sys.setrecursionlimit(5000)
y = []
def fib(n):
    if n <2: 
        return n
    else:
        return fib(n-1) + fib(n-2)
x = [fib(n) for n in range(34)]
for i in x:
    if i%2 ==0 and i < 4000000:
        y.append(i)

#print(x)
print(sum(y))
