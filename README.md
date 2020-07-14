# firstInternshipApp

This repository will include the work that I have done during my first internship.Below, you can find the information about the files:

**1)Vectorization.py :** This file is created to show how important it is to use vectorization in calculation. When we use built in functions of numpy instead of explicit for loops, it takes much more less time.

**2)Vectorization-general.py :** After recognizing how important using built in function is ,this file will include the built in functions which we can make use of while applying logistic regression. 

**3)broadcasting.py :** This file is created to recognize how Python behaves in the case of we are trying to add two matrices which are of dimensions 3x4 and 1x4.In mathemetically speaking, this operation can not be performed.However, this file shows that with only one line of code a 3x4 matrix can be divided by 1x4 matrix with the help of the broadcasting. I also do the same operation with two explicit for loop to see how hard it is with compared to built in function implementation.

**4)first-exercise.py :** This file contains a lot of useful and well implemented functions which then can be used in the implementation of deep learning.These are the solutions to the first exercise in deep learning course in Coursera. I understand how numpy can be used and what are the important functions that I need to use.

**5)Logistic_Regression_with_a_Neural_Network_mindset_v6a.ipynb :** This file is created to solve the first programming assignment of the course. Here is a step by step description of the algorithm which is a classification of images as a cat image or a non cat image:
  - Helper functions (like sigmoid)
  - Initilization of the parameter (w,b)
  - Propogate 
  - Optimize
  - Predict (By looking the value of sigmoid that is calculated by using parameter w and b, the prediction is done as 1 or 0)
  - Model (this is a function that merges all the function and calls them in correct order.)
  
  Remember that .h5 files are important. Why??
  
  **6)Exercise_1_House_Prices_Question.ipynb :** This file is created to predict the price of a house by using number of bedroom. In a sense, what we can do might simply be write a function that returns the price. However, instead of give as the parameter we train the data with several cases.And we want our model to "predict" for some certain numbers.In the case where we have images as input parameters, this method will be very useful.(Computer Vision)
  
  **7)Exercise2-Question.ipynb :** Predicting which number that handwritten number belongs to.
  
  **8)clothing.ipynb :** Predicting the clothing.
  
  **9)callback.ipynb :** Understanding callback which enables us to stop if we reach the enough accuracy without going the last epoch.
  
