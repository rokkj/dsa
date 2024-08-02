def msort(arr, start, end):
    if start >= end:
        return
    mid = (start + end) // 2
    msort(arr, start, mid)
    msort(arr, mid + 1, end)
    i = start
    j = mid + 1
    combined = []
    while i <= mid and j <= end: 
        if arr[i] < arr[j]:
            combined.append(arr[i])
            i+=1
        else:
            combined.append(arr[j])
            j+=1
    
    while i <= mid:
        combined.append(arr[i])
        i+=1
        
    while j <= end:
        combined.append(arr[j])
        j+=1
    
    arr[start:end + 1] = combined
    
def merge_sort(arr):
    msort(arr, 0, len(arr)-1)
    return arr