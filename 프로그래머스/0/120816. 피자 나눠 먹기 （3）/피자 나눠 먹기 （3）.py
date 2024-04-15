def solution(slice, n):
    s = n % slice
    if s == 0:
        answer = n / slice
    elif s != 0:
        answer = (n / slice) + 1
    answer = int(answer)
    return answer

def solve():
    slice = 7
    n = 10
    answer = solution(slice,n)
    print("{}".format(answer))
    return

solve()