def main(N):
    a=0
    for s in list(range(N+1)):
        if s%2==1:
            a=a+s
    """
    Return the sum of odd numbers from zero to N.
    Args:
        N: int
    Returns:
        int: return  answer
    """
    return a
print(main(5))