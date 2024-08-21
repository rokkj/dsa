def binary_search(arr, key):
    hi, lo = len(arr) - 1, 0

    while lo <= hi:
        mid = (hi + lo) // 2
        if key < arr[mid]:
            hi = mid - 1
        elif key > arr[mid]:
            lo = mid + 1
        else:
            return mid
    return -1

def find_sum(a, b, sum_value):
    a.sort()

    for i in range(0, len(b)):
        r = sum_value - b[i]
        if(binary_search(a, r) != -1):
            return -1
    return 0

a = [2,3,5,7,12,15,23,32,42]
b = [3,13,13,15,22,33]

if (find_sum(a,b,30)):
    print('True')
else:
    print('False')