def solution(num1, num2):
    answer = (num1 / num2) * 1000
    return int(answer)

def solve():
    num1 = 3
    num2 = 2
    answer = solution(num1, num2)
    print("{}".format(answer))
    return

solve()