def solution(sides):
    sides = sorted(sides)
    sides0 = sides[0]
    sides1 = sides[1]
    sides2 = sides[2]
    if sides2 >= (sides0+sides1):
        answer = 2
    elif sides2 < (sides0+sides1):
        answer = 1
        pass
    return answer

def solve():
    sides = [199, 72, 222]
    answer = solution(sides)
    print(answer)
    return

solve()