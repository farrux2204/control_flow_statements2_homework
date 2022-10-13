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
    answer=x1
    if answer<x2:
        answer=2
    if answer<x3:
        answer=3
    if answer<x4:
        answer=4
    if answer<x5:
        answer=5
    return answer
print(main(11986))
    