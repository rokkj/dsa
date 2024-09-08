def get_binary_strings_helper(index, current, result):

    if  len(current) == index:
        result.append("".join(current))
        return
    
    current[index] = '0'
    get_binary_strings_helper(index + 1, current, result)
    current[index] = '1'
    get_binary_strings_helper(index + 1, current, result)
    
def get_binary_strings(n):
    result = []
    current = ['0'] * n
    
    get_binary_strings_helper(0, current, result)
    return result
