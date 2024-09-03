def find_fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    super_previous = 0
    previous = 1
    for i in range(2, n+1):
        current = super_previous + previous
        super_previous = previous 
        previous = current
    return previous