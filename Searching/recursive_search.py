# an implementation of recursive linear search


def recursive_search(arr, n):
    if len(arr)-1 < 0:
        return False
    elif arr[0] == n:
        return True
    elif arr[len(arr)-1] == n:
        return True
    else:
        return recursive_search(arr[1:-1], n)


# test code
if __name__ == '__main__':
    test_list = [x for x in range(10)]
    print(recursive_search(test_list, 6))
    print(recursive_search(test_list, 16))
