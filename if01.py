def main(a,b,c):
    """
    Find the largest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    max = a
    if max > b:
        if max > c:
            max = max
        else:
            max = c

    else: 
        if b > c:
            max = b
        else:
            max = c 
            return max
print(main(2,6,7))