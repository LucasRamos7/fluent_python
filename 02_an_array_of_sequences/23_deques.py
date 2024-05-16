from collections import deque


if __name__ == '__main__':
    # The optional maxlen argument sets the maximum number of items allowed in this instance of deque and sets a
    # read-only maxlen instance attribute
    dq = deque(range(10), maxlen=10)
    print(dq)

    # Rotating with n > 0 takes items from the right end and prepends them to the left, with n < 0 does it the other way
    # around
    dq.rotate(3)
    print(dq)
    dq.rotate(-4)
    print(dq)

    # Appending to a deque that is full (len(d) == d.maxlen) discards items from the other end
    dq.appendleft(-1)
    print(dq)

    # Adding three items to the right pushes out the three leftmost items
    dq.extend([11, 22, 33])
    print(dq)

    # extendleft works by appending each successive item of the iter argument to the left of the deque, reversing the
    # position of the items in the iterable
    dq.extendleft([10, 20, 30, 40])
    print(dq)

