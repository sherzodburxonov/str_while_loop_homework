def main(s):
    """
    A variable of type str is given. Find how many uppercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    n=0
    while n<len(s):
        if s[n]==s[n].upper():
            i=i+1
        n=n+1
    return i
print(main("CodeschoolUz"))
    