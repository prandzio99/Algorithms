# an implementation of the fibbonaci search

def fibonacci_search(arr, n):
    prev_fib_2 = 0
    prev_fib_1 = 1
    fib = prev_fib_2 + prev_fib_1

    while fib < len(arr):
        prev_fib_2 = prev_fib_1
        prev_fib_1 = fib
        fib = prev_fib_2 + prev_fib_1

    offset = -1

    while fib > 1:
        i = min(offset+prev_fib_2, len(arr)-1)
        if arr[i] < n:
            fib = prev_fib_1
            prev_fib_1 = prev_fib_2
            prev_fib_2 = fib - prev_fib_1
            offset = i
        elif arr[i] > n:
            fib = prev_fib_2
            prev_fib_1 -= prev_fib_2
            prev_fib_2 = fib - prev_fib_1
        else:
            return True

    if prev_fib_1 == n and arr[len(arr)-1] == n:
        return True

    return False


# test code
if __name__ == '__main__':
    test_list = [x for x in range(10)]
    print(fibonacci_search(test_list, 2))
    print(fibonacci_search(test_list, 12))
