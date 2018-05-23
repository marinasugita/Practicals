def count_number_of_blocks(n):
    """Calculate number of blocks needed, given the number of rows to make a 2D pyramid."""
    if n <= 0:
        return 0
    return n + count_number_of_blocks(n - 1)


print(count_number_of_blocks(6))