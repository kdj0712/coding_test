def solution(n):
    s = n % 7
    if s == 0:
        answer = n / 7
    elif s != 0:
        answer = (n / 7) + 1
    answer = int(answer)
    return answer

def solve():
    n = 5
    answer = solution(n)
    print("{}".format(answer))
    return

solve()