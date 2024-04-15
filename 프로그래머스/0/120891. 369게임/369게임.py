def solution(order):
    x = [int(digit) for digit in str(order)]
    answer = 0
    for i in range(len(x)):
        if x[i] % 3 == 0 and x[i] !=0:
            answer = answer + 1
    return answer

def solve():
    order = 2942365418370
    answer = solution(order)
    print("{}".format(answer))
    return

solve()