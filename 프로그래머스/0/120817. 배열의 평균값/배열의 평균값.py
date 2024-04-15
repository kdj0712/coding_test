def solution(numbers):
    number = 0
    for i in range(len(numbers)):
        number += int(numbers[i])
    answer = number / len(numbers)
    return answer

def solve():
    numbers = [89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
    answer = solution(numbers)
    print("{}".format(round(answer,1)))
    return

solve()