def solution(num1, num2):
    if num1 == num2:
        answer = 1
    elif num1 != num2:
        answer = -1
    return int(answer)

def solve():
    num1 = 2
    num2 = 3
    answer = solution(num1, num2)
    print("{}".format(answer))
    return

solve()