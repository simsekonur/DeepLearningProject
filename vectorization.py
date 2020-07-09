import numpy as np 
import time 

a = np.array([1,2,3,4])

print(a)

a = np.random.rand(1000000) 

b = np.random.rand(1000000)
tic = time.time()
c = np.dot(a,b)
toc = time.time()
print (c)
print("The operation is done with vectorization at " + str(1000*(toc-tic)) + "ms")

c = 0
timeBefore = time.time()
for i in range(0,len(a)):
    c += a[i] * b[i]
timeAfter = time.time()

print(c)
print("With the for loop at " +  str(1000*(timeAfter-timeBefore)) + "ms")
