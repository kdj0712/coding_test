def solution(numbers, direction):
    numbers
    answer = []
    if direction == "right":
        answer.append(numbers[len(numbers)-1])
        for x in range(len(numbers)-1):
            answer.append(numbers[x])

    elif direction == "left":
        for y in range(len(numbers)-1):
            answer.append(numbers[y+1])
        answer.append(numbers[0])
    return answer

def solve():
    numbers = [4, 455, 6, 4, -1, 45, 6]
    direction = "left"
    answer = solution(numbers,direction)
    print("{}".format(answer))
    return

solve()