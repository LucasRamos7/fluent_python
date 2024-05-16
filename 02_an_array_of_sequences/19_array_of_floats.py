# Import the array type
from array import array
from random import random


if __name__ == '__main__':
    # Create an array of double-precision floats (typecode 'd') from any iterable object - in this case, a genexp
    floats = array('d', (random() for i in range(10**7)))

    # Inspect the last number in the array
    print(floats[-1])

    fp = open('floats.bin', 'wb')

    # Save the array to a binary file
    floats.tofile(fp)
    fp.close()

    # Create an empty array of doubles
    floats2 = array('d')
    fp = open('floats.bin', 'rb')

    # Read 10 million numbers from the binary file
    floats2.fromfile(fp, 10**7)
    fp.close()

    # Inspect the last number in the array
    print(floats2[-1])

    # Verify that the contents of the arrays match
    print(floats == floats2)