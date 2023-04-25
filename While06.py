def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    i=0
    n=0
    while n<len(s):
        if s[n]=="a" :
            i=i+1
        if s[n]=="e" :
            i=i+1
        if s[n]=="i" :
            i=i+1
        if s[n]=="o" :
            i=i+1
        if s[n]=="u" :
            i=i+1
        if s[n]=="o'" :
            i=i+1
        n=n+1
    return len(s)-i
print(main("Codeacademy"))