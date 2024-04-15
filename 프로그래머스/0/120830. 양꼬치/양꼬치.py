def solution(n,k):
    
    if k > 0:
        if n >= 10:
            x = n / 10
            x = int(x)
        else:
            x = 0
            pass
    elif k == 0:
        x = 0
        pass
    
    k = k - x
    stick = 12000
    beverage = 2000
    answer = (n * stick) + (k * beverage)
    answer = int(answer)
    return answer

def solve():
    n = 10
    k = 3
    answer = solution(n,k)
    print("{}".format(answer))
    return