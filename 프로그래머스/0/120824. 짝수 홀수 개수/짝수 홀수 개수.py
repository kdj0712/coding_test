def solution(num_list):
    answer = []
    x = 0
    y = 0
    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            x = x + 1
        elif num_list[i] % 2 != 0:
            y = y + 1
    answer = [x, y]

    return answer

def solve():
    num_list = [1, 3, 5, 7]
    answer = solution(num_list)
    print(answer)
    return

solve()