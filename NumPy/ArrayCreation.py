import numpy as np

# Create ndarray from Python list or tuple using array()
a = np.array([2,3,4])

# Print a
print a

# Print a data type: int64
print a.dtype

# Create ndarray
b = np.array([1.2, 3.5, 5.1])

# Print b
print b

# Print b data type: float64
print b.dtype

# Create 2-dimensional array
c = np.array([(1.5,2,3), (4,5,6)])

# Print c
print c

# Create 2-dimensional array with explicit data type
d = np.array([ [1,2], [3,4] ], dtype=complex)

# Print d
print d