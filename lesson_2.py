import numpy as np
# checking the shape of numpy arrays:
n10 = np.array([[10,20,30],[40,50,60]])
print(n10)
print(n10.shape)
# change the shape:
n10.shape = (3,2)
print(n10)


# stacking methods:
n11 = np.array([10,20,30])
n12 = np.array([40,50,60])
# vstack(): vertical stacking
print(np.vstack((n11,n12)))
# hstack(): horizontal stacking
print(np.hstack((n11,n12)))
# column_stack(): column stacking
print(np.column_stack((n11,n12)))



# intersection and difference methods:
n13 = np.array([1,2,3,4,5,0,13,14])
n14 = np.array([1,2,3,4,5,6,7,8,9])

# intersection:
print(np.intersect1d(n13,n14))

# difference:
# take the ones unique in n13
print(np.setdiff1d(n13,n14))
# take the ones unique in n14
print(np.setdiff1d(n14,n13))