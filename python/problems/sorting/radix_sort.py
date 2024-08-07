#https://www.youtube.com/watch?v=Il45xNUHGp0&t=4s

def counting_sort(arr, place):
    size = len(arr)
    count = [0] * 10
    output = [0] * size
    
    # Calculate count of elements.
    for i in range(0, size):
        index = arr[i] // place
        count[index % 10] += 1
        
    # Calculate cumulative count
    
    for i in range(1, 10):
        count[i] += count[i-1]
    
    # Place the elements in the sorted order
    i = size - 1
    while i >= 0:
        index = arr[i] // place
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -=1
    
    for i in range(0, size):
        arr[i] = output[i]
        
def radix_sort(arr):
    # Get maximum element
    max_element = max(arr)
    
    # Apply counting sort to sort elements based on place value.
    place = 1
    while max_element // place > 0:
        counting_sort(arr, place)
        place *= 10
    return arr