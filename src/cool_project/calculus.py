def sum_small_numbers(a: int, b: int) -> int:
    """Sum two small numbers. Does not work with numbers bigger than 100 or 50."""
    if a > 100:
        raise ValueError("a is too big, must be smaller than 100")
    if b > 50:
        raise ValueError("b is too big, must be smaller than 50")
    return a + b
