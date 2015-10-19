#!/usr/bin/python3


def linear_search(alist, item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos + 1

    return found

test_list = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(linear_search(testlist, 3))
print(linear_search(testlist, 13))
