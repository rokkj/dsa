def selection_sort(arr):
    for i in range(len(arr)):
        minvalue = arr[i]
        minindex = i
        for j in range(i+1,len(arr)):
            if arr[j] < minvalue:
                minvalue = arr[j]
                minindex = j
        arr[i], arr[minindex] = arr[minindex], arr[i]
    print(arr)

selection_sort([5,8,8,9,4,7])