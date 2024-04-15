def solution(numbers):
    numbers.sort()
    answer =  max(numbers[0]*numbers[1], numbers[-1]*numbers[-2])
    # 가장 작은 두 음수의 곱과 가장 큰 두 양수의 곱 중 더 큰 값 반환
    return answer

def solve():
    numbers = [1, 2, -3, 4, -5, -500]
    answer = solution(numbers)
    print("{}".format(answer))
    return

solve()
