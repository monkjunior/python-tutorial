import numpy as np

def printInfo(a):
    print("\n\nValues: \n", a)
    print("\nType: ", type(a))
    print("\nDimentions: ", a.ndim)
    print("\nShape (tuple): ", a.shape)
    print("\nNumber of elements: ", a.size)
    print("\nData type: ", a.dtype)
    print("\nSize in bytes of each element: ", a.itemsize)
