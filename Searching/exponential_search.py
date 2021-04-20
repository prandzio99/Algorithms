# a simple implementation of exponential search algorithm
import binary_search as bs


def exponential_search(arr, n):
    if arr[0] == n:
        return True

    i = 1
    while i < len(arr) and arr[i] <= n:
        i *= 2

    start = i // 2
    end = min(i, len(arr)-1)

    return bs.binary_search(arr[start:end], n)


# test code
if __name__ == '__main__':
    test_list = [x for x in range(10)]
    print(exponential_search(test_list, 4))
    print(exponential_search(test_list, 15))
