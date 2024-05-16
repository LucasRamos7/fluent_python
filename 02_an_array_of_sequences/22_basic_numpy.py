import numpy as np


if __name__ == '__main__':
    # Build and inspect a numpy.ndarray with integers 0 to 11
    a = np.arange(12)
    print(a)
    print(type(a))

    # Inspect the dimensions of the array: this is a one-dimensional, 12-element array
    print(a.shape)

    # Change the shape of the array, adding one dimension, then inspecting the result
    a.shape = 3, 4
    print(a)

    # Get row at index 2
    print(a[2])

    # Get element at index 2, 1
    print(a[2, 1])

    # Get column at index 1
    print(a[:, 1])

    # Create a new array by transposing (swapping columns with rows)
    print(a.transpose())

