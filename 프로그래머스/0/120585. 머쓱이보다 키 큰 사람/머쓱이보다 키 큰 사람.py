def solution(array, height):
    height = int(height)
    answer = []
    answer = array
    if height in answer:
        if answer.count(height) == 1:
            answer = sorted(answer)
            answer = len(answer) - len(range(answer.index(height)+1))
        elif answer.count(height) > 1:
            new_answer = [item for item in answer if item != height] 
            answer = list(set(new_answer)) 
            answer = new_answer.append(height)
            answer = sorted(new_answer)
            answer = len(answer) - len(range(answer.index(height)+1))
    else:
        array = array.append(height)
        answer = sorted(answer)
        answer = len(answer) - len(range(answer.index(height)+1))
    return answer

def solve():
    array = [180, 120, 140, 190, 191, 190, 150, 150, 167]
    height = 167
    answer = solution(array, height)
    print(answer)
    return

solve()