def solution(my_string):
    import re
    numbers = re.findall(r'\d',my_string)
    answer = 0
    for x in range(len(numbers)):
        number = int(numbers[x])
        answer = answer + number
    return answer

def solve():
    my_string = "1a2b3c4d123"
    answer = solution(my_string)
    print("{}".format(answer))
    return

solve()