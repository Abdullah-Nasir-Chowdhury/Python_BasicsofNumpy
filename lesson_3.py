# Numpy array mathematics
import numpy as np

n1 = np.array([10,20])
n2 = np.array([30,40])

# add two arrays:
array_sum = np.sum([n1,n2])
print(array_sum)
# add arrays along columns:
array_sum_col = np.sum([n1,n2], axis=0)
print(array_sum_col)
# add arrays along rows:
array_sum_row = np.sum([n1,n2], axis=1)
print(array_sum_row)


# scalar operations:
n1 = n1 + 1
print(n1)
n1 = n1 - 1
print(n1)
n1 = n1 * 2
print(n1)
n1 = n1 / 2
print(n1)


# mean, standard deviation, median:
n1 = np.array([10,20,30,40,50,60,70])
# mean:
print(np.mean(n1))
# median:
print(np.median(n1))
# standard deviation:
print(np.std(n1))