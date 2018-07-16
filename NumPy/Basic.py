import numpy as np

# NumPy's main object is the homogenous multidimensional array

# NumPy's array class is call ndarray, alias array

# Declare ndarray with range 0-14 in the shape of 3 x 5 : (row x column) : (1st x 2nd axis)
a = np.arange(15).reshape(3,5)

# Print array elements
print a

# Print shape of array: (3 X 5)
print a.shape

# Print number of axes (dimensions): 2
print a.ndim

# Print data type of elements: int32
print a.dtype.name

# Print size of each element in bytes: 4
print a.itemsize

# Print total number of elements in array: 15
print a.size

# Print type of object a: numpy.ndarray
print type(a)

# Create a new array
b = np.array([6,7,8])

# Print b array
print b

# Print type of object b: numpy.ndarray
print type(b)