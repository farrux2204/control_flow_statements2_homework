def main(a,b,c):
    """
    Find the smallest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    min=a
    if min<b:
        if min<c:
            min=min
        else:
            min =c
    else:
        if c>b:
            min =b
        else:
            min =c
    return min 
print(main(5,-1,2))
    




    
