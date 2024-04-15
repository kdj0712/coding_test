def solution(n):
    answer = []
    for x in range(n+1):
        if  n % (x+1) == 0:
            answer.append(x+1)
    return answer

def solve():
    n = 24
    answer = solution(n)
    print("{}".format(answer))
    return

solve()