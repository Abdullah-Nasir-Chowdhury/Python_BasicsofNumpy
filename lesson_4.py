#Numpy Matrix:
import numpy as np

n1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
n2 = np.array([[9,8,7],[6,5,4],[3,2,1]])
print(n1)

# indexing:
print(n1[0])
print(n1[1])
print(n1[:,1])
print(n1[:,2])
print(n1[1:2])

# transpose a matrix:
print(n1.transpose())

# matrix multiplication:
print(n1.dot(n2))
print(n2.dot(n1))


# numpy save and load:
# save:
np.save('my_numpy',n1)
# load:
n3 = np.load('my_numpy.npy')
print(n3)


# matrix multiplication:
