def solution(n):
    answer = 0
    for i in range(n+1):
        if i % 2 == 0:
            answer = answer + i
        elif i % 2 != 0:
            pass
    return answer

def solve():
    n = 4
    answer = solution(n)
    print("{}".format(answer))
    return

solve()