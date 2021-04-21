import time
from binary_search import binary_search as bs
from exponential_search import exponential_search as es
from fibonacci_search import fibonacci_search as fs
from interpolation_search import interpolation_search as ints
from jump_search import jump_search as js
from linear_search import linear_search as ls
from recursive_search import recursive_search as rs
from random import randint as random

SET_RANGE = 1000000
TEST_LIST = [x for x in range(SET_RANGE)]
ITEM = random(0, SET_RANGE)


def timer(func):
    def wrapper(*args, **kwargs):
        before = time.time()
        val = func(*args, **kwargs)
        after = time.time()
        result = after - before
        if result > 1:
            print("Finished in", result, "seconds")
        else:
            print("Finished in", result*1000, "milliseconds")
        if val:
            print("Element found.\n")
        else:
            print("Element not found.\n")
    return wrapper


@timer
def binary(arr, x):
    print("Binary Search")
    res = bs(arr, x)
    return res


@timer
def exp(arr, x):
    print("Exponential Search")
    res = es(arr, x)
    return res


@timer
def fib(arr, x):
    print("Fibonacci Search")
    res = fs(arr, x)
    return res


@timer
def ins(arr, x):
    print("Interpolation Search")
    res = ints(arr, x)
    return res


@timer
def jump(arr, x):
    print("Jump Search")
    res = js(arr, x)
    return res


@timer
def line(arr, x):
    print("Linear Search")
    res = ls(arr, x)
    return res


@timer
def rec(arr, x):
    print("Recursive Search")
    try:
        res = rs(arr, x)
        return res
    except RecursionError:
        return False


# driver code
if __name__ == '__main__':
    print("Searching for", ITEM, "in array [0, 1000000]\n")
    binary(TEST_LIST, ITEM)
    exp(TEST_LIST, ITEM)
    fib(TEST_LIST, ITEM)
    ins(TEST_LIST, ITEM)
    jump(TEST_LIST, ITEM)
    line(TEST_LIST, ITEM)
    rec(TEST_LIST, ITEM)


# Example result

# Searching for 540867 in array [0, 1000000]

# Binary Search
# Finished in 9.973287582397461 milliseconds
# Element found.

# Exponential Search
# Finished in 8.779048919677734 milliseconds
# Element found.

# Fibonacci Search
# Finished in 0.0 milliseconds
# Element found.

# Interpolation Search
# Finished in 0.0 milliseconds
# Element found.

# Jump Search
# Finished in 4.988670349121094 milliseconds
# Element found.

# Linear Search
# Finished in 14.968156814575195 milliseconds
# Element found.

# Recursive Search
# Finished in 14.055195569992065 seconds
# Element not found.
