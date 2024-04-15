def solution(money):
    answer = []
    answer1 = money / 5500
    answer1 = int(answer1)
    answer2 = money % 5500
    answer2 = int(answer2)
    answer = [answer1,answer2]
    return answer

def solve():
    money = 15000
    answer = solution(money)
    print("{}".format(answer))
    return

solve()