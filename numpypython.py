# Liner algebra Library in python
# provide features for operation on multidimensional  arrays and matrices in python
import numpy as np
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)
print(type(arr1))

#2d array

arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2)
print(type(arr2))

#5*5 numPy array comprising of all zeros

arr3 = np.zeros((5,5))
print(arr3)
print(type(arr3))

#[5 7 9] ans 1+4 ,2+5, 3+6
a = np.array([1,2,3])
b = np.array([4,5,6])
ab=np.sum((a,b),axis=0)
print(ab)

#[ 6 15] 3+6(9) , 9+2+1(12)
a = np.array([2,4,3])
b = np.array([1,5,6])
ab=np.sum((a,b),axis=1)
print(ab)

# descending order
a = (9, 76, 7, 8, 4, 79, 87, 99)
x = sorted(a, reverse=True)
print(x)

# asscending order
a = (9, 76, 7, 8, 4, 79, 87, 99)
x= sorted(a)
print(x)