import array

symbols = '$¢£§'


def genexp():
    gen_tuple = tuple(ord(symbol) for symbol in symbols)
    print(gen_tuple)

    # The first argument of the array constructor defines the storage type used for the numbers in the array
    gen_array = array.array('I', (ord(symbol) for symbol in symbols))
    print(gen_array)


if __name__ == '__main__':
    genexp()
