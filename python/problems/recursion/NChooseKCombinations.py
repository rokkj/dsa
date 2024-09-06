def combinations_recurrsive(current_number, n, k, current, result):
    if len(current) == k:
        result.append(list(current))
        return
    
    if current_number == n + 1:
        return
    
    current.append(current_number)
    combinations_recurrsive(current_number + 1, n, k, current, result)
    current.pop()
    combinations_recurrsive(current_number + 1, n, k, current, result)

def find_combinations(n, k):
    result = []
    current = []
    
    combinations_recurrsive(1, n, k, current, result)
    return result