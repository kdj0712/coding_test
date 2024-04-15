def solution(age):
    answer = 2022 - (age-1)
    return answer

def solve():
    age = 40
    answer = solution(age)
    print("{}".format(answer))
    return

solve()