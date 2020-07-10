import numpy as np 
A = np.array([[1.,2.,3.,4.],[5.,6.,7.,8.],[9.,10.,11.,12.]]) # 3x4 matrix
print(A)
cal = A.sum(axis=0) # cal will be list of column summation 

print("Summation along columns as a list :" )
print(cal)


# A.shape --> creates a tuple of dimensions

count_row = A.shape[0]  # gives number of row count
count_col = A.shape[1]  # gives number of col count

i=0 
j=0 

while(j < count_col):
    i=0
    while(i < count_row):
        A[i][j] = (100* A[i][j] / cal[j])
        i+=1
    j+=1
     
print (A)

print("########################")
A = np.array([[1.,2.,3.,4.],[5.,6.,7.,8.],[9.,10.,11.,12.]]) # 3x4 matrix
percentage = 100* A/ cal.reshape(1,4)
print(percentage)
print("########################")
