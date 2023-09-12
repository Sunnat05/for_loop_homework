def main(A,B):
    ans=[]
    for i in list(range(A,B)):
        ans+=[i]
    """
    Return the numbers from B to A in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """
    return ans[::-1]
print(main(3,7))