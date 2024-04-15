def solution(array):
    array = sorted(array)
    s = len(array)
    if s % 2 == 0:
        s = (s / 2 ) - 1
        s = int(s)
    elif s % 2 != 0:
        s = (s / 2)
        s = int(s)
    answer = array[s]
    return answer

def solve():
    array = [9, -1, 0]
    answer = solution(array)
    print("{}".format(answer))
    return

solve()