def main(k,n):
    ans=[]
    while n>0:
        ans+=[k]
        n-=1
    """
    Repeat the number k n times and return to the list view.
    Args:
        k: int
        n: int
    Returns:
        list: return  answer
    """
    return ans
print(main(4,6))