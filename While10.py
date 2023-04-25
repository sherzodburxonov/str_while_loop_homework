def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd digits.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    n=0
    while n<len(s):
        if int(s[n])%2==1:
            i=int(s[n])+i
        n=n+1
    return i
print(main("5468745645"))
