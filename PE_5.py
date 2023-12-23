"""
[1,2,3...] here i%n = 0 i need to find n


"""
from tqdm import tqdm
import math as m 
#wn = list(range(1,5000))
x = list(range(1, 21))
#z = list()
#for i in tqdm(x, desc= 'Processing'): 
lcm = m.lcm(*x)
print(lcm)

#print(x)
#print(z)
