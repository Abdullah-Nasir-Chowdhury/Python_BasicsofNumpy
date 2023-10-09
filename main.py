import numpy as np
# single dimensional array
n1 = np.array([10,20,30,40])
print(n1)
# Multi dimensional array
n2 = np.array([[10,20,30,40],[40,30,20,10]])
print(n2)
# zeros:
n3 = np.zeros((1,2))
print(n3)
n4 = np.zeros((5,5))
print(n4)
# initializing numpy array with same number:
n5 = np.full((2,2),10)
print(n5)
# initializing numpy array within a range:
n6 = np.arange(10,20)
print(n6)
n7 = np.arange(10,50,5)
print(n7)
# initializing numpy array with random numbers:
n8 = np.random.randint(1,100,5)
print(n8)

