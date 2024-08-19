def merge(a, b):
    i = 0
    j = 0
    combined = []

    # Continue until one list is fully traversed
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            combined.append(a[i])
            i += 1
        elif b[j] < a[i]:
            combined.append(b[j])
            j += 1
        elif a[i] == b[j]:
            combined.append(a[i])
            i += 1
            j += 1

    # If there are remaining elements in a
    while i < len(a):
        combined.append(a[i])
        i += 1
    
    # If there are remaining elements in b
    while j < len(b):
        combined.append(b[j])
        j += 1

    return combined


print(merge([2, 4, 6, 8, 9], [8, 9, 12, 23, 65, 89]))