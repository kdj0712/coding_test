def solution(numbers):
    for i in range(len(numbers)):
        numbers[i] = numbers[i]*2
    answer = numbers
    return answer

def solve():
    numbers = [1, 2, 100, -99, 1, 2, 3]
    answer = solution(numbers)
    print(answer)
    return

solve()