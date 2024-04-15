def solution(n, t):
    answer = n
    for i in range(t):
        answer = answer * 2
        pass
    answer
    return answer

def solve():
    n = 2
    t = 10
    answer = solution(n, t)
    print(answer)
    return

solve()