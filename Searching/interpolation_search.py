# a simple implementation of interpolation search

def interpolation_search(arr, n):
    low = 0
    high = len(arr) - 1

    if low <= high and arr[low] <= n <= arr[high]:
        position = low + ((high - low) // (arr[high] - arr[low]) * (n - arr[low]))

        if arr[position] == n:
            return True

        elif arr[position] < n:
            return interpolation_search(arr[position+1:], n)

        else:
            return interpolation_search(arr[:position], n)

    else:
        return False


# test code
if __name__ == '__main__':
    test_list = [x for x in range(10)]
    print(interpolation_search(test_list, 3))
    print(interpolation_search(test_list, 13))
