def count_all_subsets(n):

    if n == 0:
        return 1

    return 2 * count_all_subsets(n - 1)
