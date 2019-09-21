import numpy as np
import functions

#Create numpy array
a1 = np.arange(15)
a2 = a1.reshape(3,5)
a3 = a1.reshape(5,3)
a4 = np.arange(1, 15, 2)

b1 = np.array([1,2,3,4])
b2 = np.array([(1,2,3,4),(5,6,7,8)], dtype=int)
b3 = np.array([(1,2,3,4), (5,6,7,8)], dtype=float)
b4 = np.array([(1,2,3,4),(5,6,7,8)], dtype=complex)
b5 = np.array([(1,2,3,4),(5,6,7,8)], dtype=np.int16)

c1 = np.zeros( (3,4) )
c2 = np.ones ( (3,4) )
c3 = np.empty( (3,4) )

#Print array
#print(np.arange(10000).reshape(100,100))
#The above array is too large so numpy auto only prints the corners
#If you want to print entire the array, using
#np.set_printoptions(threshold=np.nan)

# Basic operations

pi = np.pi
print(pi)
# Arithmetic operators on arrays apply elementwise. 
# A new array is created and filled with the result.
c2 = c2*pi
print(np.cos(c2))
# Use np.ndarray.astype()
print((10*np.sin(c2)).astype(np.int64))
print (c2 == -1.0)

# Matrix
A = np.array( [(1, 1), (0, 1)] )
B = np.array( [[1, 1], [0, 1]] )
print(A == B )

print( A.sum() )
print( A.sum(axis=0) )   # sum of each column
print( A.sum(axis=1) )   # sum of each row

print( A.min() )
print( A.min(axis=0) )
print( A.min(axis=1) )

print( A.max() )
print( A.max(axis=0) )
print( A.max(axis=1) )

C = np.array( [(2, 0), (3, 4)] )
print( A*C )        # elementwise product
print( A@C )        # mattrix product
print( A.dot(B) )   # another mattrix product

# Some operations, such as += and *=, act in place to modify an existing array rather than create a new one.

# When operating with arrays of different types, 
# the type of the resulting array corresponds to the more general or precise one 
# (a behavior known as upcasting).

# Slicing, indexing, and iterating