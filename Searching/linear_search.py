# simple implementation of linear search algorithm

def linear_search(arr, n):
    for elem in arr:
        if elem == n:
            return True
    else:
        return False


# test code
if __name__ == '__main__':
    test_list = [x for x in range(10)]
    print(linear_search(test_list, 7))
    print(linear_search(test_list, 10))
