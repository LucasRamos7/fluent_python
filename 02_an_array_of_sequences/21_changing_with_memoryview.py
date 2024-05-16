from array import array


if __name__ == '__main__':
    numbers = array('h', [-2, -1, 0, 1, 2])

    # Build memoryview from array of 5 16-bit signed integers (typecode 'h')
    memv = memoryview(numbers)
    print(len(memv))

    # memv sees the same five items in the array
    print(memv[0])

    # Create memv_oct by casting the elements of memv to bytes (typecode 'B')
    memv_oct = memv.cast('B')

    # Export elements of memv_oct as a list of 10 bytes, for inspection
    print(memv_oct.tolist())

    # Assign value 4 to byte offset 5
    memv_oct[5] = 4

    print(numbers)