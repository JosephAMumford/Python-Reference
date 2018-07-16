import numpy as np

# Create an array with 6 elements
a = np.arange(6)

print a

# Create an array with 12 elements, shape 4 rows, 3 columns
b = np.arange(12).reshape(4,3)

print b

# Create an array with 24 elements, shape 2 rows, 3 columns, 4 rows depth
c = np.arange(24).reshape(2,3,4)

print c

# Create an array with 10,000 elements.  Will print only corners
d = np.arange(10000)

print d 

# Create an array with 10,000 elements, shape 100 rows, 100 columns
e = np.arange(10000).reshape(100,100)

print e

# Set printoptions to print all values in list
np.set_printoptions(threshold=np.nan)

print e