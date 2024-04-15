def solution(y):
    num_list = [j for j in range(1,int(y)+1)]
    answer = [0]
    if y % 2 == 0:
        s = y / 2
        s = int(s)
    elif y % 2 != 0:
        s = (y / 2) + 1
        s = int(s)
        pass
    answer = answer * s
    z = 0
    for i in range(y):
        if num_list[i] % 2 != 0:
            answer[z] = num_list[i]
            z = z + 1
        elif num_list[i] %2 == 0:
            pass
    return answer

def solve():
    y = 15
    answer = solution(y)
    print(answer)
    return

solve()