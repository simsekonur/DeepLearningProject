import numpy as np 
import math 
import time 

beforeTime = time.time()

u = np.zeros((10000,1))
v = np.ones((10000,1))
u = np.exp(v) # elementwise exp to each of the element of vector v
myVar = np.exp(1)

afterTime = time.time()

print(myVar)
print(u)
print("Built in " + str(1000*(afterTime-beforeTime)) + "ms" )

"""
beforeTime = time.time()
u = np.zeros((10000,1))
for i in range(10000):
    u[i] = math.exp(u[i])
afterTime = time.time()
print("Explicit for loop " + str(1000*(afterTime-beforeTime)) + "ms" )
"""


