# simple implementation of binary search algorithm

def binary_search(arr, n):
    left = 0
    right = len(arr)-1
    if right >= left:
        mid = (left + right) // 2
        if arr[mid] == n:
            return True
        elif arr[mid] > n:
            return binary_search(arr[:mid], n)
        else:
            return binary_search(arr[mid+1:], n)
    else:
        return False


# test code
if __name__ == '__main__':
    test_list = [x for x in range(10)]
    print(binary_search(test_list, 5))
    print(binary_search(test_list, 12))
