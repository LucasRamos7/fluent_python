"""
vector2d.py: a simplistic class demonstrating some special methods

It is simplistic for didatic reasons. It lacks proper error handling, especially in the ''__add__'' and ''__mul__''
methods.

This example is greatly expanded later i nthe book.

Addition:

>>> v1 = Vector(2, 4)
>>> v2 = Vector(2, 1)
>>> v1 + v2
Vector(4, 5)

Absolute value:

>>> v = Vector(3, 4)
>>> abs(v)
5.0

Scalar multiplication
>>> v * 3
Vector(9, 12)
>>> abs(v * 3)
15.0

"""

import math


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # In case one chooses not to implement both __repr__ and __str__, implement only __repr__.
    def __repr__(self):
        return f'Vector({self.x!r}, {self.y!r})'

    def __abs__(self):
        return math.hypot(self.x, self.y)

    # If __bool__ is not implemented, Python tries to invoke x.__len__(), and if that returns zero, bool() returns
    # False. Otherwise, it returns True.
    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    # Allows multiplying a vector by a number, but not a number by a vector. This violates the commutative property of
    # scalar multiplication.
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


if __name__ == '__main__':
    import doctest
    doctest.testmod()