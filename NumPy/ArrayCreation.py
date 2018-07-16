import numpy as np
from numpy import pi

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

# Create 2-dimensional array initialized with zeros
e = np.zeros( (3,4) )

# Print e
print e

# Create 2-dimensional array initialized with ones
f = np.ones( (2,3,4), dtype=np.int16 )

# Print f
print f

# Create 2-dimensional array initialized with random data
g = np.empty( (2,3) )

# Print g
print g

# Create a sequence from a to b, step c (a,b,c)
h = np.arange( 10, 30, 5 )

# Print h
print h

# Create a sequence from a to b, step c (a,b,c)
i = np.arange( 0, 2, 0.3)

# Print i
print i

#Create a sequence in linear space from a to b, number of elements c (a,b,c)
j = np.linspace(0,2,9)

# Print j
print j

# Create a sequence in linear space from a to b, number of elements c (a,b,c)
k = np.linspace(0, 2*pi, 100)

# Print k
print k

# Create a sequence using the sin function with input array k
l = np.sin(k)

# Print l
print l