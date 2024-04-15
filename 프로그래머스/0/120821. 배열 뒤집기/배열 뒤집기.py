def solution(numbers):
    answer = [0] * len(numbers)
    for i in range(len(numbers)):
        s = 0
        s = (len(numbers))-(i+1)
        answer[i] = numbers[s]
    return answer

def solve():
    numbers = [89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
    answer = solution(numbers)
    print(answer)
    return

solve()