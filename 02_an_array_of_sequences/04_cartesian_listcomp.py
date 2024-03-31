colors = ['black', 'white']
sizes = ['S', 'M', 'L']


def cartesian_listcomp():
    # Generates list arranged by color, then size
    tshirts = [(color, size) for color in colors for size in sizes]
    print(tshirts)


def for_loop():
    for color in colors:
        for size in sizes:
            # Resulting list is arranged in the same order as the first listcomp
            print((color, size))


def cartesian_reversed():
    # Rearranging the for clauses alters the ordering. Line break adds clarity
    tshirts = [(color, size) for size in sizes
               for color in colors]
    print(tshirts)


if __name__ == '__main__':
    cartesian_listcomp()
    for_loop()
    cartesian_reversed()