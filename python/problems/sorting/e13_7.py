def binary_search(arr, key):
    hi, lo = len(arr) - 1, 0

    while lo <= hi:
        mid = (hi + lo) // 2

        if key == arr[mid]:
            return mid  # Return the index of the key
        elif key < arr[mid]:
            hi = mid - 1
        else:  # key > arr[mid]
            lo = mid + 1

    return -1  # Return -1 if the key is not found


def count_frequency(arr, k):
    index_k = binary_search(arr, k)
    print(index_k)
    if index_k == -1:
        return -1
    
    count = 1
    size = len(arr)

    for i in range(index_k + 1, size):  # go up
        if arr[i] == k:
            count += 1
        else:
            break
    
    for i in range(index_k - 1, -1, -1):  # go down   
        if arr[i] == k:
            count += 1
        else:
            break
    return count

arr = [1,2,3,4,5]
k = 2

if __name__ == '__main__':
    count = count_frequency(arr, k)
    if count == -1:
        print('Element does not exist')
    else:
        print('Count of', k, 'is', count)