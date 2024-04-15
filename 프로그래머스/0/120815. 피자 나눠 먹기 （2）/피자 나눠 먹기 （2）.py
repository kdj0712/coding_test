def solution(n):
    answer = 0
    for i in range(100):
        if 6 * (i+1) % n == 0:
            answer = i+1
            break
    return answer

def solve():
    n = 10
    answer = solution(n)
    print("{}".format(answer))
    return

solve()