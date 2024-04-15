def solution(n):
    a = 0
    for i in range(n):
        if (n % (i+1)) == 0:
            a = a + 1
        elif (n % (i+1)) != 0: 
            pass
    answer = a
    return answer

def solve():
    n = 100
    answer = solution(n)
    print("{}".format(answer))
    return

solve()