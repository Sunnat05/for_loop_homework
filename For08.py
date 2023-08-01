def main(N):
    s=0
    for a in list(range(1,N+1)):
        s=s+1/a
    """
    The number N is given. Calculate the sum below: 1 + 1/2 + 1/3 + … + 1/N.
    Args:
        N: int
    Returns:
        float: return  answer
    """
    return s
print(main(6))