def qsort(arr, start, end):
    if start >= end:
        return
    
    randindex = random.randint(start, end)
    arr[randindex], arr[start] = arr[start], arr[randindex]
    
    pivot = arr[start]
    bigger = start
    smaller = start
    
    for bigger in range(start + 1, end + 1):
        if arr[bigger] <= pivot:
            smaller += 1
            arr[smaller], arr[bigger] = arr[bigger], arr[smaller]
    
    arr[start], arr[smaller] = arr[smaller], arr[start]
    qsort(arr, start, smaller - 1)
    qsort(arr, smaller + 1, end)
        
def quick_sort(arr):
    qsort(arr, 0, len(arr) -1)
    return arr
