# simple implementation of jump search algorithm
import linear_search as ls
import math


def jump_search(arr, n):
    jump = math.sqrt(len(arr))
    prev = 0

    while arr[int(min(jump, len(arr))-1)] < n:
        prev = jump
        jump += math.sqrt(len(arr))
        if prev >= len(arr):
            return False

    return ls.linear_search(arr[int(prev):], n)


# test code
if __name__ == '__main__':
    test_list = [x for x in range(10)]
    print(jump_search(test_list, 3))
    print(jump_search(test_list, 13))
