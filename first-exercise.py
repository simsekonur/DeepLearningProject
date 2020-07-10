import math 
import numpy as np 


def basic_sigmoid(x): # this func. can only work with a real number
    temp = math.exp(-x)
    s = 1 / (1+ temp)
    return s 

print(basic_sigmoid(3))
"""
x = np.array([1,2,3])
print(np.exp(x))
print(x+3)
"""
def sigmoid(x): # this func. works with vector
    return 1/ (1+ np.exp(-x))

x = np.array([1,2,3])
print(sigmoid(x)) 

def sigmoid_derivative(x):
    q = sigmoid(x)
    dq = q *(1-q)
    return dq

x = np.array([1, 2, 3])
print ("sigmoid_derivative(x) = " + str(sigmoid_derivative(x)))

def image2vector(image):
    v = image.reshape((image.shape[0] * image.shape[1] *image.shape[2],1))
    return v

image = np.array([[[ 0.67826139,  0.29380381],
        [ 0.90714982,  0.52835647],
        [ 0.4215251 ,  0.45017551]],

       [[ 0.92814219,  0.96677647],
        [ 0.85304703,  0.52351845],
        [ 0.19981397,  0.27417313]],

       [[ 0.60659855,  0.00533165],
        [ 0.10820313,  0.49978937],
        [ 0.34144279,  0.94630077]]])

print ("image2vector(image) = " + str(image2vector(image)))

def normalizeRows(x): # x is matrix like 2x3
    x_norm = np.linalg.norm(x,axis=1,keepdims=True)
    x = x/ x_norm
    return x

x = np.array([
    [0, 3, 4],
    [1, 6, 4]])
print("normalizeRows(x) = " + str(normalizeRows(x)))

def L1loss(yhat,y): 
#the bigger loss is the bad prediction 
#the bigger loss is the more different yhat from y 
#somehow loss should be defined as the difference between 
#true values from predictions

#I experienced that if for loop is used,the same exact result
#will be obtained.However,it is best to use numpy's buit in func.

    return np.sum(abs(y-yhat))


yhat = np.array([.9, 0.2, 0.1, .4, .9])
y = np.array([1, 0, 0, 1, 1])
print("L1 = " + str(L1loss(yhat,y)))

def L2loss(yhat,y):
#it is inevitable that L2 loss will also depend on y (true results)
#and yhat (our prediction)

#this time we are using np.dot(...,...)
    return np.dot(y-yhat,y-yhat)

yhat = np.array([.9, 0.2, 0.1, .4, .9])
y = np.array([1, 0, 0, 1, 1])
print("L2 = " + str(L2loss(yhat,y)))


