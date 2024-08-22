def two_sum(numbers, target):
    mem = {}
    
    for i in range(0, len(numbers)):
        diff = target - numbers[i]
        if diff in mem:
            return [mem[diff], i]
        mem[numbers[i]] = i
    
    return [-1, -1]