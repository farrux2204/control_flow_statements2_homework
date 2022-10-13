def main(n):
    """
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    
    x1=n%10
    x2=n%100//10
    x3=n%1000//100
    x4=n//1000%10
    x5=n//10000
    mx=x1
    index=0
    if mx<x2:
        index=2
    elif mx<x3:
        index=3
    elif mx<x4:
        index=4
    else:
        index=5
    return index
print(main(56478))
    