def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd digits.
    Args:
        s: str
    Returns:
        int: return answer
    """
    sum=0
    n=0
    while n<len(s):
        if int(s[n])%2!=0:
            sum=sum+int(s[n]) 
        n=n+1

    return sum
print(main("98421"))
    
