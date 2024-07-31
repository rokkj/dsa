
def insertion_sort(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    n = len(arr)
    for i in range(1, n):
        temp = arr[i]
        j = i-1
        while j > -1 and arr[j] > temp:
            arr[j+1] = arr[j]
            arr[j] = temp
            j -= 1
            
    return arr
