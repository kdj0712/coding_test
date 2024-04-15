def solution(numbers):
    numbers
    numbers = sorted(numbers,reverse=False)
    a = numbers[len(numbers)-1]
    b = numbers[len(numbers)-2]
    answer = a * b
    return answer

def solve():
    numbers = [0, 31, 24, 10, 1, 9]
    answer = solution(numbers)
    print("{}".format(answer))
    return

solve()