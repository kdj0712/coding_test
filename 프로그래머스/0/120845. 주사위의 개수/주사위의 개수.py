def solution(box,n):
    num1 = box[0] / n
    num2 = box[1] / n
    num3 = box[2] / n
    answer = int(num1) * int(num2) * int(num3)
    return answer

def solve():
    box = [10,8,6]
    n = 3
    answer = solution(box,n)
    print("{}".format(answer))
    return

solve()