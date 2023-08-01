def main(A,B):
    s=0
    for a in list(range(A,B)):
        s=s+a 
    """
    Return the sum of all integers from A to B.
    Args:
        A: int
        B: int
    Returns:
        int: return  answer
    """
    return s
print(main(4,7))