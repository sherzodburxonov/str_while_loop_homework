def main(s):
    """
    A string of numbers is given. Find the sum of all the digits and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    n=0
    while n<len(s):
        i=int(s[n])+i
        n=n+1
    return i
print(main("5468745645"))