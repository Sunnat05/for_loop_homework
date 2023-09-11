def main(n):
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int
    Returns:
        string: return  answer
     """
    ans=""
    ans+=str(list(range(n)))
    return ans[1:-1]
print(main(4)) 