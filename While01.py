def main(s):
    """
    A variable of type str is given. Find how many digits it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """ 
    i=0
    n=0
    while n<len(s):
        if s[n].isdigit():
            i=i+1
        n=n+1
    return i
print(main("python 2022"))