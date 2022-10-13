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
    if mx<x2:
        mx=2
    if mx<x3:
        mx=3
    if mx<x4:
        x=4
    else:
        mx=5
    return mx
print(main(18927))
    