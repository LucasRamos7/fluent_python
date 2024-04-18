colors = ['black', 'white']
sizes = ['S', 'M', 'L']


def cartesian_genexp():
    # The genexp yields items one by one, a full list is never created in this example
    for tshirt in (f'{c} {s}' for c in colors for s in sizes):
        print(tshirt)


if __name__ == '__main__':
    cartesian_genexp()
