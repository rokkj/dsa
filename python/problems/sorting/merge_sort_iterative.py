def merge(arr, left, mid, right):
    l = arr[left:mid+1]
    r = arr[mid+1:right+1]
    i = 0 
    j = 0 
    k = left
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            arr[k] = l[i]
            i += 1
        else:
            arr[k] = r[j]
            j += 1
        k += 1
    
    while i < len(l):
        arr[k] = l[i]
        i += 1
        k += 1
        
    while j < len(r):
        arr[k] = r[j]
        j += 1
        k += 1

# review
def split(arr, l, h):
    block = 1
    while block <= h - l:
        i = l
        while i < h:
            left = i
            mid = min(i + block - 1, h)
            right = min(i + 2 * block - 1, h)
            merge(arr, left, mid, right)
            i += 2 * block
        block *= 2
        

def merge_sort(arr):
    n = len(arr)
    left = 0
    right = n - 1
    split(arr, left, right)
    return arr