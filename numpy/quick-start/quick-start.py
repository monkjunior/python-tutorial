import numpy as np

def printInfo(a):
    print("\n\nValues: \n", a)
    print("\nType: ", type(a))
    print("\nDimentions: ", a.ndim)
    print("\nShape (tuple): ", a.shape)
    print("\nNumber of elements: ", a.size)
    print("\nData type: ", a.dtype)
    print("\nSize in bytes of each element: ", a.itemsize)


a1 = np.arange(15)
a2 = a1.reshape(3,5)
a3 = a1.reshape(5,3)
a4 = a1.reshape(1,15)

printInfo(a1)
printInfo(a2)
printInfo(a3)
printInfo(a4)