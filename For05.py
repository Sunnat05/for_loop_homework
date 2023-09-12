def main(A,B):
    ans=""
    for i in list(range(A+1,B+1)):
        ans+=str(i)+','
    """
    Return the numbers from B to A in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """
    return ans[-2::-1]
print(main(3,7))