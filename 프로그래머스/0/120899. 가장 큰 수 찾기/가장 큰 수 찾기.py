def solution(array):
    answer = []
    a = max(array)
    b = array.index(a)
    answer.append(a)
    answer.append(b)
    return answer

def solve():
    array = [9,10,11,8]
    answer = solution(array)
    print("{}".format(answer))
    return

solve()